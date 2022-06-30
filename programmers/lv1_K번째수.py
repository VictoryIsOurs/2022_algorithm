#1번째 오류
>> TypeError: list indices must be integers or slices, not list

#2번째 오류
>> index Error


def solution(array, commands):
    answer = []
    sliceList = []
    
    for i in range(len(commands)) :  #range를 안하고 바로 commands로 하게 되면 3번이 아니라 9번 돈다.
        
        start = commands[i][0]
        end = commands[i][1]
        index = commands[i][2]
        
        sliceList = array[start-1 : end]  #end 주의
        
        sliceList.sort()
        
        num = sliceList[ index - 1 ]
        
        answer.append(num)
        
    return answer
  

#알아야 할 개념
#파이썬 - list sclice 개념!
>>> a = ['a', 'b', 'c', 'd', 'e']
# 3칸씩 이동하면서 가져옵니다.
>>> a[ -5 : : 3 ]
['a', 'd']


