import argparse
from scanner import InfoSwissArmyScanner

def main():
    parser = argparse.ArgumentParser(description='InfoSwissArmy Vulnerability Scanner')
    parser.add_argument('host', help='IP address of the IoT device')
    parser.add_argument('--username', help='SSH username (optional)')
    parser.add_argument('--password', help='SSH password (optional)')
    parser.add_argument('--key-file', help='SSH private key file (optional)')
    parser.add_argument('--blade', help='Blade to run (default: run all blades)', default=None)
    
    args = parser.parse_args()

    scanner = InfoSwissArmyScanner()
    
    # Pass the optional blade argument to the scanner
    results = scanner.scan_device(
        host=args.host, 
        username=args.username, 
        password=args.password, 
        key_file=args.key_file, 
        blade_name=args.blade
    )
    
    for blade, result in results.items():
        print(f"[{blade}] Scan result: {result}")

if __name__ == '__main__':
    main()
