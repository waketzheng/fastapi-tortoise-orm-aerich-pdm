#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

try:
    from app.settings import TORTOISE_ORM
except ImportError:
    print("You may need to explicit declare:\n\n  export PYTHONPATH=.\n")
    raise

app = FastAPI(title="Good good study, day day up")
register_tortoise(app, config=TORTOISE_ORM)


if __name__ == "__main__":
    uvicorn.run("__main__:app", reload=True)
