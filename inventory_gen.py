with open("hosts_bulk.ini", "w") as f:
    f.write("[routers]\n")
    
    
    for i in range(1, 101):
        
        
        if i == 1:
            mgmt_ip = "192.168.56.200"  
        elif i == 2:
            mgmt_ip = "192.168.56.201"  
        elif i == 3:
            mgmt_ip = "192.168.56.202"  
        else:
            mgmt_ip = f"192.168.56.{100 + i}" 
            
        new_ip = f"10.10.10.{i}"
        
        f.write(f"R{i} ansible_host={mgmt_ip} new_ip={new_ip}\n")

    
    f.write("\n[routers:vars]\n")
    f.write("ansible_user=admin\n")
    f.write("ansible_password=cisco\n")
    f.write("ansible_connection=network_cli\n")
    f.write("ansible_network_os=cisco.ios.ios\n")
    f.write("ansible_ssh_common_args='-o StrictHostKeyChecking=no -o KexAlgorithms=+diffie-hellman-group1-sha1 -o Ciphers=+aes128-cbc,3des-cbc -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa'\n")

print("Hybrid Inventory Generated: R1-R3 are REAL, R4-R100 are FAKE.")
