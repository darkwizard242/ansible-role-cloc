import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


CLOC_APP = "cloc"
CLOC_BINARY_FILE = "/usr/bin/cloc"


def test_cloc_package_installed(host):
    """
    Tests if cloc package is in installed state.
    """
    assert host.package(CLOC_APP).is_installed


def test_cloc_binary_exists(host):
    """
    Tests if cloc binary exists.
    """
    assert host.file(CLOC_BINARY_FILE).exists


def test_cloc_binary_file(host):
    """
    Tests if cloc binary is a file type.
    """
    assert host.file(CLOC_BINARY_FILE).is_file


def test_cloc_binary_which(host):
    """
    Tests the output to confirm cloc's binary location.
    """
    assert host.check_output('which cloc') == CLOC_BINARY_FILE
