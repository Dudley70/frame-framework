# FRAME Installer: Extend SuperClaude (Modular)
import os
import shutil
import json
import unittest

def load_configuration(config_path="config/features.json"):
    """Loads component configuration from the features.json file."""
    try:
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        # Extract components from the 'bmad' key, falling back to empty lists
        bmad_config = config_data.get("components", {}).get("bmad", {})
        agents = bmad_config.get("agents", [])
        tasks = bmad_config.get("tasks", [])
        workflows = bmad_config.get("workflows", ["fullstack.yaml"]) # Default workflow
        return agents, tasks, workflows
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"\033[91m✗ ERROR: Could not load or parse {config_path}: {e}\033[0m")
        return [], [], []

def install(target_dir=os.getcwd()):
    """Installs the FRAME components into the target directory."""
    print('\033[1mFRAME Installer (Modular)\033[0m')
    target_dir = os.path.abspath(target_dir)
    sources_dir = os.path.join(target_dir, 'sources')

    # --- Load Configuration ---
    bmad_agents, bmad_tasks, bmad_workflows = load_configuration()
    if not all((bmad_agents, bmad_tasks, bmad_workflows)):
        print("\033[91m✗ Halting installation due to configuration error.\033[0m")
        return

    # --- Step 1: Copy SuperClaude Core ---
    superclaude_core_src = os.path.join(sources_dir, 'superclaude/Core')
    target_core_dest = os.path.join(target_dir, 'Core')
    if os.path.exists(superclaude_core_src):
        shutil.copytree(superclaude_core_src, target_core_dest, dirs_exist_ok=True)
        print('\033[92m✓ Copied Core/\033[0m')
    else:
        print(f'\033[91m✗ ERROR: SuperClaude Core source not found at {superclaude_core_src}\033[0m')
        return

    # --- Step 2: Copy and Configure BMAD Agents ---
    bmad_agents_src = os.path.join(sources_dir, 'bmad/agents')
    target_agents_dest = os.path.join(target_dir, 'agents')
    os.makedirs(target_agents_dest, exist_ok=True)
    for agent in bmad_agents:
        src_path = os.path.join(bmad_agents_src, f'{agent}.md')
        dest_path = os.path.join(target_agents_dest, f'{agent}.md')
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
            with open(dest_path, 'r+') as f:
                content = f.read()
                if 'compatible_personas' not in content:
                    f.seek(0)
                    f.write('---\ncompatible_personas: [analyzer, security, refactorer]\n---\n' + content)
        else:
            print(f'\033[93m⚠ WARNING: Agent source file not found: {src_path}\033[0m')
    print('\033[92m✓ Integrated agents with hierarchy\033[0m')

    # --- Step 3: Copy BMAD Tasks and Workflows ---
    bmad_tasks_src = os.path.join(sources_dir, 'bmad/tasks')
    target_tasks_dest = os.path.join(target_dir, 'tasks')
    os.makedirs(target_tasks_dest, exist_ok=True)
    for task in bmad_tasks:
        src_path = os.path.join(bmad_tasks_src, f'{task}.md')
        dest_path = os.path.join(target_tasks_dest, f'{task}.md')
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
    print('\033[92m✓ Copied tasks/\033[0m')

    bmad_workflows_src = os.path.join(sources_dir, 'bmad/workflows')
    target_workflows_dest = os.path.join(target_dir, 'workflows')
    os.makedirs(target_workflows_dest, exist_ok=True)
    for workflow in bmad_workflows:
        src_path = os.path.join(bmad_workflows_src, workflow)
        dest_path = os.path.join(target_workflows_dest, workflow)
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
    print('\033[92m✓ Copied workflows/\033[0m')

    # --- Step 4: Create memory/ Directory ---
    memory_dir = os.path.join(target_dir, 'memory')
    os.makedirs(memory_dir, exist_ok=True)
    with open(os.path.join(memory_dir, 'session.log'), 'w') as f:
        f.write('# Session Log Template (YAML Structure)\ncycle: PAOA\nstatus: pending\ninsights: []\n')
    kb_src_path = os.path.join(sources_dir, 'bmad/data/bmad-kb.md')
    kb_dest_path = os.path.join(memory_dir, 'knowledge_base.md')
    if os.path.exists(kb_src_path):
        shutil.copy(kb_src_path, kb_dest_path)
    print('\033[92m✓ Setup memory/\033[0m')

    # --- Step 5: Setup Two-Tier Commands ---
    commands_dir = os.path.join(target_dir, '.claude/commands')
    os.makedirs(commands_dir, exist_ok=True)
    with open(os.path.join(commands_dir, 'frame-tool-git.md'), 'w') as f:
        f.write('# /frame-tool:git\n\n- Role: Atomic Tool\n- Purpose: Execute a quick git action.')
    with open(os.path.join(commands_dir, 'frame-flow-implement.md'), 'w') as f:
        f.write('# /frame-flow:implement\n\n- Role: Workflow Initiator\n- Purpose: Trigger a full PAOA cycle.')
    print('\033[92m✓ Setup two-tier commands\033[0m')

    print('\n\033[1mInstallation complete! Run tests with `python -m unittest`\033[0m')

if __name__ == '__main__':
    install()
