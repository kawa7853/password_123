password = "123"
x = 1
while True:
	p = input("請輸入密碼：")
	if x == 3:
		print("廢物忘記自己密碼")
		break
	elif p == password:
		print("恭喜發財")
		break
	else:
	    x+=1
	    print("您還有",4-x,"次機會")