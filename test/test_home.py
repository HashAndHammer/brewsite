from app.brewsite import app


def test_home():
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to our brewsite page" in response.data

    response = client.get("/breweries")
    assert response.status_code == 200

    response = client.get("/beer_types")
    assert response.status_code == 200

    response = client.get("/about")
    assert response.status_code == 200