import unittest
import os
import shutil

class TestFrameInstaller(unittest.TestCase):

    def setUp(self):
        """Set up a test directory to run the installer in."""
        self.test_dir = "test_installation_dir"
        os.makedirs(self.test_dir, exist_ok=True)
        # We need a dummy sources structure for the installer to run
        os.makedirs(os.path.join(self.test_dir, "sources/superclaude/Core"), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, "sources/bmad/agents"), exist_ok=True)
        with open(os.path.join(self.test_dir, "sources/bmad/agents/dev.md"), 'w') as f:
            f.write("# Dev Agent")

        # We need to import the installer script dynamically
        # This assumes installer.py is in a 'setup' directory at the root
        # and we are running tests from the root
        from setup.installer import install
        self.installer = install

    def tearDown(self):
        """Remove the test directory after tests."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_core_directory_created(self):
        """Test that the Core directory is created."""
        self.installer(self.test_dir)
        self.assertTrue(os.path.isdir(os.path.join(self.test_dir, "Core")))

    def test_agents_directory_created(self):
        """Test that the agents directory is created."""
        self.installer(self.test_dir)
        self.assertTrue(os.path.isdir(os.path.join(self.test_dir, "agents")))

    def test_memory_directory_created(self):
        """Test that the memory directory and its files are created."""
        self.installer(self.test_dir)
        memory_dir = os.path.join(self.test_dir, "memory")
        self.assertTrue(os.path.isdir(memory_dir))
        self.assertTrue(os.path.isfile(os.path.join(memory_dir, "session.log")))

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
    unittest.main()
