from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
app = FastAPI()
PORT = 50052

class DevicePayload(BaseModel):
    idProduct: str
    idVendor: str
    logicalDevices: list
    devicePath: str
    manufacturer: str
    product: str
    serial: str
    urDeviceType: str
    urDeviceAPIVersion: str

@app.get("/")
def root():
    return {"message": "Welcome to the Simple Webcam server."}

@app.post("/device_add")
async def device_add(payload: DevicePayload):
    try:
        # Log received payload
        logging.info(f"Received payload: {payload}")

        # Check the urDeviceType field
        if payload.urDeviceType.lower() == "video":
            logging.info("Device accepted (type: video).")
            return {"exit_code": 0}
        else:
            logging.info(f"Device rejected (type: {payload.urDeviceType}).")
            return {"exit_code": 1}
    except Exception as e:
        logging.error(f"Error processing payload: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
