from fastapi import FastAPI
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
import os

logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/")
def main():
    logger.info("HELLO WORLD")
    envs = []
    for key, value in os.environ.items():
        if key.startswith("X_"):
            envs.append({"name": key, "value": value})
    return {"hello": "world", "env": envs}
