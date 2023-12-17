def msort(xs):
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        left = xs[:mid]
        right = xs[mid:]
        return merge(msort(left), msort(right))
    
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        # print("left: ", left[i], "right: ", right[j])
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
            
    while i < len(left):
        result.append(left[i])
        i = i + 1
        
    while j < len(right):
        result.append(right[j])
        j = j + 1
        
    return result

