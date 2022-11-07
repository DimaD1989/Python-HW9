def complex_operation(a, b, operator):
    c_a = complex(a)    # complex_a
    c_b = complex(b)    # complex_b
    return c_a+c_b if operator == '+' else c_a-c_b if operator == '-' \
        else c_a*c_b if operator == '*' else c_a/c_b if operator == '/' else False

# print(complex_operation('1+2j', '3-1j', '-'))