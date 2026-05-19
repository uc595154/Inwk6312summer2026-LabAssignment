from netmiko import Netmiko
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },
    # Add more devices as needed
]

for device in devices:
    print(f"\nConnecting to {device['ip']}...")

    try:
        net_connect = Netmiko(**device)

        print(f"Default prompt: {net_connect.find_prompt()}")

        net_connect.send_command_timing("disable")
        print(f"Disable prompt: {net_connect.find_prompt()}")

        net_connect.enable()
        print(f"Enable prompt: {net_connect.find_prompt()}")

        net_connect.disconnect()

    except NetmikoTimeoutException:
        print(f"Connection timed out for {device['ip']}")

    except NetmikoAuthenticationException:
        print(f"Authentication failed for {device['ip']}")

    except Exception as e:
        print(f"Error with {device['ip']}: {e}")
