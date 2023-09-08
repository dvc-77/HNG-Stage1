# HNG-Stage1

### Built with

- FastAPI
- Render

### Features:

- Retrieve Slack name and track information.
- Get the current day of the week and UTC time.
- Access GitHub URLs for the executed file and the project's source code.
- Response format adheres to JSON standards.
- Endpoint accessible publicly on Render.

### Endpoints

- `/api`: root endpoint
   - Method: GET
   - Parameters:
     - `slack_name` (string): The Slack name.
     - `track` (string): The chosen track.
   - Example: `GET /api?slack_name=Neil%20Ohene&track=backend`

### Response
```json
{
  "slack_name": "Neil Ohene",
  "current_day": "Friday",
  "utc_time": "2023-09-08T16:57:10Z",
  "track": "backend",
  "github_file_url": "https://github.com/dvc-77/HNG-Stage1/api/main.py",
  "github_repo_url": "https://github.com/dvc-77/HNG-Stage1",
  "status_code": 200
}
```

### Getting Started:
Follow these steps to run this repo locally:

- Fork or Clone the repository: git clone https://github.com/dvc-77/HNG-Stage1.git
- Create a virtual environment and install dependencies using pip `install -r requirements.txt`.
- Run the FastAPI app using `uvicorn main:app --reload --port=8000`.
- Access the API at http://localhost:8000/api and provide the required query parameters. 
    - Example: `/api?slack_name=Neil%20Ohene&track=backend`
