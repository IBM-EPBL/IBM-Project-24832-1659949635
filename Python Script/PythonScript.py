import json
import wiotp.sdk.device
import time

myconfig = {
    "identity": {
        "orgId":"hj5fmy",
        "typeId":"NodeMCU",
        "deviceId":"12345"
    },
    "auth": {
        "token":"12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myconfig, logHandlers=None)
client.connect()

while True:
    name= "Smartbridge"
    #in area location

    #latitude= 17.4225176
    #longitude= 78.5458842

    #out area= location

    latitude= 17.4225176
    longitude= 78.5458842
    myData={'name': name, 'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status",msgFormat='json',data=myData, qos=0, onpublish=None)
    print("Data published to IBM Iot Plaform: ",myData)
    time.sleep(5)
client.disconnect()
