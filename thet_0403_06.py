#제목: 리스트 요소 추가삭제 및 for 반복문 출력

list_a=[1,2,3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스츠 충간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)
print()

number=[273,32,103,57,52]
aaa=[1,"Sunmoon",2,"Sunmoon",3,"하바드"]
aaa.insert(2,"좋아요")
aaa.pop(-1)
del aaa[-1]

for i in number:
    print("i:",i,end="")
print()
for j in aaa:
    print("j:",j,end="")
