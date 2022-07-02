# 1. 테스트 14 런타임 에러. 

def solution(lottos, win_nums):
    
    correctNumCount = 0 
    
    #당첨번호 체크
    for num in win_nums : 
        if num in lottos : 
            correctNumCount += 1
            
    # 0 카운트
    zeroCount = lottos.count(0)

    winList = [6, 5, 4, 3, 2 ]
    rankList = []
    
    #최저 순위 계산
    for i in range(0, len(winList)) : 
        if correctNumCount == winList[i] : 
                rankList.append(i+1)

    #순위가 낙첨인 경우
    if len(rankList) == 0 :
        rankList.append(6)
    
    #최고 순위 계산
    for i in range(0, len(winList)) : 
        if correctNumCount + zeroCount == winList[i] : 
            rankList.append(i+1)
    
    #최고 순위가 안들어간 경우
    if len(winList) == 1 :
        rankList.append(winList[0])
            
        
    return rankList[1], rankList[0]  #list로 반환됨.
    
    
# 220628 다음날 코드 수정
def solution(lottos, win_nums):
    
    rank = [6,6,5,4,3,2,1] #맞은게 하나도 없을 경우에도 6순위이므로 index=0에 6을 넣어줘야 함.
    correctCount = 0 
    zeroCount = lottos.count(0) #count 0 in List lottos
    
    for i in win_nums : 
        if i in lottos : 
            correctCount += 1
    
    return rank[correctCount + zeroCount] ,  rank[correctCount]
    
            
    
    
    
# -------------------------------------------
# 간단한 코드 

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
            
#     return rank[cnt_0 + ans],rank[ans]
