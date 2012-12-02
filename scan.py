def scan(items):
    if items == []:
        return 0
    total = 0
    previous = 'unseen'
    for item in items:
        if previous == 'unseen' or item > previous:
            total -= item
            previous = item
        elif item < previous:
            total = 0
            previous = 'unseen'

    return total
