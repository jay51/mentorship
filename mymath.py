
# 2^8 2^7 2^6 2^5
# 128 64 32 16 8 4 2 1
#  0  0  0  0 1 0 1 0

def binary_to_int(bnum):

    idx = len(bnum) -1  # 8
    base = 0

    result = 0
    while idx >= 0:
        result += int(bnum[idx]) * (2**base)

        base += 1
        idx -= 1

    return result

    


def int_to_binary(bnum):
    pass



# print(int("0b00001010", 2))

print(binary_to_int('00001010')) # 10


print(int_to_binary(10)) # '00001010'