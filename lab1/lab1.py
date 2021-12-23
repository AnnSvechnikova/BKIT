import sys
import math

def get_coef_kb():
    '''ввод коэффициента с клавиатуры'''
    while(True):
            coef_str = input()
            try:
                # Переводим строку в действительное число
                coef = float(coef_str)
            except:
                print('коэффициент введен неверно, попробуйте ещё раз')
            else: 
                return coef


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
        coef = float(coef_str)
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef = get_coef_kb()
    finally:
        return coef
        

def discr(a, b, c):
    return b*b - 4*a*c

def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = set() #храним корни в множестве, чтобы не было повторяющихся
    D = discr(a, b, c)
    if D < 0:
        #нет корней
        return set()
    else:
        root = math.sqrt(D)
        try:
            res1 = (-b + root)/(2*a)
            res2 = (-b - root)/(2*a)
        except ArithmeticError: 
            #возможно, имеет место квадратное уравнение bx^2 + c = 0
            try:
                res1 = math.sqrt(-c/b)
                result.add(-res1)
                result.add(res1)
            except ArithmeticError:
                # нет корней
                return set()
        if(res1 >= 0):
            result.add(-math.sqrt(res1))
            result.add(math.sqrt(res1))        
        if(res2 >= 0):
            result.add(-math.sqrt(res2))  
            result.add(math.sqrt(res2))
        return result      
            

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = list(get_roots(a,b,c))
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
    
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# lab1.py 1 0 -4
