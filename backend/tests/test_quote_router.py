import pytest
import httpx

@pytest.mark.asyncio
async def test_create_quote_with_new_source(client: httpx.AsyncClient):
    # First, create a user
    user_data = {"email": "test@example.com", "username": "testuser", "password": "password"}
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    user_id = response.json()["user"]["id"]

    # Then, create a quote with a new source
    quote_data = {
        "content": "This is a test quote.",
        "user_id": user_id,
        "source": {
            "title": "Test Book",
            "source_type": "book",
            "creator": "Test Author",
        },
    }
    response = await client.post("/quote/with_source", json=quote_data)
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == quote_data["content"]
    assert data["user_id"] == quote_data["user_id"]
    assert data["source_id"] is not None

@pytest.mark.asyncio
async def test_create_quote_with_existing_source(client: httpx.AsyncClient):
    # First, create a user
    user_data = {"email": "test2@example.com", "username": "testuser2", "password": "password"}
    response = await client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    user_id = response.json()["user"]["id"]

    # Then, create a producer
    producer_data = {"name": "Test Producer", "pd_type": "publisher"}
    response = await client.post("/producers/", json=producer_data)
    assert response.status_code == 200
    producer_id = response.json()["id"]

    # Then, create a source
    source_data = {
        "title": "Another Test Book",
        "source_type": "book",
        "creator": "Another Test Author",
        "pd_id": producer_id,
        "data": {},
    }
    response = await client.post("/source/", json=source_data)
    assert response.status_code == 200
    source_id = response.json()["id"]

    # Then, create a quote with the existing source
    quote_data = {
        "content": "This is another test quote.",
        "user_id": user_id,
        "source_id": source_id,
    }
    response = await client.post("/quote/", json=quote_data)
    assert response.status_code == 200
    data = response.json()
    assert data["content"] == quote_data["content"]
    assert data["user_id"] == quote_data["user_id"]
    assert data["source_id"] == source_id