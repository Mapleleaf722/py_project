def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
    
print('3的阶乘=',factorial(3))
print('6的阶乘=',factorial(6))
print('100的阶乘=',factorial(100))