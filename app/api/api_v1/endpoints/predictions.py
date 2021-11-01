from typing import Any

from fastapi import APIRouter, Body, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import json

from app.api import depends
from app.schema.prediction_output import PredictionOutput
from app.schema.prediction_input import PredictionInput
from app.model.RequestLog import RequestLog
from app.model.AppUser import AppUser

router = APIRouter()

@router.post("/predict_on_text", response_model=PredictionOutput)
def predict_on_text(
  input: PredictionInput,
  db: Session = Depends(depends.get_db),
  current_user: AppUser = Depends(depends.check_token)
) -> Any:
  '''
  Apply prediction on given text input
  '''
  try:
    model_input = input.data

    # TODO: 1. get model
    # model = Model.load()

    # TODO: 2. apply inference
    # model_output = model.predict()
    model_output = {"result": "1"}

    log = RequestLog(model_input, json.dumps(model_output), datetime.now().strftime("%Y-%m-%d %H:%M:%s"))
    db.add(log)
    db.commit()
  except:
    raise HTTPException(
      status_code=500,
      detail="Prediction couldn't be finished",
    )

  return model_output

@router.post("/prediction_on_file", response_model=PredictionOutput)
def prediction_on_file(
  input: UploadFile = File(...),
  db: Session = Depends(depends.get_db),
  current_user: AppUser = Depends(depends.check_token)
) -> Any:
  '''
  Apply prediction on given image or video
  '''
  try:
    model_input = input.file.read()

    # TODO: 1. get model
    # model = Model.load()

    # TODO: 2. apply inference
    # model_output = model.predict()
    model_output = {"result": "1"}

    log = RequestLog(input.filename, json.dumps(model_output), datetime.now().strftime("%Y-%m-%d %H:%M:%s"))
    db.add(log)
    db.commit()
  except:
    raise HTTPException(
      status_code=500,
      detail="Prediction couldn't be finished",
    )

  return model_output
