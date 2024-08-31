import sqlite3
import argparse

class DBManager:
    def __init__(self, db_path='db/vuln_data.db'):
        self.db_path = db_path

    def get_all_results(self, host):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM scan_results WHERE host = ?', (host,))
        rows = cursor.fetchall()
        
        conn.close()
        return rows

    def delete_host_entries(self, host):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM scan_results WHERE host = ?', (host,))
        conn.commit()
        
        conn.close()
        print(f"Deleted all entries for host: {host}")

    def delete_all_entries(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM scan_results')
        conn.commit()
        
        conn.close()
        print("Deleted all entries in the database")

def main():
    parser = argparse.ArgumentParser(description='Database Manager for IoT Device Vulnerability Scanner')
    parser.add_argument('host', nargs='?', help='Host name (optional, required for retrieving/deleting specific host entries)')
    parser.add_argument('--get', action='store_true', help='Get all results for a specific host')
    parser.add_argument('--delete-host', action='store_true', help='Delete all entries for a specific host')
    parser.add_argument('--delete-all', action='store_true', help='Delete all entries in the database')
    
    args = parser.parse_args()
    
    db_manager = DBManager()
    
    if args.get:
        if not args.host:
            print("Please provide a host name to retrieve results.")
        else:
            results = db_manager.get_all_results(args.host)
            for row in results:
                print(row)
    
    if args.delete_host:
        if not args.host:
            print("Please provide a host name to delete entries.")
        else:
            db_manager.delete_host_entries(args.host)
    
    if args.delete_all:
        db_manager.delete_all_entries()

if __name__ == '__main__':
    main()
