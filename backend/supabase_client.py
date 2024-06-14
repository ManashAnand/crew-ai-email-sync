import supabase
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
import os

app = FastAPI()

SUPABASE_URL = "https://hpihmxbhkffomzcsckue.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwaWhteGJoa2Zmb216Y3Nja3VlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDMwMDA2NjIsImV4cCI6MjAxODU3NjY2Mn0.kOhuwmFGxDxRt65dQaCOxDvW4ETM7kV3UfCUzn54BwA"
client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

# class HealthResponse(BaseModel):
#     message: str
#     data: dict = None
#     error: str = None



@app.get("/health")
async def health_check():
    try:
        
        # return {"message": "API is healthy"}
        response = client.from_("emails").select("*").execute()
     
        print(response)

        # # Check if the response has data and return the appropriate message
        if response.data:
            return {"message": "API is healthy", "data": response.data}
        else:
            return {"message": "API is not healthy", "error": "No data found"}
    except Exception as e:
        # Return the error message in case of an exception
        return {"message": "API is not healthy", "error": str(e)}



@app.get("/emails")
async def get_emails():
    print("Working")
    response = client.table('emails').select("*").execute()
    print(response)
    return response.data