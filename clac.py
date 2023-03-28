## 함수 선언부(=메소드)
def add_func(n1, n2) :
    retValue = n1 + n2
    return retValue

def sub_func(n1, n2) :
    return n1 - n2

## 전역 변수부
num1, num2, result = 100, 200, 0



## 메인 코드부
hap = add_func(num1, num2)
print(num1, '+', num2, '=', hap)

result = sub_func(num1, num2)
print(num1, '-', num2, '=', result)
