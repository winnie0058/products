import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename , 'r' , encoding='utf-8') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue
			# strip()去除換行符號
			# split()切割完為清單
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# def read_file(filename):
# 	products = []
# 	if os.path.isfile(filename):
# 		print('檔案存在')
# 		with open(filename , 'r' , encoding='utf-8') as f:
# 			for line in f:
# 				if '商品名稱,商品價格' in line:
# 					continue
# 				# strip()去除換行符號
# 				# split()切割完為清單
# 				name, price = line.strip().split(',')
# 				products.append([name, price])
# 			print(products)
# 	else:
# 		print('找不到檔案....')
# 	return products

# 使用者輸入
def user_input(products):
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
	# print(products)

	return products

def print_products(products):
	for p in products:
		# print(p)
		print(p[0],'的價格是',p[1])

# 寫入檔案
def write_file(products):
	with open('products.csv','w',encoding='utf-8') as f:
	# with open('products.csv') as f:
		f.write('商品名稱,商品價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():

	filename = 'products.csv'
	if os.path.isfile(filename):
		print('檔案存在')
		products = read_file(filename)
	else:
		print('找不到檔案....')

	products = user_input(products)
	print_products(products)
	write_file(products)

main()