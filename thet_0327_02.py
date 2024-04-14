#제목:for 반복문 기초

hap=0
n=int(input("n을 입력하세요:"))
for i in range(n+1):
    hap=hap + i
print("i: {:4d} hap: {}".format(i, hap))