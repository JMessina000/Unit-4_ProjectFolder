import time


def problem_1():
    Sum = 0
    x = 1
    while x < 1000:
        if x % 3 == 0 or x % 5 == 0:
            Sum = Sum + x
            x = x + 1
        else:
            x = x + 1
    return Sum

# print(problem_1())


def problem_2():
    n1 = 1
    n2 = 2
    Sum = 2
    while n1 <= 4000000 or n2 <= 4000000:
        nth = n1 + n2
        if nth % 2 == 0:
            Sum = Sum + nth
        n1 = n2
        n2 = nth
    return Sum

# print(problem_2())


def problem_3():
    num = 600851475143
    i = 2
    while i * i < num:
        while num % i == 0:
            num = num / i
        i = i + 1
    return num

# print(problem_3())


def problem_4():

    start = time.time()

    def isPalindrome(n):
        num = str(n)
        reverse_number = ''
        for k in num:
            reverse_number = k + reverse_number
        if reverse_number == num:
            return True
        return False

    largest_palindrome = 0

    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            num = i*j
            if num > largest_palindrome:
                if isPalindrome(num):
                    largest_palindrome = num

    print("Largest palindrome is: ")
    print(largest_palindrome)

    print("Code execution time: ")
    print(time.time()-start)

# problem_4()


def problem_5():

    start_time = time.time()

    def gcd(n1, n2):
        remainder = 1
        while remainder != 0:
            remainder = n1 % n2
            n1 = n2
            n2 = remainder
        return n1

    def lcm(n1, n2):
        return (n1*n2)/gcd(n1, n2)

    num = lcm(2, 3)

    for i in range(4, 21):
        num = lcm(num, i)

    print("Smallest divisible number: ", num)

    end_time = time.time()
    print("Code execution time: ", end_time - start_time)

# problem_5()


def problem_6():
    count = 0
    count2 = 0
    num = 0
    num2 = 0
    sum_of_squares = 0
    square_of_sums = 0

    while count < 100:
        count = count + 1
        num = num + 1
        sum_of_squares = sum_of_squares + (num ** 2)

    print("Sum of the squares: ", sum_of_squares)

    while count2 < 100:
        count2 = count2 + 1
        num2 = num2 + 1
        square_of_sums = square_of_sums + num2
    if count2 == 100:
        square_of_sums = square_of_sums ** 2

    print("Square of the sums: ", square_of_sums)

    print("Difference: ", square_of_sums - sum_of_squares)


# problem_6()

