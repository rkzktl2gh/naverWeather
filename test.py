from naverWeather import *
while(1):
 print("메뉴를 선택하세요.")
 print("1번 : 검색, 2번 : 종료, 3번 : 옷장에 옷 넣기")
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
 elif control == '3': # 3번 입력 시
  L1 = list()
  L2 = list()
  L3 = list()
  while(1):
      print("-------------------------------------------------")
      print("                <<< 옷     장 >>>                ")
      print("1번 : 상의 | 2번 : 하의 | 3번 : 신발 | 4번 : 종료")
      print("-------------------------------------------------")
      room = input()
      if room == '1':
          while(1):
              print("-------------------------------------------------------------------")
              print("                        <<< 상의 코너 >>>                        ")
              print("1번 : 옷 추가하기 | 2번 : 옷 삭제하기 | 3번 : 확인하기 | 4번 : 종료")
              print("-------------------------------------------------------------------")
              room1 = input()
              if room1 == '1':
                  i = 0
                  print("------------------------")
                  print("   옷을 입력해주세요.   ")
                  print("ex) 흰색긴팔 or 회색반팔")
                  print("------------------------")
                  L1.insert(i, str(input("")))
              if room1 == '2':
                  print("----------------------------------")
                  print("아래 목록에서 삭제할 옷을 고르시오")
                  print(L1)
                  print("삭제할 옷은?")
                  print("----------------------------------")
                  L1.remove(str(input("")))
                  print("삭제되었습니다~")
              if room1 == '3':
                  print(L1)
              if room1 == '4':
                  break
      if room == '2':
          while(1):
              print("-------------------------------------------------------------------")
              print("              <<< 하의 코너 >>>              ")
              print("1번 : 옷 추가하기 | 2번 : 옷 삭제하기 | 3번 : 확인하기 | 4번 : 종료")
              print("-------------------------------------------------------------------")
              room1 = input()
              if room1 == '1':
                  i = 0
                  print("----------------------------")
                  print("     옷을 입력해주세요.     ")
                  print("ex) 흰색긴바지 or 회색반바지")
                  print("----------------------------")
                  L2.insert(i, str(input("")))
              if room1 == '2':
                  print("----------------------------------")
                  print("아래 목록에서 삭제할 옷을 고르시오")
                  print(L2)
                  print("삭제할 옷은?")
                  print("----------------------------------")
                  L2.remove(str(input("")))
                  print("삭제되었습니다~")
              if room1 == '3':
                  print(L2)
              if room1 == '4':
                  break
      if room == '3':
          while(1):
              print("---------------------------------------------------------------------")
              print("              <<< 신발 코너 >>>              ")
              print("1번 : 옷 추가하기 | 2번 : 신발 삭제하기 | 3번 : 확인하기 | 4번 : 종료")
              print("---------------------------------------------------------------------")
              room1 = input()
              if room1 == '1':
                  i = 0
                  print("--------------------------------")
                  print("      신발을 입력해주세요.      ")
                  print("ex) 검은색운동화 or 흰색구두")
                  print("--------------------------------")
                  L3.insert(i, str(input("")))
              if room1 == '2':
                  print("------------------------------------")
                  print("아래 목록에서 삭제할 신발을 고르시오")
                  print(L3)
                  print("삭제할 신발은?")
                  print("------------------------------------")
                  L3.remove(str(input("")))
                  print("삭제되었습니다~")
              if room1 == '3':
                  print(L3)
              if room1 == '4':
                  break
      if room == '4':
          break
 else:
     print("다시입력해주세요")
