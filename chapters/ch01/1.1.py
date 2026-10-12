def fact(n):
    if n < 0:
        print('Factorial is defined only for non-negative integers')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result   
  
print(fact(int(input("Enter n:"))))