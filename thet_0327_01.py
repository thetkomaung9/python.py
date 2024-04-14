#제목:if ~ elif Review
#이름:딱코먼

year=int("연도를 입력하세요:")
print(year,type(year))
if year >2024 and year <=2050:
    print("가까운 연도")
elif year <=2100:
    print("비교적 가까운 연도")
else:
    print("내가 살아있을까?")