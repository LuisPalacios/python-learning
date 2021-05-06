# main.py

# Install the following dependencies from this requirements.txt file:
#fastapi
#uvicorn
#uvloop
#gunicorn
#httptools

# virtualenv venv
# source venv/bin/activate
# pip freeze

# pip install fastapi uvicorn uvloop gunicorn httptools

# pip freeze


# Testing: 
# Run the server for testing and reloading. 
#       uvicorn main:app --reload 
# In production, 
#   gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app
#
from typing import Optional
from fastapi import FastAPI
app = FastAPI(title="My greeting server")
@app.get("/api/greet")
async def greet(name: Optional[str] = None):
    if name is None:
        name = "Luis"
    return { "greeting": f"Hello, {name}!" }
