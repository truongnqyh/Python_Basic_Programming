# Create a function to calculate factorials
def cal_factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * cal_factorial(num - 1)

def print_result_factorial(num):
    result = cal_factorial(num)
    print(f"The factorial of {num} is {cal_factorial(num)}")

print_result_factorial(4)
