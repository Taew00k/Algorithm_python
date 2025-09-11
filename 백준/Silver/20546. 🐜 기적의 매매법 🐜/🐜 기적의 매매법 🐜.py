money = int(input())
day = list(map(int,input().split()))
jun_num = 0
jun_money = money
sung_num = 0
sung_money = money
increase = 0
decrease = 0

for i in day:
      if i <= jun_money:
            jun_num += jun_money // i
            jun_money -= (jun_money // i) * i

for j in range(1, len(day)):
      if day[j] > day[j-1]:
            increase += 1
            decrease = 0
      elif day[j] < day[j-1]:
            decrease += 1
            increase = 0
      if decrease >= 3 and day[j] <= sung_money:
            sung_num += sung_money // day[j]
            sung_money -= (sung_money // day[j]) * day[j]
      elif increase >= 3 and sung_num > 0:
            sung_money += sung_num * day[j]
            sung_num = 0

sung = sung_money + sung_num * day[-1]
jun = jun_money + jun_num * day[-1]

if jun > sung:
      print("BNP")
elif sung > jun:
      print("TIMING")
else:
      print("SAMESAME")