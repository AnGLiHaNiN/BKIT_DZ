import sys
import math
import random

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = ""
        while not isinstance(coef, float):
            try:
                coef = float(coef_str)
            except:
                print("Некорректный ввод данных! Введите заново!")
                coef = float(coef_str)
    except:
        # Вводим с клавиатуры
        coef_str = ""
        coef = ""
        while not isinstance(coef, float):
            try:
                print(prompt)
                coef_str = input()
                coef = float(coef_str)
            except:
                print("Некорректный ввод данных! Введите заново!")
    # Переводим строку в действительное число
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        if ((-b / (2.0*a)) >= 0):
            root1 = math.sqrt(-b / (2.0*a))
            root2 = -root1;
            if root1==0:
                result.append(root1)
            else:
                result.append(root1)
                result.append(root2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        if (((-b + sqD) / (2.0*a)) >= 0):
            root1 = math.sqrt((-b + sqD) / (2.0*a))
            root2 = -root1
            if root1==0:
                result.append(root1)
            else:
                result.append(root1)
                result.append(root2)
        if (((-b - sqD) / (2.0*a)) >= 0):
            root3 = math.sqrt((-b - sqD) / (2.0*a))
            root4 = -root3
            if root3==0:
                result.append(root3)
            else:
                result.append(root3)
                result.append(root4)
        
    return result

def sort_with_lambda(lst):
    return sorted(lst, key=lambda x: abs(x), reverse=True)

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

def main():
    
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} , {} , {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# lab1.py 1 -5 6
