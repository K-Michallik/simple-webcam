#!/bin/sh
JSON=$1

# run manual test with payload
#remove the following line for real urcapx
JSON="{ \"idProduct\": \"1234\", \"idVendor\": \"1234\", \"logicalDevices\": [{\"deviceNode\": \"/devices/pci0000:00/0000:00:15.0/usb1/1-1/1-1:1.2/net/wlan0\", \"major\": 0, \"minor\": 0}], \"devicePath\": \"/devices/pci0000:00/0000:00:15.0/usb1/1-1\", \"manufacturer\": \"Realtek\", \"product\": \"802.11n NIC\", \"serial\": \"f84fad64143c\", \"urDeviceType\": \"NETWORK\", \"urDeviceAPIVersion\": \"1.0\" }"

# check we have json payload
if [ -z "$JSON" ]; then
  echo "json missing"
  exit 1;
fi

# check json payload version
APIVERSION=$(echo $JSON | jq -r .urDeviceAPIVersion)
if [ "$APIVERSION" != "1.0" ]; then
  echo "json version $APIVERSION not supported"
  exit 2
fi

# just handle NETWORK events
# NETWORK | SERIAL | VIDEO | ....
TYPE=$(echo $JSON | jq -r .urDeviceType)
if [ "$TYPE" != "NETWORK" ]; then
  echo "not network adaptor hotplug"
  exit 3
fi


# post json to rest application in urcapx
HTTP_CODE=$(curl --silent -o /dev/null -w "%{response_code}" -X POST -H 'Content-Type: application/json' -d "${JSON}" http://localhost:50052/device_add)
CODE=$?

# check curl was successfull
if [ $CODE -ne 0 ]; then
  echo "CURL failed (code: $code)"
  exit 4;
fi

# check http status code (200,404,...)
if [ $HTTP_CODE -ne 200 ]; then
	echo "APP reject device (http-code ${HTTP_CODE})"
  exit 1;
fi

echo "APP accept device"
exit 0
