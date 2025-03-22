import pywifi
from pywifi import const

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(5)  # Wait for scan to complete
    results = iface.scan_results()
    for result in results:
        print(f"SSID: {result.ssid}")
        print(f"Signal: {result.signal} dBm")
        print(f"Encryption: {result.akm.encode('utf-8')}")
        print(f"Auth: {result.cipher.encode('utf-8')}")
        print("------------")

if _name_ == "_main_":
    scan_wifi()