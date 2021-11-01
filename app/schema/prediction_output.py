from pydantic import BaseModel

class PredictionOutput(BaseModel):
  result: str