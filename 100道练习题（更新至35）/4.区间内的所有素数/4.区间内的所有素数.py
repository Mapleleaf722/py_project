# 素数：质数又称素数。
# 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数;否则称为合数。

# 判断一个数是否为素数
def is_prime(number):
    if number in (1,2):
        return True
    for i in range(2,number):
        if number%i==0:
            return False
    return True

# 输入开始数字和结束数字，打印闭区间内所有的素数
def print_primes(begin,end_):
    for number in range(begin,end_+1):
        if is_prime(number):
            print(f'{number} is a prime')

begin=11
end_=25
print_primes(begin,end_)