from mikesone.lib import try_me
import matplotlib

def test_try_me():
    assert type(try_me()) == matplotlib.figure.Figure