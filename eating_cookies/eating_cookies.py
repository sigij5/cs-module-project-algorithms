'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     if n == 0:
#         return 1  # test wanted this to equal zero?
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
    
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n, mem={}):
    if n == 0:
        return 1
    if n < 3:
        return n
    elif mem[n] > 0:  
        return mem[n]  
    else:
        mem[n] = eating_cookies(n-1, mem) + eating_cookies(n-2, mem) + eating_cookies(n-3, mem)
        return mem[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
