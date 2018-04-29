
import py
from toolplus_curve.inserts.add_curve_braid import braid


def test_braid():
    h = braid.circle_humps(3, 3)
    assert len(h) == 3


def test_braid2():
    h = braid.circle_humps(3, 5)
    assert len(h) == 1
