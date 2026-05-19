from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]

for device in devices:

    print("=" * 80)
    print(f"Connecting to {device['ip']}")
    print("=" * 80)

    net_connect = Netmiko(**device)

    output = net_connect.send_command(
        "show ip interface brief",
        use_textfsm=True
    )

    net_connect.disconnect()

    for interface in output:
        print(
            f"Interface: {interface['interface']:<25} "
            f"IP Address: {interface['ip_address']:<18} "
            f"Status: {interface['status']:<25} "
            f"Protocol: {interface['proto']}"
        )

    print("\n")
