from naverWeather import *
while(1):
 print("메뉴를 선택하세요.")
 print("1번 : 검색, 2번 : 종료")
 control = input()
 if control == '1': # 1번 입력 시
  print("지역명을 입력해주세요.")
  area=input()
  if area in naverWeather.map_cityNum: # 올바른 도시명 입력 시
   print(naverWeather(area).getWeather())
  elif area =='': print(naverWeather("서울").getWeather())
  else: # 잘못된 도시명 입력 시
   print("잘못된 도시명입니다. 다시 입력하세요")
   area=input()
   if area in naverWeather.map_cityNum:
    print(naverWeather(area).getWeather())
   else:
      while(area not in naverWeather.map_cityNum):
          print("잘못된 도시명입니다. 다시 입력하세요")
          area=input()
          if area in naverWeather.map_cityNum:
              print(naverWeather(area).getWeather())
 elif control == '2': # 2번 입력 시
  print("프로그램을 종료합니다.")
  break
 else:
     print("다시입력해주세요")
