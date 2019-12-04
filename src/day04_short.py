def main(low, high):
    num_codes_1, num_codes_2 = 0, 0
    for code in range(low, high+1):
        arr_code = [ int(i) for i in str(code)]
        if arr_code == sorted(arr_code):
            if any([ j > 1 for j in [arr_code.count(i) for i in range(10)]]):
                num_codes_1 += 1
            if any([ j == 2 for j in [arr_code.count(i) for i in range(10)]]):
                num_codes_2 += 1
    print("Number of codes matching first part: {}\nNumber of codes matching first part: {}"
          .format(num_codes_1, num_codes_2))

main(246540, 787419)