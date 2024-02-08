import sys

import mock


def test_setup():
    sys.modules["smbus2"] = mock.Mock()

    import ledshim
    ledshim.show()
