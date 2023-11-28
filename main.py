from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.data_manager import Data_Manager

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You might want to restrict this to specific origins in a production environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("https://localhost.com/{project_name}")
async def create_db_record(project_name):
    try:
        create_db = Data_Manager(project_name)
        
    except Exception as e:
        return 1