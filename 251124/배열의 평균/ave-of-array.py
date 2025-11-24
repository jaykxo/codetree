import sys
import statistics
input = sys.stdin.readline

# 2행 4열 입력
rows = [list(map(int, input().split())) for _ in range(2)]

# 1. 가로 평균
row_means = [statistics.mean(row) for row in rows]

# 2. 세로 평균 (전치)
cols = list(zip(*rows))
col_means = [statistics.mean(col) for col in cols]

# 3. 전체 평균
all_mean = statistics.mean([num for row in rows for num in row])

print(*[f"{m:.1f}" for m in row_means])
print(*[f"{m:.1f}" for m in col_means])
print(f"{all_mean:.1f}")
