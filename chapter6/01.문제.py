
# 팔방향 델타 배열 생성
# 상, 우상, 우, ....
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 2) Boggle 보드판 데이터
MAP = [['u', 'r', 'l', 'p', 'm'],
       ['x', 'p', 'r', 'e', 't'],
       ['g', 'i', 'a', 'e', 't'],
       ['x', 't', 'n', 'z', 'y'],
       ['x', 'o', 'q', 'r', 's']]

MAX_COL_LEN = len(MAP[0])
MAX_ROW_LEN = len(MAP)

def dfs(row, col, target, MAP) :

    # 기저조건1 // 전체 MAP의 범위를 넘어서는 안된다.
    # 범위 항상 조심할것. 배열은 0 ~ N-1이라 최대범위 제한 할 때는 >=, <= 를 통해 범위 제한해야 함.
    if row < 0 or row >=  MAX_ROW_LEN or col < 0 or col >= MAX_COL_LEN :

        return False

    # 기저조건 2 // 현재 내가 보고 있는 단어와 내가 만들고 있는 단어의 첫번째를 비교
    # 항상 target[0]으로만 비교해도 되는 이유는 재귀를 반복하면서, target에 단어를 하나씩 미루면서 넣을 것

    if target[0] != MAP[row][col] :
        return False

    # 기저조건3 // 내가 찾는 단어가 완성 된 경우, 즉 마지막까지 다 온 경우라면
    if len(target) == 1:
        return True

    #재귀를 진행시키는 조건

    for dx in range(8) :

        next_row = row + dr[dx]
        next_col = col + dc[dx]

        if dfs(next_row, next_col, target[1:], MAP):
            return True

    #for문을 통해 모든 경우를 다 봐도, 찾고자 하는 단어가 없는 경우
    return False

for row in range(5):
    for col in range(5):

        if dfs(row, col, "pretty", MAP) :
            print("참")


