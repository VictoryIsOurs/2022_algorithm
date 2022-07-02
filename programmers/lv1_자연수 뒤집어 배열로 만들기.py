~~~
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
~~~

def solution(n):

    answer=[]
    
    # str to list
    answer = list(str(n))
    answer.reverse()
    
    return list(map(int, answer))
  
  
  
  
  ############################
# 파이썬에서 String을 List로 변환하는 방법
1. 문자열의 문자들을 분리하여 리스트로 변환
2. split()으로 문자열을 분리하여 리스트로 변환
3. slicing으로 문자열을 추출하여 리스트로 변환
