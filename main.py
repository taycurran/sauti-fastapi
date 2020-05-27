from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

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