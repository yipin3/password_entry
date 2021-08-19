# 測試密碼程式

i = 3
password='a123456'
while i > 0:
	i = i - 1
	user = input('請輸入密碼: ')
	if user == password:
		print('正確密碼')
		break
	else :
		print('密碼錯誤')
		if i > 0:
			print('你還有', i, '次機會')
		else:
			print('沒機會囉')
