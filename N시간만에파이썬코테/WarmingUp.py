/* 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
예: 8888의 경우 4로 카운팅해야함.
*/

//먼저 1부터 10,000까지 리스트로 받는다.
list(range(1, 10001))  //from-to 구간 주의
//또는 
[for i in range(1, 10001)]


//string으로 변환
str(list(range(1, 10001)))

//count함수 사용
str(list(range(1, 10001))).count('8')  //8을 카운트 해준다. 


//시간복잡도 구하기
%%timeit

//정답
count = 0
for ch in str(list(range(1, 10001))) :
  if '8' in str(ch) :   //string에 8이 들어있으면
    count += str(ch).count('8')  //8의 갯수를 센다.
    
//------------------------------------------------------------------------

/*
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하라. (단, 점들의 배열은 모두 정렬되어있다고 가정.)
예를 들어 S = [1, 3, 4, 8, 13, 17, 20]이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
*/


//for을 돌린 후, 가장 짧은 거리의 점들을 저장

minDistance = S[len(S)-1] - S[0] //끝에서 처음꺼 빼기
minLeftPoint = S[0]
minRightPoint = S[0]

for i in S:
  for j in S:
    if j-i <= minDistance : 
      minDistance = j-i
      minLeftPoint = S[i]
      minRightPoint = S[j]

