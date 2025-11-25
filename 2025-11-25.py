def __replace_3_5(n):
    ret = n
    if n % 3 == 0 :
        ret = 'Fizz'
    if n % 5 == 0:
        ret = 'Buzz'
    if n % (3 * 5) == 0 :
        ret = 'FizzBuzz'
    return ret

def fizz_buzz(n):
    return [__replace_3_5(i+1) for i in range(n)]
