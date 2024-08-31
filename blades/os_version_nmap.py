import nmap

def check_vulnerability(host, *args, **kwargs):
    try:
        nm = nmap.PortScanner()
        scan_result = nm.scan(hosts=host, arguments='-O')  # '-O' enables OS detection

        os_info = scan_result['scan'].get(host, {}).get('osmatch', [])
        
        if os_info:
            # Just taking the first match; in real scenarios, more detailed analysis might be needed
            os_name = os_info[0].get('name')
            accuracy = os_info[0].get('accuracy')
            print(f"OS Detected: {os_name} (Accuracy: {accuracy}%)")
            return os_name
        else:
            print(f"No OS information found for {host}.")
            return None

    except Exception as e:
        print(f"Error while scanning {host} with nmap: {e}")
        return None
