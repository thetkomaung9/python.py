#제목: 별 피라미드 출력하기 Review
#이름:딱코먼
for i in range(1,10,2):
    for k in range(1,5-i):
        print("", end="")
    for j in range (0, i*2+1):
        print("*", end="")
    print();
    
print("*\t 1")
print("**\t 2")
print("***\t 3")
print("****\t 4")
print("*****\t 5")

rows = 4

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
