# to build app
from fastapi import FastAPI, File, UploadFile
# allows web team access to app
from fastapi.middleware.cors import CORSMiddleware
# allows you to create a class to structure POST input
from pydantic import BaseModel
# allows for html rendering
from fastapi.responses import HTMLResponse
# for data handling
import pandas as pd

# allows main to get modules from various files in current dir
# from fastapi import APIRouter
# router = APIRouter()

# ----------------------------------------------------------------------------
# --- DB Stuff ---
from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# import pstgres.models, pstgres.schemas, pstgres.crud
# from pstgres.aws_db import SessionLocal, engine
# from pstgres.models import Base

# Base.metadata.create_all(bind=engine)
# --- -------- ---

app = FastAPI()

# Dependency
# def get_db():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close()



# CORS - Cross-Origin Resource Sharing
# Gives Web Team Access to API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
  """
  Sauti Market Monitor API  
  Verifies the API is deployed, and links to the docs.
  """
  return HTMLResponse("""
  <h1>Sauti Market Monitor</h1>
  <p>Go to <a href="/docs">/docs</a> for documentation.</p>
  """)

@app.get("/qc_wholesale")
async def qc_wholesale():
  qc_ws = pd.read_csv("app/qc_wholesale.csv")
  qc_ws = qc_ws.to_json()
  return qc_ws

# POST Root Example
class Story(BaseModel):
  title: str
  text: str

@app.post("/predict")
async def predict(story: Story):
  """
  Predicts whether a product-market pair is normal, stress, or crisis level.

  Naive Baseline: Always predicts 'Normal"
  """

  # Not doing anything but verifying that we can read it.
  print(story)
  X = pd.DataFrame([dict(story)])
  print(X.to_markdown())

  return {
      'level': 'normal',
      'probability': 0.50
  }