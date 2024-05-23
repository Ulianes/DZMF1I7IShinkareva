import numpy as np
# функция для чтение матрицы из файла
def read_matrix_from_file(Матрица):
    with open(Матрица, 'r') as file:
        lines = file.readlines()
        matrix = [list(map(int, line.split())) for line in lines]
    return np.array(matrix)

# вычисление суммы отрицательных элементов в векторе
def sum_negative_elements(vector):
    return sum(element for element in vector if element < 0)

# поиск строки с наименьшей суммой отрицательных элементов
def find_min_negative_sum_row(matrix):
    min_sum = float('inf')
    min_row_index = -1
    for i in range(matrix.shape[0]):
        row_sum = sum_negative_elements(matrix[i])
        if row_sum < min_sum:
            min_sum = row_sum
            min_row_index = i
    return min_row_index

# вывод элементов строки матрицы
def print_row(matrix, row_index):
    print("Элементы строки:", matrix[row_index])

# Основная программа
def main():
    Матрица = 'matrica.txt'
    matrix = read_matrix_from_file(Матрица)
    min_row_index = find_min_negative_sum_row(matrix)
    print_row(matrix, min_row_index)

if __name__ == "__main__":
    main()