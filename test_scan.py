from scan import scan

def test_scan_empty_list():
    assert scan([]) == 0

def test_scan_consecutive():
    assert scan([1, 2, 3]) == 6

def test_1():
    assert scan([2, 2, 3]) == 5

def test_2():
    assert scan([1, 2, 3, 4]) == 10

def test_3():
    assert scan([2, 2, 2]) == 2

def test_4():
    assert scan([1, 2, 2, 3]) == 6

def test_5():
    assert scan([1, 3, 5]) == 9

def test_6():
    assert scan([1, 2, 3, 2]) == 0

def test_7():
    assert scan([1, 2, 3, 2, 1]) == 1

def test_8():
    assert scan([1, 2, 3, 5, 4, -1]) == -1

def test_9():
    assert scan([-1, -2, -3]) == -3

def test_10():
    assert scan([-3, -2, -1]) == -6
