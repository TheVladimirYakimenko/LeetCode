def mySqrt(x: int) -> int:
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        square_mid = mid ** 2

        if square_mid == x:
            return mid
        elif square_mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right


print(mySqrt(5))
