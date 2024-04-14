#제목: for반복문과 while 반복문으로 1~n까지 n의 배수의 합을 출력하세요
#이름: 딱코먼

#for 반복문
#n= input("정수 n을 입력하세요: ")
#x=int(input("배수 x을 입력하세요: "))
#sum=0
#for i in range(0,n+1, x):
  #   print("i: {:5d} sum: {}". format(i, sum))
#print("Last sum=", sum)


#while 반복문
i=0
while i < n:
    sum=sum+i
    i=i+x
    print("i: {:5d} sum: {}". format(i, sum))
print("Last sum=", sum)