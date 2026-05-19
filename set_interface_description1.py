from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22",
    }
]

# Configuration commands
loopback_config = [
    "interface Loopback0",
    "ip address 1.1.1.1 255.255.255.255",
    "description Loopback configured with Netmiko",
    "no shutdown"
]

for device in devices:

    print(f"Connecting to {device['ip']}")

    net_connect = Netmiko(**device)

    # Send configuration commands
    output = net_connect.send_config_set(loopback_config)

    print(output)

    # Verify configuration
    verify = net_connect.send_command("show ip interface brief")

    print("\nVerification:")
    print(verify)

    net_connect.disconnect()
