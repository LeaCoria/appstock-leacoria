from query.register_new_item import (register_new_item_query,
                                     ItemAlreadyExistDB)


class ItemAlreadyExist(Exception):
    pass


class ModelNewItem():

    @classmethod
    def register_new_item(self, new_item):

        try:
            register_new_item_query(
                cod=new_item.cod,
                name=new_item.name,
                brand=new_item.brand,
                quantity=new_item.quantity
                )
        except ItemAlreadyExistDB:
            raise ItemAlreadyExist
