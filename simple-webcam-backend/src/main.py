from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional
import logging
import os

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
    logicalDevices: Optional[List[dict]] = None
    devicePath: Optional[str] = None
    manufacturer: str
    product: str
    serial: str
    urDeviceType: str
    urDeviceAPIVersion: str

@app.get("/")
def root():
    return {"message": "Welcome to the Simple Webcam server."}

### Uncomment the below "device_add" endpoint if you are having trouble with the DevicePayload model.
# @app.post("/device_add")
# async def device_add(request: Request):
#     raw_payload = await request.json()
#     logging.info(f"Raw payload received: {raw_payload}")

#     # Check device type
#     device_type = raw_payload.get("urDeviceType", "").lower()
#     if device_type == "video":
#         logging.info("Device accepted (type: video).")
#         return {"exit_code": os.EX_OK}
#     else:
#         logging.info(f"Device rejected (type: {device_type}).")
#         return {"exit_code": 1}
#
# @app.post("/device_remove")
# async def device_remove(request: Request):
#     raw_payload = await request.json()
#     logging.info(f"Raw payload received: {raw_payload}")
#     logging.info(f"Device was removed.")
#     return {"exit_code": os.EX_OK}

@app.post("/device_add")
async def device_add(payload: DevicePayload):
    try:
        # Log the validated payload
        logging.info(f"Validated payload: {payload}")

        # Check the device type
        device_type = payload.urDeviceType.lower()
        if device_type == "video":
            logging.info("Device accepted (type: video).")
            return {"exit_code": os.EX_OK}
        else:
            logging.info(f"Device rejected (type: {device_type}).")
            return {"exit_code": 1}
    except Exception as e:
        logging.error(f"Error processing payload: {e}")
        raise HTTPException(status_code=400, detail="Invalid payload")

@app.post("device_remove")
async def device_remove(payload: DevicePayload):
    try:
        # Log the validated payload
        logging.info(f"Validated payload: {payload}")
        logging.info(f"Device was removed.")
        
        # Note for device removals the exit code does not matter.
        return {"exit_code": os.EX_OK}
    except Exception as e:
        logging.error(f"Error processing payload: {e}")
        raise HTTPException(status_code=400, detail="Invalid payload")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
