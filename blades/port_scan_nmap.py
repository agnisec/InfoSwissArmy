import nmap

def check_vulnerability(host, username=None, password=None, key_file=None):
    nm = nmap.PortScanner()
    
    try:
        # Perform a basic scan on the top 1000 ports
        nm.scan(hosts=host, arguments='-sS -O --top-ports 1000')
        
        open_ports = []
        
        # Parse the results
        if host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    state = nm[host][proto][port]['state']
                    if state == 'open':
                        open_ports.append(port)
        
        if open_ports:
            return f"Open ports on {host}: {', '.join(map(str, open_ports))}"
        else:
            return f"No open ports found on {host}."
    
    except Exception as e:
        return f"Error scanning host {host}: {str(e)}"
