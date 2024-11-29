from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import logging

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the request model
class QuantumData(BaseModel):
    data: str

# Root endpoint
@app.get("/")
async def root():
    logging.info("Root endpoint accessed.")
    return {"message": "Welcome to Quantum-Compute API"}

# Handle requests to favicon.ico
@app.get("/favicon.ico")
async def favicon():
    logging.info("Favicon request handled.")
    return {"message": "Favicon not provided"}

# Quantum computation endpoint
@app.post("/quantum-compute/")
async def quantum_compute(data: QuantumData):
    quantum_api_url = "http://localhost:5000/quantum-endpoint"  # Update the URL to match Quantum-API's endpoint

    try:
        # Log the outgoing request
        logging.info(f"Sending data to Quantum-API: {data.dict()}")

        # Make a POST request to the Quantum-API
        response = requests.post(quantum_api_url, json=data.dict())
        response.raise_for_status()  # Raise an error for HTTP errors

        # Log the response
        quantum_result = response.json()
        logging.info(f"Received response from Quantum-API: {quantum_result}")

        # Return the response from Quantum-API
        return {"result": quantum_result}

    except requests.exceptions.RequestException as e:
        # Log the error
        logging.error(f"Error communicating with Quantum-API: {e}")

        # Return a custom error response
        raise HTTPException(status_code=500, detail=f"Error communicating with Quantum-API: {e}")
