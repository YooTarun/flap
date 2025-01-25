from app import app  # Import the Flask app from your file

def test_home():
    # Create a test client
    with app.test_client() as client:
        # Send a GET request to the "/" route
        response = client.get("/")
        # Assert that the status code is 200
        assert response.status_code == 200
        # Assert that the response data matches the expected output
        assert response.data == b"Hello World!"
