# to build app
from fastapi import FastAPI
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
# FastAPI is a Python class that provides all the functionality for this API
# the app variable serves as an "instance" of the class FastAPI
app = FastAPI()

# CORS - Cross-Origin Resource Sharing
# refers to the situations when a frontend running in a browser has 
# JavaScript code that communicates with a backend, 
# and the backend is in a different "origin" than the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# "path" is the last part of a URL starting from the first /
# "path" is commonly called an "endpoint" or "route"
# "operations" refers to one of the HTTP methods
# The @ indicates a "path operation decorator"
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