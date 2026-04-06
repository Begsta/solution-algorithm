def size_string(string: str) -> int:

    chars: dict[str, int] = dict()

    max_len: int = 0
    left: int = 0

    for idx, char in enumerate(string):
        if char in chars and chars[char] >= left:
            left = chars[char] + 1

        chars[char] = idx

        len_str: int = idx - left + 1

        if max_len < len_str:
            max_len = len_str
    return max_len


def min_int_in_matrix(matrix: list[list[int]], k: int) -> int:
    n: int = len(matrix)
    left: int = matrix[0][0]
    right: int = matrix[n - 1][n - 1]

    def find(target: int) -> int:
        row = n - 1
        col = 0
        count = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                col += 1
                count += row + 1
            else:
                row -= 1
        return count

    while left < right:
        mid: int = left + (right - left) // 2

        if find(mid) >= k:
            right = mid
        else:
            left = mid + 1
    return left


def main():
    print("Начало тестов")

    assert size_string("abcabcbb") == 3
    assert size_string("pwwkew") == 3

    assert size_string("") == 0
    assert size_string("a") == 1
    assert size_string("aaaaa") == 1
    assert size_string("abcdef") == 6

    assert size_string("abba") == 2
    assert size_string("tmmzuxt") == 5
    assert size_string("aab") == 2
    assert size_string("baa") == 2

    assert size_string(" ") == 1
    assert size_string("a b c a") == 3
    print("Тесты про стоку пройдены\nНачало тестов про матрицу")

    matrix1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]

    assert min_int_in_matrix(matrix1, 8) == 13
    assert min_int_in_matrix(matrix1, 4) == 10

    assert min_int_in_matrix(matrix1, 1) == 1
    assert min_int_in_matrix(matrix1, 9) == 15

    matrix2 = [[-5]]
    assert min_int_in_matrix(matrix2, 1) == -5

    matrix3 = [[1, 2], [1, 3]]

    assert min_int_in_matrix(matrix3, 1) == 1
    assert min_int_in_matrix(matrix3, 2) == 1
    assert min_int_in_matrix(matrix3, 3) == 2

    matrix4 = [[-5, -1, 2], [-4, 0, 3], [-2, 1, 4]]

    assert min_int_in_matrix(matrix4, 4) == -1
    assert min_int_in_matrix(matrix4, 5) == 0

    print("Все тесты пройдены")


if __name__ == "__main__":
    main()
