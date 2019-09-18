def reversedSumOfDigits(p, n):
    if n == 1:
        return str(p) if p <= 9 else "-1"
    start = int("1" + "0"* (n-1))
    
    arr = list(str(start))
    if p == 1:
        return ''.join(arr)
    
    index = len(arr) - 1
    flag = False
    curr = 0
    while curr < p and index >= 0:
        if p - curr >= 10:
            arr[index] = '9'
            curr += 9
        else:
            tmp = str(p - curr)
            if index != 0:
                tmp = str(p - curr - int(arr[0]))
            arr[index] = tmp
            flag = True
            break
        index -= 1
    
    if flag == True:
        return ''.join(arr)
    return "-1"
