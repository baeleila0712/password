password = '0716'
x = 1
while x < 4 :
	x = x + 1
	password = input('請輸入密碼： ')
	if password == '0716':
		print('登入成功')
		break
	elif x == 2:
		print('登入失敗 你還有兩次機會')
	elif x == 3:
		print('登入失敗 你還有一次機會')
	else:
		print('密碼三次錯誤 請洽客服中心')
