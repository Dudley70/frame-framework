# FRAME Installer: Extend SuperClaude
import os
import shutil
import json
import unittest

# --- Configuration ---
# This configuration will eventually be moved to a separate config file
# For now, it's defined here for clarity.
BMAD_AGENTS = ['analyst', 'dev', 'qa', 'sm']
BMAD_TASKS = ['create-story', 'advanced-elicitation']
BMAD_WORKFLOWS = ['fullstack.yaml']


def install(target_dir=os.getcwd()):
    """Installs the FRAME components into the target directory."""
    print('\033[1mFRAME Installer\033[0m')
    target_dir = os.path.abspath(target_dir)
    sources_dir = os.path.join(target_dir, 'sources')

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
    for agent in BMAD_AGENTS:
        src_path = os.path.join(bmad_agents_src, f'{agent}.md')
        dest_path = os.path.join(target_agents_dest, f'{agent}.md')
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
            # Add hierarchy YAML frontmatter
            with open(dest_path, 'r+') as f:
                content = f.read()
                f.seek(0)
                f.write('---\ncompatible_personas: [analyzer, security, refactorer]\n---\n' + content)
        else:
            print(f'\033[93m⚠ WARNING: Agent source file not found: {src_path}\033[0m')
    print('\033[92m✓ Integrated agents with hierarchy\033[0m')

    # --- Step 3: Copy BMAD Tasks and Workflows (Abbreviated) ---
    # Copy tasks
    bmad_tasks_src = os.path.join(sources_dir, 'bmad/tasks')
    target_tasks_dest = os.path.join(target_dir, 'tasks')
    os.makedirs(target_tasks_dest, exist_ok=True)
    for task in BMAD_TASKS:
        src_path = os.path.join(bmad_tasks_src, f'{task}.md')
        dest_path = os.path.join(target_tasks_dest, f'{task}.md')
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
    print('\033[92m✓ Copied tasks/\033[0m')

    # Copy workflows
    bmad_workflows_src = os.path.join(sources_dir, 'bmad/workflows')
    target_workflows_dest = os.path.join(target_dir, 'workflows')
    os.makedirs(target_workflows_dest, exist_ok=True)
    for workflow in BMAD_WORKFLOWS:
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
    # Atomic tool example
    with open(os.path.join(commands_dir, 'frame-tool-git.md'), 'w') as f:
        f.write('# /frame-tool:git\n\n- Role: Atomic Tool\n- Purpose: Execute a quick git action (SuperClaude-inspired). Example: /frame-tool:git status')
    # Workflow initiator example
    with open(os.path.join(commands_dir, 'frame-flow-implement.md'), 'w') as f:
        f.write('# /frame-flow:implement\n\n- Role: Workflow Initiator\n- Purpose: Trigger a full PAOA cycle. Dev agent codes, QA agent loops for tests, and reflection updates the knowledge base.')
    print('\033[92m✓ Setup two-tier commands\033[0m')

    print('\n\033[1mInstallation complete! Run tests with `python -m unittest`\033[0m')


if __name__ == '__main__':
    install()
