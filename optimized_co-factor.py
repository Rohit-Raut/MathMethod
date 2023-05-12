import numpy as np

def get_matrix_dimension():
    while True:
        try:
            dimension = int(input("Enter the number of rows/columns for the square matrix: "))
            if dimension <= 0:
                print("Please enter a positive integer for the matrix dimension.")
            else:
                return dimension
        except ValueError:
            print("Invalid input. Please enter a positive integer for the matrix dimension.")


def get_matrix_entries(dimension):
    matrix = np.zeros((dimension, dimension), dtype=int)
    for i in range(dimension):
        for j in range(dimension):
            while True:
                try:
                    entry = int(input(f"Enter the element A({i+1},{j+1}): "))
                    matrix[i, j] = entry
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the matrix element.")
    return matrix


def find_max_zero_row_column(matrix):
    max_zeros = 0
    max_zeros_index = -1
    max_zeros_type = None

    for i in range(len(matrix)):
        zeros_in_row = np.count_nonzero(matrix[i] == 0)
        if zeros_in_row > max_zeros:
            max_zeros = zeros_in_row
            max_zeros_index = i
            max_zeros_type = "row"

    for i in range(len(matrix[0])):
        zeros_in_column = np.count_nonzero(matrix[:, i] == 0)
        if zeros_in_column > max_zeros:
            max_zeros = zeros_in_column
            max_zeros_index = i
            max_zeros_type = "column"

    return max_zeros_index, max_zeros_type


def calculate_determinant(matrix):
    if matrix.shape[0] == 1:
        return matrix[0, 0]

    max_zeros_index, max_zeros_type = find_max_zero_row_column(matrix)
    determinant = 0

    if max_zeros_type == "row":
        for j in range(matrix.shape[0]):
            if matrix[max_zeros_index, j] == 0:
                continue
            sign = (-1) ** (max_zeros_index + j)
            print(matrix)
            submatrix = get_submatrix(matrix, max_zeros_index, j)
            cofactor = sign * calculate_determinant(submatrix)
            determinant += matrix[max_zeros_index, j] * cofactor
        print(f"The determinant is calculated using row {max_zeros_index + 1}.")

    elif max_zeros_type == "column":
        for i in range(matrix.shape[0]):
            if matrix[i, max_zeros_index] == 0:
                continue
            sign = (-1) ** (i + max_zeros_index)
            submatrix = get_submatrix(matrix, i, max_zeros_index)
            cofactor = sign * calculate_determinant(submatrix)
            determinant += matrix[i, max_zeros_index] * cofactor
        print(f"The determinant is calculated using column {max_zeros_index + 1}.")

    return determinant


def get_submatrix(matrix, row_to_exclude, col_to_exclude):
    submatrix = np.delete(np.delete(matrix, row_to_exclude, axis=0), col_to_exclude, axis=1)
    return submatrix


def main():
    dimension = get_matrix_dimension()
    matrix = get_matrix_entries(dimension)
    determinant = calculate_determinant(matrix)
    print("The determinant of the matrix is:", determinant)


if __name__ == "__main__":
    main()













