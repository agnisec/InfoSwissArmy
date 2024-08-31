InfoSwissArmy is an all purpose "scanner" that is built to expanded upon and tailored to specific needs. The core function of the program relies on "blades" which are python scripts that perform specific/repeatable tasks such as gathering OS version of a given host. The results are stored in a local sqlite db that is stores results based on the host IP. The DB is interactable through the HostDataKnife.py script which allows the user to gather all results for a given host, delete a specific host from the DB, or remove all results from the DB. 

**Dependencies:**
Python3 (see requirements.txt for required python packages)
sqlite
Nmap

**Tool Structure:**
InfoSwissArmy/
│
├── db/
│   └── vuln_data.db            # SQLite database storing scan results
│
├── blades/
│   ├── __init__.py             # Initializes the blades package
│   ├── os_version_ssh.py       # Blade for checking OS version via SSH
│   ├── os_version_nmap.py      # Blade for checking OS version via nmap
│   └── port_scan_nmap.py       # Blade for performing a basic port scan using nmap
│
├── scanner.py                  # Core scanner logic, handles blade execution and result saving
├── blade_manager.py            # Manages the loading and execution of blades
├── cli.py                      # CLI interface for running the InfoSwissArmy tool
├── db_manager.py               # Script to manage the database (retrieve, delete entries)
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation for the project



**InfoSwissArmy.py Usage:**

Basic Command (runs all blades as default)
python InfoSwissArmy.py <host_ip> 

Blade Specific Command (runs specified plugin, SSH based commands requires credentials)
python InfoSwissArmy.py <host_ip> --username <username> --password <password> --blade os_version_SSH

Blade Specific Command (non-SSH based commands do not require credentials)
python InfoSwissArmy.py <host_ip> --blade os_version_nmap

Blade Specific Command for port scanning
python InfoSwissArmy.py <host_ip> --blade port_scan_nmap


**HostDataKnife.py Usage**

Get all scan results in db for given host
python HostDataKnife.py <host_ip> --get

Delete given host from db
python HostDataKnife.py <host_ip> --delete-host

Delete all data from db
python HostDataKnife.py --delete-all



**Current Available Blades:**
os_version_ssh: uses provides username and password/key file to login to host and gather OS version
os_version_nmap: uses nmap to run a remote check and does its best to gather the OS version
port_scan_nmap: used to perform a basic SYN scan (-sS) and OS detection (-O) on the top 1000 most common ports (--top-ports 1000).
