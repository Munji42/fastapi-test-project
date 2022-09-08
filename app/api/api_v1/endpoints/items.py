from typing import Any, List

from fastapi import APIRouter

from app import crud, schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def read_items(
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    items = crud.item.get_multi(skip=skip, limit=limit)

    return items
