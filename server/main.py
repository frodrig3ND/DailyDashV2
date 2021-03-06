from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://192.168.1.181",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://192.168.1.181:8081",
    "http://192.168.1.181:8080",
    "http://rasp-srv:8000",
    "http://192.168.1.232",
    "http://192.168.1.181:8888",
    "//rasp-srv",
]

origins_all = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_all,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .water import create_module as water_create  # noqa: E402
from .vitamin import create_module as vitamin_create  # noqa: E402
from .task import create_module as task_create  # noqa: E402
from .strava import create_module as strava_create  # noqa: E402

water_create(app)
vitamin_create(app)
task_create(app)
strava_create(app)