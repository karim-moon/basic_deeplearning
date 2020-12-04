def vector_size_check(*vector_variables):
    return all([len(ele) == len(vector_variables[0]) for ele in vector_variables[1:]])



def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables):
        return [sum(ele) for ele in zip(*vector_variables)]
    else:
        raise ArithmeticError



def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables):
        return [2*ele[0] - sum(ele) for ele in zip(*vector_variables)]
    else:
        raise ArithmeticError



def scalar_vector_product(alpha, vector_variable):
    return [alpha * ele for ele in vector_variable]


def matrix_size_check(*matrix_variables):
    row_len = len(matrix_variables[0])
    col_len = len(matrix_variables[0][0])

    return all([len(element) == row_len for element in matrix_variables[1:]]) and \
            all([len(element[0]) == col_len for element in matrix_variables[1:]])


def is_matrix_equal(*matrix_variables):
    ex_mat = matrix_variables[0]

    return all([element == ex_mat for element in matrix_variables])


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [vector_addition(*ele) for ele in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [vector_subtraction(*ele) for ele in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [[matrix_variable[i][j] for i in range(len(matrix_variable))] for j in range(len(matrix_variable[0]))]


def scalar_matrix_product(alpha, matrix_variable):
    if type(alpha) != int:
        raise AttributeError
    return [scalar_vector_product(alpha, ele) for ele in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a[0]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    matrix_b = matrix_transpose(matrix_b)
    return [[sum(x*y for x,y in zip(matrix_a[idx_a] , matrix_b[idx_b])) \
         for idx_b in range(len(matrix_b))] for idx_a in range(len(matrix_a))]