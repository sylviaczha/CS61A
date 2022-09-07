def factors_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt_n:
        if divides(k, n):
            total += 2
        k += 1
    if k*k == n:
        
def count_frames(f):
    def counted(n):
        counted.open_count += 1 #increment the open frame count
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
            #keep track of the maximum number of open frames at any time
        result = f(n)
        counted.open_count -= 1 #close the frame
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted
