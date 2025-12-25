from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_wrong_file():
    response = client.post(
        "/upload-grades",
        files={"file": ("test.txt", b"bad")}
    )
    assert response.status_code == 400