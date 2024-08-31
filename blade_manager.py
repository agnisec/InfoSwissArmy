import os
import importlib

class BladeManager:
    def __init__(self, blades_dir='blades'):
        self.blades_dir = blades_dir
        self.blades = {}

    def load_blades(self):
        for filename in os.listdir(self.blades_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                blade_name = filename[:-3]  # Remove .py extension
                module_name = f'{self.blades_dir}.{blade_name}'
                module = importlib.import_module(module_name)
                self.blades[blade_name] = module

    def run_blade(self, blade_name, host, username=None, password=None, key_file=None):
        blade = self.blades.get(blade_name)
        if blade is None:
            print(f"Blade '{blade_name}' not found.")
            return None
        if hasattr(blade, 'check_vulnerability'):
            return blade.check_vulnerability(host, username, password, key_file)
        else:
            print(f"Blade '{blade_name}' does not have a 'check_vulnerability' function.")
            return None
