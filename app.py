from flask import (Flask,
                   render_template,
                   request, redirect,
                   url_for,
                   flash)
from flask_login import (LoginManager, login_user, logout_user,
                         login_required, current_user)

from config import config, _get_db_connection

# Models:
from models.ModelUser import ModelUser
from models.ModelNewUser import (ModelNewUser,
                                 EmailAlreadyExist,
                                 UserAlreadyExist)
from models.Forms import (SignUpForm,
                          RegisterItemForm,
                          AddQuantityForm,
                          SubstractQuantityForm)
from models.ModelNewItem import (ModelNewItem, ItemAlreadyExist)

# Entities:
from models.entities.User import User
from models.entities.NewUser import NewUser
from models.entities.Item import Item

# Querys
from query.get_all_users import _get_all_users
from query.make_admin import make_admin_query
from query.unmake_admin import unmake_admin_query
from query.search_item import search_item
from query.add_quantity import _add_quantity
from query.get_all_items import _get_all_items
from query.substract_quantity import _substract_quantity
from query.make_me_admin import make_me_admin_query
from query.first_query import (_create_table_items,
                               _create_table_users,
                               _insert_admin,
                               _insert_items)

app = Flask(__name__)

app.secret_key = "AB!iwcNAt1^%kvhUI*S^"

db = _get_db_connection()

login_manager_app = LoginManager(app)


def first_query():
    try:
        _create_table_users(db)
        _create_table_items(db)
        _insert_admin(db)
        _insert_items(db)
        return None
    except Exception:
        return None


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    first_query()
    try:
        current_user.name
        return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('login'))


# MÉTODO DE LOGEO AUTENTICANDO LOS DATOS CON LA BASE DE DATOS
@app.route('/login', methods=['GET', 'POST'])
def login():
    first_query()
    if request.method == 'POST':
        user = User(
            0,
            username=request.form['username'],
            password=request.form['password']
        )
        logged_user = ModelUser.login(db, user)
        if logged_user is not None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Password invalid")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        try:
            current_user.name
            return redirect(url_for('home'))
        except AttributeError:
            return render_template('auth/login.html')


# MÉTODO DE REGISTRO EN LA BASE DE DATOS
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    first_query()
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        newuser = NewUser(request.form['email'],
                          NewUser.save_password(request.form['password']),
                          request.form['username'],
                          request.form['name'],
                          request.form['lastname']
                          )
        try:
            ModelNewUser.signup(newuser)
            flash("Register succesfully!!!")
            return redirect(url_for('signup'))
        except EmailAlreadyExist:
            flash("Email already register")
            return render_template('auth/signup.html', form=form)
        except UserAlreadyExist:
            flash("Username already register")
            return render_template('auth/signup.html', form=form)
    else:
        try:
            current_user.name
            return redirect(url_for('home'))
        except AttributeError:
            return render_template('auth/signup.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/users')
@login_required
def users():
    if current_user.admin:
        all_users = _get_all_users()
        return render_template('users.html', all_users=all_users)
    else:
        return redirect(url_for('home'))


@app.route('/make_admin', methods=['GET', 'POST'])
@login_required
def make_admin():
    if current_user.admin and request.method == 'POST':
        make_admin_query(request.form['username'])
        return redirect(url_for('users'))
    else:
        return redirect(url_for('home'))


@app.route('/make_me_admin', methods=['GET', 'POST'])
@login_required
def make_me_admin():
    if current_user.admin and request.method == 'GET':
        return redirect(url_for('home'))
    else:
        if request.method == 'POST':
            make_me_admin_query(request.form['username'])
            return redirect(url_for('home'))
        else:
            return render_template('make_me_admin.html')


@app.route('/unmake_admin', methods=['GET', 'POST'])
@login_required
def unmake_admin():
    if current_user.admin and request.method == 'POST':
        unmake_admin_query(request.form['username'])
        return redirect(url_for('users'))
    else:
        return redirect(url_for('home'))


@app.route('/items')
@login_required
def items():
    all_items = _get_all_items()
    return render_template('items.html', all_items=all_items)


@app.route('/purchase_item', methods=['GET', 'POST'])
@login_required
def purchase_item():
    item = Item(request.form['cod'],
                request.form['name'],
                request.form['brand'],
                request.form['current_cuantity'])
    return render_template('purchase_item.html',
                           item=item,
                           show_errors=False)


@app.route('/substract_quantity', methods=['GET', 'POST'])
@login_required
def substract_quantity():
    form = SubstractQuantityForm(request.form)
    if request.method == 'POST' and form.validate():
        if (int(request.form['quantity_to_substract']) <
                int(request.form['current_cuantity'])):
            _substract_quantity(request.form['quantity_to_substract'],
                                request.form['current_cuantity'],
                                request.form['cod'])
            flash("Item purchased successfully!!!")
            return redirect(url_for('items'))
        else:
            flash("You try to purchase more items than existing items!!!")
            return redirect(url_for('items'))
    else:
        return render_template('purchase_item.html',
                               item=Item(request.form['cod'],
                                         request.form['name'],
                                         request.form['brand'],
                                         request.form['current_cuantity']),
                               show_errors=True,
                               form=form)


@app.route('/add_items', methods=['GET', 'POST'])
@login_required
def add_items():
    if current_user.admin and request.method == 'POST':
        try:
            item = search_item(request.form['cod'])
            return render_template('add_items.html',
                                   show_item=True,
                                   show_errors=False,
                                   item=item)
        except Exception:
            flash("The item is not register")
            return render_template('add_items.html', show_item=False)
    elif current_user.admin:
        return render_template('add_items.html', show_item=False)
    else:
        return redirect(url_for('home'))


@app.route('/add_quantity', methods=['GET', 'POST'])
@login_required
def add_quantity():
    form = AddQuantityForm(request.form)
    if (current_user.admin and request.method == 'POST' and form.validate()):
        _add_quantity(request.form['quantity_to_add'],
                      request.form['current_cuantity'],
                      request.form['cod'])
        flash("Item added succesfully!!!")
        return redirect(url_for('add_items'))
    elif current_user.admin and not form.validate():
        return render_template('add_items.html',
                               show_item=True,
                               show_errors=True,
                               item=search_item(request.form['cod']),
                               form=form)
    else:
        return redirect(url_for('home'))


@app.route('/register_new_item', methods=['GET', 'POST'])
@login_required
def register_new_item():
    form = RegisterItemForm(request.form)
    if current_user.admin and request.method == 'POST' and form.validate():
        new_item = Item(request.form['cod'],
                        request.form['name'],
                        request.form['brand'],
                        request.form['quantity'])
        try:
            ModelNewItem.register_new_item(new_item)
            flash("Register item succesfully!!!")
            return redirect(url_for('register_new_item'))
        except ItemAlreadyExist:
            flash("Item already register")
            return redirect(url_for('register_new_item'))

    elif current_user.admin:
        return render_template('register_new_item.html', form=form)
    else:
        return redirect(url_for('home'))


# REDIRECCIÓN PARA USUARIOS QUE INTENTEN ENTRAR A PÁGINAS PRIVADAS SIN ESTAR
# AUTENTICADOS
def status_401(error):
    return redirect(url_for('login'))


# CARTERL ANTE URL INEXISTENTE
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
