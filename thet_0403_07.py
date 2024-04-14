#제목: range() 함수 review
a=range(10)
print(a,type(a))
b=list(a)
print(b, type(b))
c=range(0, int(11/2))
print(c, type(c))
aaa=[1,2,3,4,5.5,7.8,111, "Sunmoon", 'a']
for i in range(5):
    print(i, ": 반복")
for i in range(len(aaa)):
    print(i,":", aaa[i], end="\t")
###역반복문
for i in range(10):
    print(i, ":", "반복횟수")
for i in reversed(range(1,11)):
    print(i, ":", "반복횟수")