from app.crud.base import CRUDBase
from app.schemas.item import Item


class CRUDItem(CRUDBase):
    ...


item = CRUDItem(Item)
