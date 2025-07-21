import unittest
import os
import shutil
import json

class TestFrameInstaller(unittest.TestCase):

    def setUp(self):
        """Set up a test directory and dummy sources for the installer."""
        self.test_dir = "test_installation_dir"
        # Clean up any previous runs
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create dummy sources and config that the installer needs to run
        self.sources_dir = os.path.join(self.test_dir, "sources")
        os.makedirs(os.path.join(self.sources_dir, "superclaude/Core"), exist_ok=True)
        os.makedirs(os.path.join(self.sources_dir, "bmad/agents"), exist_ok=True)
        os.makedirs(os.path.join(self.sources_dir, "bmad/data"), exist_ok=True)
        
        with open(os.path.join(self.sources_dir, "bmad/agents/dev.md"), 'w') as f:
            f.write("# Dev Agent")
        with open(os.path.join(self.sources_dir, "bmad/data/bmad-kb.md"), 'w') as f:
            f.write("# Knowledge Base")

        # Create dummy config/features.json for the modular installer test
        self.config_dir = os.path.join(self.test_dir, "config")
        os.makedirs(self.config_dir, exist_ok=True)
        features = {
            "components": {
                "bmad": { "agents": ["dev"], "tasks": [], "workflows": [] }
            }
        }
        with open(os.path.join(self.config_dir, "features.json"), 'w') as f:
            json.dump(features, f)

        # We need to import the installer script dynamically
        from setup.installer import install
        self.installer = install

    def tearDown(self):
        """Remove the test directory after tests."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_installer_reads_from_config(self):
        """Test that the installer correctly reads agents from features.json."""
        self.installer(self.test_dir)
        # The installer should create 'agents/dev.md' because it's in our dummy config
        agent_file_path = os.path.join(self.test_dir, "agents/dev.md")
        self.assertTrue(os.path.isfile(agent_file_path), "Installer did not create agent file based on config.")

    def test_memory_directory_created(self):
        """Test that the memory directory and its files are created."""
        self.installer(self.test_dir)
        memory_dir = os.path.join(self.test_dir, "memory")
        self.assertTrue(os.path.isdir(memory_dir))
        self.assertTrue(os.path.isfile(os.path.join(memory_dir, "session.log")))
        self.assertTrue(os.path.isfile(os.path.join(memory_dir, "knowledge_base.md")))

    def test_commands_directory_created(self):
        """Test that the two-tier commands are created."""
        self.installer(self.test_dir)
        commands_dir = os.path.join(self.test_dir, ".claude/commands")
        self.assertTrue(os.path.isdir(commands_dir))
        self.assertTrue(os.path.isfile(os.path.join(commands_dir, "frame-tool-git.md")))
        self.assertTrue(os.path.isfile(os.path.join(commands_dir, "frame-flow-implement.md")))

    def test_agent_file_has_persona_frontmatter(self):
        """Test that the installer adds the compatible_personas YAML frontmatter."""
        self.installer(self.test_dir)
        agent_file_path = os.path.join(self.test_dir, "agents/dev.md")
        self.assertTrue(os.path.isfile(agent_file_path))
        with open(agent_file_path, 'r') as f:
            content = f.read()
            self.assertIn("compatible_personas:", content)

if __name__ == '__main__':
    # This allows running the test script directly
    # We need to be in the project root for imports to work
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    os.chdir(project_root)
    # Add setup to the path to allow import
    import sys
    sys.path.insert(0, os.path.join(project_root, 'setup'))
    unittest.main()
