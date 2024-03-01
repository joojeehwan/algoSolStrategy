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
        backtrack(i + 1, path)  # i + 1이 이 코드의 핵심
        path.pop()

    return combinations

print(backtrack(0, []))

