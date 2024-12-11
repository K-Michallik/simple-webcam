#!/usr/bin/env python3

# test payload
# "{ \"idProduct\": \"1234\", \"idVendor\": \"1234\", \"logicalDevices\": [{\"deviceNode\": \"/devices/pci0000:00/0000:00:15.0/usb1/1-1/1-1:1.2/net/wlan0\", \"major\": 0, \"minor\": 0}], \"devicePath\": \"/devices/pci0000:00/0000:00:15.0/usb1/1-1\", \"manufacturer\": \"Realtek\", \"product\": \"802.11n NIC\", \"serial\": \"f84fad64143c\", \"urDeviceType\": \"NETWORK\", \"urDeviceAPIVersion\": \"1.0\" }"
#

import json
import os
import sys
import requests
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("json_payload", help="JSON payload containing device add information")

def send_device_data_to_server(payload: dict) -> int:
    """
    Send device data to the FastAPI server and return the response exit code.
    """
    try:
        response = requests.post(
            url="http://localhost:50052/device_add",
            json=payload,
            timeout=5  # Adjust timeout as needed
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("exit_code", 1)  # Default to 1 if exit_code not in response
    except requests.RequestException as e:
        print(f"Error communicating with server: {e}", file=sys.stderr)
        return 1  # Reject device on communication failure

if __name__ == "__main__":
    # Parse arguments
    args = parser.parse_args()
    added_device_data = json.loads(args.json_payload)

    # Send device data to FastAPI server and get the exit code
    exit_code = send_device_data_to_server(added_device_data)

    # Exit with the code returned by the server
    exit(exit_code)