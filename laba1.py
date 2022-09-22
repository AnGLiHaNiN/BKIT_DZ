import sys
import math

def get_coef(index, prompt):

    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = ""
        while not isinstance(coef, float):
            try:
                coef = float(coef_str)
            except:
                print("Некорректный ввод данных!")
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
                print("Некорректный ввод данных!")
    # Переводим строку в действительное число
    return coef


def get_roots(a, b, c):

    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result

def get_roots_be(a, b, c):
    tmp=get_roots(a,b,c)
    r=[]
    for a in tmp:
        if a > 0:
            r.append(a**0.5)
            r.append(-(a**0.5))
        elif a == 0:
             r.append(0)
    return r   

def main():
 
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots_be(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

if __name__ == "__main__":
    main()
