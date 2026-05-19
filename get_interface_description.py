from netmiko import ConnectHandler

# Define all routers
r1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

r2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": "22"
}

# Add more routers if needed
devices = (r1, r2)

# Loop through all devices
for device in devices:

    print("=" * 100)
    print(f"Connecting to {device['ip']}")
    print("=" * 100)

    net_connect = ConnectHandler(**device)

    output = net_connect.send_command("show interface description")

    print(output)

    net_connect.disconnect()

    print("\n")
