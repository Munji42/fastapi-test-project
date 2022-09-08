from app import crud


def test_get_item() -> None:
    stored_item = crud.item.get()
    assert stored_item
    assert "title" == stored_item["title"]
    assert "description" == stored_item["description"]
