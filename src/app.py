# src/app.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
from .utils import *

# Initialize FastAPI app
app = FastAPI()

# Serve static files (for Bootstrap and custom styles)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="src/templates")

# Create DB if does not exists
create_sqlite_database()

# Create Tables if not exist
create_main_tables()

# Define the index route
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route for the Add Manga page
@app.get("/add-manga", response_class=HTMLResponse)
async def get_add_manga(request: Request):
    return templates.TemplateResponse("add_manga.html", {"request": request})

# Handle form submission from the Add Manga page
@app.post("/add-manga", response_class=HTMLResponse)
async def post_add_manga(request: Request, manga_urls: str = Form(...)):
    # Split the input by newlines to handle multiple URLs if entered
    urls_list = [url.strip() for url in manga_urls.splitlines() if url.strip()]
    
    # For debugging purposes, print the URLs entered
    print("Manga URLs Submitted:", urls_list)

    # Adding urls to the db for a later parsing
    for url in urls_list:
        clean_url = url.strip().lower()
        add_url(clean_url)

    # Display a confirmation message in the response
    message = f"URLs submitted and added to the database successfully!"


    # Pass the submitted URLs and message back to the template for feedback
    return templates.TemplateResponse("add_manga.html", {
        "request": request,
        "submitted_urls": urls_list,
        "message": message
    })

# Define a status endpoint to verify the application is running
@app.get("/status")
def read_status():
    return {"status": "running", "app": "FastAPI Application", "version": "1.0"}
