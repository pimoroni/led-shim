import sys

import mock


def test_setup():
    sys.modules['smbus'] = mock.Mock()
    import ledshim
    ledshim.show()
