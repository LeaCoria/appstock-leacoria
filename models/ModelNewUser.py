from query.create_user import (create_user,
                               UserAlreadyExistDB,
                               EmailAlreadyExistDB)


class EmailAlreadyExist(Exception):
    pass


class UserAlreadyExist(Exception):
    pass


class ModelNewUser():

    @classmethod
    def signup(self, newuser):

        try:
            create_user(
                email=newuser.email,
                password=newuser.password,
                username=newuser.username,
                name=newuser.name,
                last_name=newuser.lastname
            )
        except EmailAlreadyExistDB:
            raise EmailAlreadyExist
        except UserAlreadyExistDB:
            raise UserAlreadyExist
        return newuser
