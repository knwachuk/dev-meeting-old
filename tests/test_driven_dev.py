import pytest
from savia import math


class TestMathModule:

    def test_inc(self):
        assert math.inc(3) == 4

    def test_dec(self):
        assert math.dec(4) == 3
        with pytest.raises(TypeError):
            math.dec('h')
            math.dec(True)
