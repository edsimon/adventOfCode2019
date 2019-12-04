low = 246540
high = 787419

def main(low, high):
    num_codes_1, num_codes_2 = 0, 0
    for code in range(low, high+1):
        arr_code = [ int(i) for i in str(code)]
        if arr_code == sorted(arr_code):
            if two_adjecent(arr_code):
                num_codes_1 += 1
            if new_two_adjecent(arr_code):
                num_codes_2 += 1
    return (num_codes_1, num_codes_2)

def two_adjecent(arr_code):
    for num in range(10):
        if arr_code.count(num) > 1 :
            return True
    return False

def new_two_adjecent(arr_code):
    for num in range(10):
        if arr_code.count(num) == 2 :
            return True
    return False

first, second = main(low, high)
print("Number of codes matching first part: {}\nNumber of codes matching first part: {}"
      .format(first, second))
