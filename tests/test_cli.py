"""Test CLI functionality"""

import pytest
from click.testing import CliRunner
from two_neurons.cli import main


class TestCLI:
    """Test CLI commands"""

    def test_init_command(self):
        """Test init command"""
        runner = CliRunner()
        result = runner.invoke(main, ["init"])
        assert result.exit_code == 0

    def test_status_command(self):
        """Test status command"""
        runner = CliRunner()
        result = runner.invoke(main, ["status"])
        assert result.exit_code == 0

    def test_config_command(self):
        """Test config command"""
        runner = CliRunner()
        result = runner.invoke(main, ["config", "show"])
        assert result.exit_code == 0

    def test_help_command(self):
        """Test help command"""
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
