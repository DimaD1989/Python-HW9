from asyncore import write


def write_log(some_str):
    open('calculator_history.txt', 'a').write(some_str + '\n')