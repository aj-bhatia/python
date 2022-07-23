# Ajay Bhatia
# BinarySearchI
# Binary search algorithm iterative version\

if __name__ == "__main__":
	ll = [1, 3, 5, 7, 12, 15, 16, 20, 23, 27, 35, 46, 70]
    target = 35

    lo = 0
    hi = len(ll)-1
    while lo <= hi:
        mid = lo+(hi-lo)//2:
        if ll[mid] > target:
            hi = mid-1
        elif ll[mid] < target:
            lo = mid+1
        else:
            return mid
    return -1
