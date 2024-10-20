#게임판 덮기

'''

input

3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########

output

0
2
1514

'''

TC = int(input())

#(0,0)이 되는 블록을 기준으로 놓을 수 있는 경우의 수 4가지
BlockType = [[(0,0), (0,1), (1,1)],
             [(0,0), (1,0), (1,1)],
             [(0,0), (0,1), (1,0)],
             [(0,0), (1,0), (1,-1)]]

#print(BlockType)

def sol():
    now_row, now_col = -1, -1
    # 맨위, 맨 왼쪽부터 블록 찾기
    for i in range(H):
        for j in range(W):
            if (MAP[i][j] == "."):
                now_row = i
                now_col = j
                break
        if now_col != -1:
            break
    #모든 칸을 채운 경우 1을 반환(가짓수)
    if now_row == -1 and now_col == -1:
        return 1

    cnt = 0
    debug = 1
    for block in BlockType:
        flag = True
        for dr, dc in block:
            next_row = now_row + dr
            next_col = now_col + dc
            #1) 경기장 밖인경우 false
            if next_row < 0 or next_row >= H or next_col < 0 or next_col >= W:
                flag = False
                break
            #2) 검은색 블록
            elif MAP[next_row][next_col] == '#':
                flag = False
                break
            #3) 겹치지 않는 것은, "특정 순서"를 정하도록 되어있는 아래 가정들을 통해 해결
            # 3-1) now_row / now_col 찾기
            # 3-2) 4가지 경우의 수

        #예외 조건을 제외하고, 실제 이동 및 블록 처리(색칠 및 복구)(백트래킹)
        if flag:
            for dr, dc in block:
                next_row = now_row + dr
                next_col = now_col + dc
                MAP[next_row][next_col] = '#'
            cnt += sol()
            for dr, dc in block:
                next_row = now_row + dr
                next_col = now_col + dc
                MAP[next_row][next_col] = '.'

    return cnt

for _ in range(TC):
    #입력인자 받기 연습 필요
    H, W = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    print(sol())




