# Ajay Bhatia
# BinarySearchR
# Binary search algorithm recursive version

def search(ll, lo, hi, target):
    # if low is ever greater than or equal to high, then the value is not in the list
    if lo >= hi:
        return -1

    # find the mid point of the list
    mid = lo+(hi-lo)//2

    # check if the value in the middle of the list is greater than or less than the target
    # if smaller, shrink the list and research
    if ll[mid] < target:
        return search(ll, mid+1, hi, target)
    # if larger, shrink the list and research
    elif ll[mid] > target:
        return search(ll, lo, mid, target)
    # if the target is found, return the index at which it exists
    else:
        return mid

if __name__ == "__main__":
    ll = [1, 3, 6, 8, 10, 18, 22, 24, 37, 60, 93]
    search(ll, 0, len(ll), 22)
