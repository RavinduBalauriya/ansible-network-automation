#  Scalable Network Automation & Disaster Recovery System

This project is a **Network Automation Framework** designed to manage, configure, and backup Cisco IOS devices at scale. It leverages **Ansible** for configuration management and **Python** for dynamic inventory generation, simulating a real-world enterprise environment.

## Project Overview

In traditional networking, configuring hundreds of routers manually is error-prone and time-consuming. This project solves that problem by:
1.  **Automating IP Management:** Assigning unique Loopback IPs dynamically.
2.  **Disaster Recovery:** Automatically fetching and saving running configurations locally.
3.  **Scalability:** Using a Python script to generate inventory for **100+ routers** instantly.

## Technologies Used

* **Core:** Ansible (Automation Engine), Python 3.
* **Environment:** GNS3 (Network Simulation), Linux Fedora (Control Node).
* **Networking:** Cisco IOS, SSH, TCP/IP.
* **Library:** Paramiko (SSH connectivity).

## Key Features

- **Dynamic Inventory Generation:** A custom Python script (`inventory_gen.py`) auto-generates the Ansible inventory file (`hosts_bulk.ini`), capable of scaling from 3 to 100+ devices.
- **Automated Provisioning:** Configures Loopback interfaces with unique IP addresses based on variable logic.
- **Automated Backups:** Pulls the `running-config` from all routers and saves them to a local directory for backup/restore purposes.
- **Legacy SSH Support:** Optimized `ansible.cfg` to handle cryptographic compatibility issues between modern Linux kernels and legacy Cisco devices (SHA1/RSA key negotiation).
- **Zero-Touch Key Verification:** Automated SSH host key acceptance for seamless mass deployment.
