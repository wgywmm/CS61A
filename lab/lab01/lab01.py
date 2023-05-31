def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1
    for i in range(k):
        result *= n
        n -= 1
    return result

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    total = 0
    while y > 0:
        digit = y % 10  # 获取最右边的数字
        total += digit  # 将该数字加到总和中
        y //= 10  # 将 y 右移一位
    return total

    # 将整数转换为字符串，并遍历字符串中的每一个字符
    # 将字符转换为对应的数字，并求和
    return sum(int(digit) for digit in str(y))


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # 将整数转换为字符串
    num_str = str(n)
    
    # 遍历字符串中的每个数字
    for i in range(len(num_str) - 1):
        # 如果当前数字和下一个数字都是 8，则返回 True
        if num_str[i] == '8' and num_str[i+1] == '8':
            return True
    
    # 如果没有找到连续的两个数字 8，则返回 False
    return False
