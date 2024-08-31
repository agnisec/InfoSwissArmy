from blade_manager import BladeManager
import sqlite3

class InfoSwissArmyScanner:
    def __init__(self, db_path='db/vuln_data.db'):
        self.blade_manager = BladeManager()
        self.blade_manager.load_blades()
        self.db_path = db_path

    def scan_device(self, host, username=None, password=None, key_file=None, blade_name=None):
        results = {}

        if blade_name:
            # Run only the specified blade
            result = self.blade_manager.run_blade(blade_name, host, username, password, key_file)
            if result is not None:
                results[blade_name] = result
        else:
            # Run all available blades
            for blade_name in self.blade_manager.blades.keys():
                result = self.blade_manager.run_blade(blade_name, host, username, password, key_file)
                if result is not None:
                    results[blade_name] = result

        self.save_results(host, results)
        return results

    def save_results(self, host, results):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS scan_results (
                            host TEXT, 
                            blade_name TEXT, 
                            result TEXT, 
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

        for blade_name, result in results.items():
            cursor.execute('INSERT INTO scan_results (host, blade_name, result) VALUES (?, ?, ?)',
                           (host, blade_name, result))
        
        conn.commit()
        conn.close()

    def get_results(self, host):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM scan_results WHERE host = ?', (host,))
        rows = cursor.fetchall()
        
        conn.close()
        return rows
