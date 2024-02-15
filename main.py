from wifi import Cell, Scheme

# Scan for available Wi-Fi networks
def scan_wifi_networks():
    cells = Cell.all('wlan0')
    for cell in cells:
        print(f"SSID: {cell.ssid}, Signal Strength: {cell.signal}")

# Create a new Wi-Fi network
def create_wifi_network(ssid, password):
    scheme = Scheme.for_cell('wlan0', ssid, Cell.all('wlan0')[0], password)
    scheme.save()

# Example usage
if __name__ == "__main__":
    # Scan available networks
    print("Available Wi-Fi networks:")
    scan_wifi_networks()

    # Create a new Wi-Fi network
    new_ssid = input("Enter new Wi-Fi network name (SSID): ")
    new_password = input("Enter password for the new Wi-Fi network: ")
    create_wifi_network(new_ssid, new_password)
    print(f"Wi-Fi network '{new_ssid}' created successfully!")
