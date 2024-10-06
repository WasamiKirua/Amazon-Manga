# src/app.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Initialize FastAPI app
app = FastAPI()

# Serve static files (for Bootstrap and custom styles)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="src/templates")


# Define the index route
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define a status endpoint to verify the application is running
@app.get("/status")
def read_status():
    return {"status": "running", "app": "FastAPI Application", "version": "1.0"}
