import network
import time

# Initialize Wi-Fi interface in station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Scanning for Wi-Fi networks...")

# Scan for available Wi-Fi networks
networks = wlan.scan()

if networks:
    print(f"Found {len(networks)} network(s):")
    print("{:<30} {:<8} {:<6}".format('SSID', 'Channel', 'RSSI'))
    for net in networks:
        # Decode the SSID (which is in bytes) and print other details
        print("{:<30} {:<8} {:<6}".format(net[0].decode(), net[2], net[3]))
else:
    print("No Wi-Fi networks found.")

# Deactivate the Wi-Fi interface if not needed for further operations
wlan.active(False)