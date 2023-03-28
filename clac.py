## 함수 선언부(=메소드)
def add_func(n1, n2) :
    retValue = n1 + n2
    return retValue

def sub_func(n1, n2) :
    return n1 - n2

def mult_func(n1, n2) :
    return n1 * n2

def div_func(n1, n2) :
    return n1 / n2

def sqr_func(n1) :
    return n1 * n1

## 전역 변수부
num1, num2, result = 100, 200, 0



## 메인 코드부
hap = add_func(num1, num2)
print(num1, '+', num2, '=', hap)

result = sub_func(num1, num2)
print(num1, '-', num2, '=', result)

result2 = mult_func(num1, num2)
print(num1, '*', num2, '=', result2)

result3 = div_func(num1, num2)
print(num1, '/', num2, '=', result3)

result4 = sqr_func(num1)
print(num1, '**', num1, '=', result4)
