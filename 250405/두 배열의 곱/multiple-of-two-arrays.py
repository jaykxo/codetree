def read_matrix(rows):
    matrix = []
    while len(matrix) < rows:
        line = input().strip()
        if line:
            nums = list(map(int, line.split()))
            if len(nums) == 3:
                matrix.append(nums)
            else:
                raise ValueError("각 행에는 정확히 3개의 숫자가 있어야 합니다.")
    return matrix

# 첫 번째 3x3 행렬 입력 받기
matrix1 = read_matrix(3)

# 두 번째 3x3 행렬 입력 받기
matrix2 = read_matrix(3)

# 두 행렬의 원소별 곱 출력
for i in range(3):
    for j in range(3):
        print(matrix1[i][j] * matrix2[i][j], end=' ')
    print()