from fastapi import APIRouter,Depends,Header,HTTPException,Body,Request
from fastapi.encoders  import jsonable_encoder
from fastapi.responses import JSONResponse
from controllers.health import CheckDataBaseConnection
from config import settings,sentry
from controllers import TokenJWT
from controllers import dda
import time
from datetime import datetime,timedelta
import json

router = APIRouter()

@router.get("/settings/app_status")
async def appStatus():

  DataBaseConnection = CheckDataBaseConnection()

  return JSONResponse (
    {
      "database": DataBaseConnection          
    }) 


  

  