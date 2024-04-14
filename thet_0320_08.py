#날짜/시간과 관련된 기능을 가져옴
import datetime

#헌재 날짜/시간을 구함
now=datetime.datetime.now()

#오전 구분
if now.hour < 12:
    print(f"현재 시간은{now.hour} 오전")
    #print("현재 시각은{}".format(now.hour))
    
#계절 구분:붐
if 3 <=now.month <= 5:
    print(f"이번 달은 {now.month}월 붐")
    
#계절 구분:여름
if 6 <=now.month <= 8:
    print(f"이번 달은 {now.month}월 여름")