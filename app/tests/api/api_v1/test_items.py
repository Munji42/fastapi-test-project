from fastapi.testclient import TestClient


def test_read_item(client: TestClient) -> None:

    response = client.get(
        f"http://localhost:4200/api/v1/items",
    )
    assert response.status_code == 200
    content = response.json()[0]
    assert content["title"] == "title"
    assert content["description"] == "description"
