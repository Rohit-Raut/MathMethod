# Some of the important information is used from the following git repo
# https://github.com/weijie-chen/Linear-Algebra-With-Python/blob/master/Chapter%203%20-%20Determinant.ipynb

#function ask user for the input-int for number of row/column [Square matrix]
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

#the function is designed to ask the user for individual elements of the matrix
def get_matrix_entries(dimension):
    matrix = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            while True:
                try:
                    entry = int(input(f"Enter the element A({i+1},{j+1}): "))
                    row.append(entry)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the matrix element.")
        matrix.append(row)
    print("Matrix:")
    for row in matrix:
        for element in row:
            print(f"{element:<5}", end="")
        print()
    return matrix

def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0
    for j in range(len(matrix)):
        sign = (-1) ** j
        cofactor = sign * matrix[0][j] * calculate_determinant(get_submatrix(matrix, 0, j))
        determinant += cofactor

    return determinant


def get_submatrix(matrix, row_to_exclude, col_to_exclude):
    submatrix = []
    for i in range(1, len(matrix)):
        row = []
        for j in range(len(matrix)):
            if i != row_to_exclude and j != col_to_exclude:
                row.append(matrix[i][j])
        if row:
            submatrix.append(row)
    return submatrix


def main():
    dimension = get_matrix_dimension()
    matrix = get_matrix_entries(dimension)
    determinant = calculate_determinant(matrix)
    print("The determinant of the matrix is:", determinant)


if __name__ == "__main__":
    main()
