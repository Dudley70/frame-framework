import glob
import json
import os

def generate_inventory():
    # Ensure we are in the script's directory to have correct relative paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    # Change to project root for glob operations
    original_cwd = os.getcwd()
    os.chdir(project_root)
    
    try:
        superclaude_files = glob.glob('sources/superclaude/**/*.md', recursive=True)
        bmad_files = glob.glob('sources/bmad/**/*.md', recursive=True) + glob.glob('sources/bmad/**/*.yaml', recursive=True)
        
        # Remove the sources/ prefix for cleaner paths
        superclaude_files = [f.replace('sources/superclaude/', '') for f in superclaude_files]
        bmad_files = [f.replace('sources/bmad/', '') for f in bmad_files]
        
        inventory_data = {
            'superclaude': sorted(superclaude_files),
            'bmad': sorted(bmad_files)
        }
        
        with open('inventory.json', 'w') as f:
            json.dump(inventory_data, f, indent=2)
        
        print("✅ Inventory generated successfully at inventory.json")
        
    finally:
        # Restore original working directory
        os.chdir(original_cwd)

if __name__ == '__main__':
    generate_inventory()
