L1 = list()
L2 = list()
L3 = list()

class room():
    def room_1():
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
            elif room1 == '2':
                print("----------------------------------")
                print("아래 목록에서 삭제할 옷을 고르시오")
                print(L1)
                print("삭제할 옷은?")
                print("----------------------------------")
                a = str(input())
                if a in L1:
                    L1.remove(a)
                    print("삭제되었습니다~")
                else:
                    print("<<<<<<<<<입력한 옷이 없습니다.>>>>>>>>>")
                    print("<<<확인하시고 다시 입력부탁드립니다.>>>")
            elif room1 == '3':
                print(L1)
            elif room1 == '4':
                break
            else:
                print("<<<<<<잘못입력하셨습니다. 다시입력해주세요>>>>>>")
                print("")
    def room_2():
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
                L2.insert(i, str(input()))
            elif room1 == '2':
                print("----------------------------------")
                print("아래 목록에서 삭제할 옷을 고르시오")
                print(L2)
                print("삭제할 옷은?")
                print("----------------------------------")
                b = str(input(""))
                if a in L2:
                    L2.remove(b)
                    print("삭제되었습니다~")
                else:
                    print("<<<<<<<<<입력한 옷이 없습니다.>>>>>>>>>")
                    print("<<<확인하시고 다시 입력부탁드립니다.>>>")
            elif room1 == '3':
                print(L2)
            elif room1 == '4':
                break
            else:
                print("<<<<<<잘못입력하셨습니다. 다시입력해주세요>>>>>>")
                print("")
    def room_3():
        while(1):
            print("---------------------------------------------------------------------")
            print("              <<< 신발 코너 >>>              ")
            print("1번 : 신발 추가하기 | 2번 : 신발 삭제하기 | 3번 : 확인하기 | 4번 : 종료")
            print("---------------------------------------------------------------------")
            room1 = input()
            if room1 == '1':
                i = 0
                print("--------------------------------")
                print("      신발을 입력해주세요.      ")
                print("ex) 검은색운동화 or 흰색구두")
                print("--------------------------------")
                L3.insert(i, str(input()))
            elif room1 == '2':
                print("------------------------------------")
                print("아래 목록에서 삭제할 신발을 고르시오")
                print(L3)
                print("삭제할 신발은?")
                print("------------------------------------")
                c = str(input())
                if c in L3:
                    L3.remove(c)
                    print("삭제되었습니다~")
                else:
                    print("<<<<<<<<<입력한 옷이 없습니다.>>>>>>>>>")
                    print("<<<확인하시고 다시 입력부탁드립니다.>>>")
            elif room1 == '3':
                print(L3)
            elif room1 == '4':
                break
            else:
                print("<<<<<<잘못입력하셨습니다. 다시입력해주세요>>>>>>")
                print("")
