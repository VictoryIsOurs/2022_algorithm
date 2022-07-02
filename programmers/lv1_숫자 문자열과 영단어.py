def solution(s):
    answer = ''
    dic = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3' , 'four' : '4' ,
          'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8' , 'nine' : '9' }

    word = ''
    for c in s : 
        if c in '0123456789' : #숫자라면 
            answer += c
            word = '' #word 초기화
            
        else : #문자라면 
            word += c
            if word in dic.keys() : 
                answer += dic[word]
                word = ''
                
    return int(answer)  #int괄호 씌우면 str to int임.
  
  
  
  # 주의 : str과 int type은 + 불가  / int(answer)하면 str to int 됨.
