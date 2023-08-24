
def test_sum_result(calculate, make_number):
    print(calculate)  # выведет адрес функции к которой обращается
    print(calculate(1, 2))  # вызовет функцию и вернет результат
    print(make_number)
