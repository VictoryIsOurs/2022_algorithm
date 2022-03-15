import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#가장자리 처리 조건을 간소화하기 위해 보드 감싸기 #'c'는 checked
board = [['c']*(n+2)] + [['c'] + list(input())[:-1] +['c'] for _ in range(m)] + [['c']*(n+2)]

cnt = 0
force = {'B': 0, 'W': 0} #정답을 저장할 set
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상하좌우 방향
def dfs(r, c, type): #dfs
    global cnt
    cnt += 1
    for d in dir:
        if board[r+d[0]][c+d[1]] == type:  #상하좌우에 같은 병사가 있음
            board[r+d[0]][c+d[1]] = 'c'
            dfs(r+d[0], c+d[1], type)

for r in range(1, m+1):
    for c in range(1, n+1):
        if board[r][c] != 'c': #확인하지 않은 병사가 있음
            cnt = 0
            type = board[r][c]
            board[r][c] = 'c'
            dfs(r, c, type)
            force[type] += cnt**2

print(str(force['W']) + " " + str(force['B']))
