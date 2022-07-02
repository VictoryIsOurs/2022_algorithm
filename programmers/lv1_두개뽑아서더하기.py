def solution(numbers):
    answer = []
    for i in range(0, len(numbers)): #5
        for j in range(i+1, len(numbers)): #1~5
            if numbers[i] + numbers[j] not in answer : 
                    answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer
  
    
    ##오답 체크
    # for i in numbers : 
    #  for j in range(i+1, len(number)) : 
    # 로 했을 때,  numbers에서 직접 뽑게 되면 같은 수(4+4) 같은 수가 더해져서 값이 안나옴. 
    
    
