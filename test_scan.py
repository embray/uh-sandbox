assert scan([]) == 0
assert scan([1, 2, 3]) == 6
assert scan([2, 2, 3]) == 5
assert scan([1, 2, 3, 4]) == 10
assert scan([2, 2, 2]) == 2
assert scan([1, 2, 2, 3]) == 6
assert scan([1, 3, 5]) == 9
assert scan([1, 2, 3, 2]) == 0
assert scan([1, 2, 3, 2, 1]) == 1
assert scan([1, 2, 3, 5, 4, -1]) == -1
assert scan([-1, -2, -3]) == -3
assert scan([-3, -2, -1]) == -6
