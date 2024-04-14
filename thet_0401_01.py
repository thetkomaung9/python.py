#제목: 팩토리얼 계산하기 Review
#이름:딱코먼
n=int(input("n을 입력하세요: "))
fact=1
print(n, "!:", end="")
for i in range(n,0,-1):
    fact= fact*i
    print(i, end="")
    if(i>1):
        print("X", end="")
print(n, " =", fact)
    