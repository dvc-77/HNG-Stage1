import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from dateutil.parser import isoparse

from main import app


client = TestClient(app)

test_data = {
  "slack_name": "example_name",
  "track": "backend",
}

query_params = f"/api?slack_name={test_data['slack_name']}&track={test_data['track']}"

def test_endpoint_accessible():
    response = client.get(query_params)
    assert response.status_code == 200

def test_json_format(): 
    response = client.get(query_params)
    assert response.status_code == 200
    data = response.json()
    expected_keys = [
        "slack_name", 
        "current_day", 
        "utc_time", 
        "track",
        "github_file_url", 
        "github_repo_url",
        "status_code"]
    assert all(key in data for key in expected_keys)

def test_data_valid():
    response = client.get(query_params)
    current_day = datetime.utcnow().strftime('%A')
    data = response.json()

    try:
        utc_time = isoparse(data["utc_time"])
    except ValueError:
        pytest.fail("Invalid UTC time format")
    

    assert response.status_code == 200
    assert data["slack_name"] == test_data["slack_name"]
    assert data["current_day"] == current_day
    assert data["track"] == test_data["track"]
    assert data["github_file_url"] == "https://github.com/dvc-77/HNG-Stage1/api/main.py"
    assert data["github_repo_url"] == "https://github.com/dvc-77/HNG-Stage1"



