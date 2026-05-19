for interface in output:
    print(
        f"{interface['interface']} "
        f"{interface['ip_address']} "
        f"{interface['status']} "
        f"{interface['proto']}"
    )
