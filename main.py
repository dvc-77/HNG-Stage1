from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/api")
async def root(slack_name:str, track:str):
    current_day = datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/dvc-77/HNG-Stage1/api/main.py",
        "github_repo_url": "https://github.com/dvc-77/HNG-Stage1",
        "status_code": 200
    }

    return response
