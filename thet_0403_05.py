#제목: 리스트 연산자 연결, 반복, len()

list_a=[1,2,3]
list_b=[4,5,6]
list_c=["선문대"]
list_d="선문대"

print("#리스트")
print("list_a=", list_a, type(list_a))
print("list_b=", list_b, type(list_b))
print("list_c=", list_c, type(list_c))
print("list_d=", list_d, type(list_d))
print()
print(list_c[0], type(list_c[0]))
print(list_d[0], type(list_d[0]))


print("# 리스트 기분 연산자")
print("list_a+list_b=",list_a+list_b)
print("list_a*3=", list_a*3)
print()

print("# 길이 구하기")
print("len(list_a)=", len(list_a))