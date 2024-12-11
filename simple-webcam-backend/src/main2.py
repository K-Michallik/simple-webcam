from fastapi import FastAPI, HTTPException, Response
import pysftp
import uvicorn
import socket
import os
import random

app = FastAPI()
PORT = 50052

REMOTE_IP = "10.0.0.168"
REMOTE_PATH = "/home/lab/psx/apple.png"
LOCAL_PATH = "/tmp/apple.png"
DEFAULT_USER = "lab"
DEFAULT_PASSWORD = "easybot"

# Optionally define cnopts to disable host key checking (if needed)
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  # Use this cautiously; prefer using known_hosts for security.

@app.get("/")
def root():
    return {"message": "Welcome to the simple External Communicator client"}


@app.get("/connect")
def connect_to_device(ip: str, port: int = 50051, message: str = "Hello world"):
    try:
        # Create a socket connection to the socket server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))

            # Send the provided message to the socket server
            s.sendall(message.encode())

            # Receive the response from the socket server
            data = s.recv(1024)

            # Decode the received data and return as JSON response
            response = data.decode()
            return {"response": response}

    except ConnectionRefusedError:
        raise HTTPException(status_code=500, detail="Connection to the socket server refused.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        s.close()

@app.get("/test")
def test_fn():
    return {"response":"Hello World"}

@app.get("/random-number")
async def get_random_number():
    return {"random_number": random.randint(1, 1000)}

@app.get("/scp_file")
def scp_file(username: str = DEFAULT_USER, password: str = DEFAULT_PASSWORD):
    print(os.getcwd())
    try:
        # Establish the SFTP connection using pysftp
        with pysftp.Connection(REMOTE_IP, username=username, password=password, cnopts=cnopts) as sftp:
            # Get the remote file and save it locally
            sftp.get(REMOTE_PATH, LOCAL_PATH)

        return {"message": "Success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    

@app.get("/image")
def get_image():
    hostname = REMOTE_IP
    port = 22
    username = DEFAULT_USER
    password = DEFAULT_PASSWORD # In production, use environment variables or secure methods to store credentials
    remote_path = REMOTE_PATH

    # Set up connection options
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # Disable host key checking (use with caution)

    try:
        # Establish SFTP connection
        with pysftp.Connection(host=hostname, port=port, username=username, password=password, cnopts=cnopts) as sftp:
            # Read the remote file into memory
            with sftp.open(remote_path, 'rb') as remote_file:
                file_data = remote_file.read()

        # Return the image data as an HTTP response
        return Response(content=file_data, media_type="image/png")
    except Exception as e:
        print(f"Error retrieving image: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving image")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
