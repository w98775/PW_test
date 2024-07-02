# 密碼重試程式
# password = 'a123456' 
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確就印出登入成功，不正確就印出密碼錯誤，還有＿＿次幾會！

password = 'a123456'
i = 3 # 剩餘機會
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		i = i - 1
		if i > 0:
			print('密碼錯誤！ 還有', i, '次機會')
		else:
			print('密碼錯誤，沒有剩餘機會！')
