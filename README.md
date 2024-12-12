# Simple-Webcam

This sample provides a practical way to manage USB devices like webcams using a backend server built with FastAPI. The system handles events for connecting and disconnecting devices, while the frontend includes a toggle button to control the webcam feed. For more information about device types in Polyscope X, please see our [documentation](https://docs.universal-robots.com/). 

> [!NOTE]
> This sample currently only works on a physical controller. It will fail on the simulator.

---

## **Key Features**

### **Backend (FastAPI)**

- **Device Add Endpoint** (`/device_add`):
  - Processes information when a USB device is connected.
  - Decides whether to accept or reject the device.
  - Logs key details about the device and the action taken.
- **Device Remove Endpoint** (`/device_remove`):
  - Handles events when a USB device is disconnected.
  - Logs the removal for future reference.

### **Frontend**

- **Webcam Demo**:
  - The frontend utilizes the `ngx-webcam` library. It runs a modified version of the [ngx-webcam-demo](https://github.com/basst314/ngx-webcam-demo) with buttons to toggle the webcam and take a snapshot
  

---

## **How It Works**

1. **Device Add Process**:

   - When a USB device is plugged in, `on_device_add.py` runs automatically.
   - This script parses the device details and sends them to the `/device_add` endpoint.
   - The backend validates the details, checks the device type, and logs whether the device is accepted or rejected.

2. **Device Remove Process**:

   - When a USB device is unplugged, `on_device_remove.py` runs automatically.
   - This script sends the device information to the `/device_remove` endpoint.
   - The backend logs the removal for records or debugging.

3. **Frontend Integration**:

   - A toggle button in the frontend lets users enable or disable the webcam feed.
   - Clicking the button sends a request to the backend to update the webcam's state.


## **API Endpoints**

### **POST /device\_add**

- **Purpose**: Handles new device connections.
- **Request Body (sample)**:
  ```json
  {
    "idProduct": "2137",
    "idVendor": "0bda",
    "logicalDevices": [
      {"deviceNode": "/dev/video0", "major": 81, "minor": 0}
    ],
    "manufacturer": "HFGK-N",
    "product": "USB Camera",
    "serial": "200901010001",
    "urDeviceType": "VIDEO",
    "urDeviceAPIVersion": "0.1"
  }
  ```
- **Response**:
  - `200 OK` with an `exit_code` field (0 = accepted, 1 = rejected).

### **POST /device\_remove**

- **Purpose**: Logs device disconnections.
- **Request Body (sample)**:
  ```json
  {
    "idProduct": "2137",
    "idVendor": "0bda",
    "logicalDevices": [
      {"deviceNode": "/dev/video0", "major": 81, "minor": 0}
    ],
    "manufacturer": "HFGK-N",
    "product": "USB Camera",
    "serial": "200901010001",
    "urDeviceType": "VIDEO",
    "urDeviceAPIVersion": "0.1"
  }
  ```
- **Response**:
  - `200 OK` (exit codes are not relevant here).

---

## **Logging System**

Each component uses logging to keep track of events and actions:

- **`main.py`**: Logs device decisions and frontend requests.
- **`on_device_add.py`**: Logs initialization and device addition processing.
- **`on_device_remove.py`**: Logs initialization and device removal events.

### Example Logs:

```plaintext
2024-12-12 15:01:36,728 - main - DEBUG - Validated payload: idProduct='2137' idVendor='0bda' logicalDevices=[{'deviceNode': '/dev/video1', 'major': 81, 'minor': 1}, {'deviceNode': '/dev/video0', 'major': 81, 'minor': 0}] manufacturer='HFGK-N' product='USB Camera' serial='200901010001' urDeviceType='VIDEO' urDeviceAPIVersion='0.1'
2024-12-12 15:01:36,728 - main - INFO - Device was removed.
```

---
## **Installation**
To install the contribution type:

`$ npm install`

### Build
To build the contribution type:

`$ npm run build`

### Deploy
To deploy the contribution to the simulator type:

`$ npm run install-urcap`

### Further help

Get more help from the included SDK documentation.

## **License**

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **How to Contribute**

We encourage contributions! Please fork the repository, make your changes, and submit a pull request.

