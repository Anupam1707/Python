import network
import time

# Replace with your network credentials
SSID = 'anupam17'
PASSWORD = 'Anupam170107'

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print('Connecting to network...')
    while not wlan.isconnected():
        print('.', end='')
        time.sleep(1)
    
    print('\nConnected to network')
    print('Network config:', wlan.ifconfig())

# Connect to WiFi
connect_to_wifi(SSID, PASSWORD)
