'''
완전 탐색(brute force)
'''

# 6.1 1부터 n까지의 합을 계산하는 반복함수와 재귀 함수

# 반복문
def sumFor(n : int) :

    ret = 0

    for i in range(1, n + 1):
        ret += i

    return ret
# 재귀함수
def sumRecursive(n : int) :

    if (n == 1) :
        return 1
    # 더 이상 쪼개지지 않는 최소한의 작업을 항상 명시 해야 힘.
    '''
    1. 재귀를 종료 시키는 코드 (base case)
    2. 재귀를 진행시키는 코드 ( 
    '''
    return n + sumRecursive(n-1)

print(sumFor(10))
print(sumRecursive(10))

# 6.2 n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘
def pick(n, picked, toPick):
    if toPick == 0:
        print_picked(picked)
        return

    smallest = picked[-1] + 1 if picked else 0

    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, toPick - 1)
        picked.pop()


def print_picked(picked):
    print(picked)

print(pick(4, [], 2))

# python 코드
combinations = []
elements = [1,2,3,4,5]
m = 2

def backtrack(start, path):
    if len(path) == m:
        combinations.append(path[:])
        return

    for i in range(start, len(elements)):
        path.append(elements[i])
        backtrack(i + 1, path)
        path.pop()

    return combinations

print(backtrack(0, []))

# 예제 보금게임
# 데이터 영역
# 1) 상하좌우/대각선 이동 데이터
dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

# 2) Boggle 보드판 데이터
b = [['u', 'r', 'l', 'p', 'm'],
     ['x', 'p', 'r', 'e', 't'],
     ['g', 'i', 'a', 'e', 't'],
     ['x', 't', 'n', 'z', 'y'],
     ['x', 'o', 'q', 'r', 's']]


# 알고리즘 영역
def hasWord(x, y, word, board):

    # 조건 영역(base case)
    # 1) 좌표는 Boggle 판을 넘어서면 안 된다.
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return False
    # 2) 좌표의 첫단어와 내가 만들고 있는 단어의 첫단어가 부합하지 않으면 재귀호출 시퀀스를 종료시킨다.
    elif board[x][y] != word[0]:
        return False
    # 3) 1),2) 조건을 통과하고 이번 재귀호출이 마지막 단어탐색이라면 True를 반환하여 재귀호출 시퀀스를 종료시킨다.
    elif len(word) == 1:
        return True

    # 상하좌우/대각선 모든 경우를 이동(완전탐색)해야하므로 반복문을 사용
    # 8방향이라 델타 배열을 통해 반복문 쓴거고(방향성 있는 증가), 위에선 숫자를 한개씩 증가시키기 위해(선형증가) i 값을 증가만 시키면 되었다.
    # 위의 n개에세 m개를 구하는 코드의 구조와 해당 알고리즘의 코드구조는 같다.
    '''
    1. 기저 구조
    2. 재귀를 반복시키는 구문
    '''
    for di in range(8):
        nx = x + dx[di]
        ny = y + dy[di]

        # 재귀호출
        if hasWord(nx, ny, word[1:], board):  # True를 Return하면 True를 반환하여 재귀호출 시퀀스를 종료시킨다.
                                              # 첫 번쨰 글자의 경우엔, 이미 위의 base 조건 2번에서 확인하고 있으니 굳이 검사 항목(word)에
                                              # 넣지 않아도 된다.

            return True

    return False  # for문을 모두 돌았는데도 True가 반환되지 못하면 False를 반환하여 재귀호출 시퀀스를 종료시킨다.

# Boggle 보드판 첫 이동 : 완전탐색 ( 반복문 )
for i in range(5):
    for j in range(5):
        if hasWord(i, j, "pretty", b):  # 재귀호출의 시퀀스의 Return이 True이면 pretty 단어 탐색 성공, COMPLETE 출력!
            print("COMPLETE")
