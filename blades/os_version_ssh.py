import paramiko

def check_vulnerability(host, username=None, password=None, key_file=None):
    if not username:
        print("Username is required for SSH-based checks.")
        return None

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        if key_file:
            ssh.connect(host, username=username, key_filename=key_file)
        else:
            ssh.connect(host, username=username, password=password)
        
        stdin, stdout, stderr = ssh.exec_command('uname -a')
        os_version = stdout.read().decode().strip()
        
        print(f"OS Version: {os_version}")
        ssh.close()
        return os_version
    except Exception as e:
        print(f"Error: {e}")
        return None
