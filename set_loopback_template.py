import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load YAML files
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Jinja2 environment
env = Environment(
    loader=FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template('interfaces_config_template.j2')

# Render config
loopback_config = template.render(data=interfaces)

# Convert into list of commands
config_commands = loopback_config.split("\n")

# Connect to devices
for host in hosts["hosts"]:

    print(f"Logged into {host['name']} successfully")

    net_connect = Netmiko(
        host=host["name"],
        username=host["username"],
        password=host["password"],
        port=host["port"],
        device_type=host["type"]
    )

    output = net_connect.send_config_set(config_commands)

    print(f"Pushed config into {host['name']} successfully")

    net_connect.disconnect()

print("Done!")
