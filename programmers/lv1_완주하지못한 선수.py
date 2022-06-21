#1 : 효율성에서 다 틀림. 
def solution(participant, completion):
    answer = ''
    
    for person in participant : 
        
        if person in completion :  #완주자
            completion.remove(person)  #remove() : 값으로 제거
            pass
        else : #완주X
            answer = person

            
    return answer


# 문제점 : for문안에 in으로 O(n^2) / 또한  remove로 인해 O(n2) , 조건문에 in이 있어서 O(n2)에 걸림.  sort 후 해결  
#2 : 

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
