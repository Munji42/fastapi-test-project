class CRUDBase:
    def __init__(self, model):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model


    def get(self):
        return {"title": "title", "description": "description"}

    def get_multi(self, *, skip: int = 0, limit: int = 100):
        return [{"title": "title", "description": "description"}]
