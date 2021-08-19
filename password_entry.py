# 測試密碼程式

i = 0
password='a123456'
while i < 3 :
	user = input('請輸入密碼: ')
	if user == password:
		print('正確密碼')
		break
	else :
		print('密碼錯誤，你還有', 2 - i, '次機會')
	i = i + 1
	
