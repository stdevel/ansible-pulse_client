"""
Role unit tests
"""


def test_packages(host):
    """
    Ensure that packages are installed
    """
    pkgs = [
        'pulsesecure'
    ]
    for _pkg in pkgs:
        assert host.package(_pkg).is_installed


def test_cef(host):
    """
    Ensure that Chrome Embedded Browser is installed
    """
    _ceb = host.file("/opt/pulsesecure/lib/cefRuntime/Resources/libcef.so")
    assert _ceb.exists
