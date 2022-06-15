
def solution(new_id):
    
    #1단계
    new_id = new_id.lower()
#    for i in range(len_new_id):
#        if(new_id[i].isupper() == True): #1단계
#                new_id[i].lower()
    
    #2단계
    answer = ''
    for i in new_id:
        if i.islower() or i.isdigit() or i in '-_.': #오답났던 부분
            answer += i
    
    #3단계
    while '..' in answer:
            answer = answer.replace("..", ".")
            
    #4단계                
    if(answer[0] == '.' and len(answer)>1): #오답 : & 이라고 씀.
            answer = answer[1:]
            
    if answer[-1] == '.': #오답: answer[len(answer)] == '.'
            answer = answer[:-1]
    
    #5단계
    if len(answer)==0:
        answer = 'a'
        
    #6단계
    if len(answer)>=16:
        answer = answer[:15]
        if(answer[-1]) == '.':
            answer = answer[:-1]
            
    #7단계
    if len(answer) <= 3:
        answer = answer + answer[-1]*(3-len(answer))
    
    return answer
