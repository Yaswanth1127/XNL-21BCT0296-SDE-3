import requests

BASE_URL = "http://localhost:8000"

def test_login_endpoint():
    response = requests.get(f"{BASE_URL}/login")
    assert response.status_code == 200

def test_secure_api_endpoint():
    response = requests.get(f"{BASE_URL}/secure-api")
    assert response.status_code == 200

if __name__ == "__main__":
    test_login_endpoint()
    test_secure_api_endpoint()
    print("✅ All Integration Tests Passed Successfully!")
