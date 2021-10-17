import os #operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):
	print('檔案存在')
	with open('products.csv' , 'r' , encoding='utf-8') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue
			# strip()去除換行符號
			# split()切割完為清單
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
else:
	print('找不到檔案....')


# 使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name , price]
	# products.append(p)
	products.append([name, price])

# 印出所有資料
print(products)

# for p in products:
# 	# print(p)
# 	print(p[0],'的價格是',p[1])

# 寫入檔案
with open('products.csv','w',encoding='utf-8') as f:
# with open('products.csv') as f:
	f.write('商品名稱,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
