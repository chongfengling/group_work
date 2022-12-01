from utilities import *

def test_calculate_average():
    input = np.array([[1, 2], [3, 4]])
    output = np.array([2., 3.])
    assert np.allclose(calculate_average(input), output)