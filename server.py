from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import logging
from src.io import Input, Output
from src.core import Core

app = FastAPI()


@app.post("/", response_model=Output)
async def ask(req: Input):
    core = Core(logging)
    data = jsonable_encoder(req)
    logging.info(f"input json: {data}")
    ans = core.run(data)
    logging.info(f"output json: {ans}")
    return ans
