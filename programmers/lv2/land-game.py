# https://programmers.co.kr/learn/courses/30/lessons/12913

# DP
def solution(land):
    for i in range(len(land) - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])
        # for j in range(4):
        #     land[i + 1][j] += max(land[i][:j], land[i][j + 1 :])
    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
