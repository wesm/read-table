from cStringIO import StringIO
import numpy as np

from numpy.testing import (assert_array_almost_equal,
                           assert_array_equal)

from nose.tools import assert_raises

class TestReadTable(unittest.TestCase):
    pass

def case1():
    example = """A B C D
foo 1 1.1111 "1 1"
bar 2 2.2222 "2 2"
baz 3 3.3333 "3 3"
quux 4 4.4444 "4 4"
"""
    row_labels = [0, 1, 2, 3]
    expected = np.array([('foo', 1, 1.1111, '1 1'),
                         ('bar', 1, 2.2222, '2 2'),
                         ('baz', 1, 3.3333, '3 3'),
                         ('quux', 1, 4.4444, '4 4')],
                        dtype=[('A', 'a4'), ('B', 'i'),
                               ('C', 'f'), ('D', 'a3')])

def case1_rowlabels():
    example = """A B C D
one foo 1 1.1111 "1 1"
two bar 2 2.2222 "2 2"
three baz 3 3.3333 "3 3"
four quux 4 4.4444 "4 4"
"""
    row_labels = ['one', 'two', 'three', 'four']
    expected = np.array([('foo', 1, 1.1111, '1 1'),
                         ('bar', 1, 2.2222, '2 2'),
                         ('baz', 1, 3.3333, '3 3'),
                         ('quux', 1, 4.4444, '4 4')],
                        dtype=[('A', 'a4'), ('B', 'i'),
                               ('C', 'f'), ('D', 'a3')])


if __name__ == '__main__':
    buf = StringIO(example)
    # gen = np.loadtxt(buf, names=True, dtype=None, delimiter=' ')
    gen = np.genfromtxt(buf, names=True, dtype=None, delimiter=' ')

