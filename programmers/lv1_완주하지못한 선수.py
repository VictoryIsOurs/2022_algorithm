#1 : TestCase 정답 | 효율성 오답 
def solution(participant, completion):
    answer = ''
    
    for person in participant : 
        
        if person in completion :  #완주자
            completion.remove(person)  #remove() : 값으로 제거
            pass
        else : #완주X
            answer = person

            
    return answer


# 문제점 : for문 및 for문안에서 in으로 인해 O(n^2) --> 효율성 오답 
#         또한  if내에서 remove로 인해 O(n^2)   


#2 : dictionary를 사용하여 효율성 해결
def solution(participant, completion):
    hash = {} #dictionary {key : value }
    
    answer = ''
    
    for person in participant : 
        if person in hash : 
            hash[person] += 1 #중복 체크
    
        else : 
            hash[person] = 1 #완주자 체크
    
    for person in completion : 
        if hash[person] == 1 : #완주자 체크 
            del hash[person]
        else : 
            hash[person] -= 1
    
    answer = list(hash.keys())[0]
    
    return answer
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
