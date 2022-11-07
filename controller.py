import complex_numbers
import rational_numbers
import inputs
import logger


def operation(a=0, b=0, t=0):
    t = inputs.type_input()
    if t == 0:
        print('Введено неверно, попробуйте ещё раз.\n')
        return operation()
    tp = 'рациональными' if t == 1 else 'комплексными'
    print(f'Работаем с {tp} числами.')
    a = inputs.number_input(0)
    b = inputs.number_input(1)
    return a, b, t
