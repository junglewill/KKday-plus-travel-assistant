import csv

#使用這輸入城市名稱和日期，日期格式為8位數字
city = input("請輸入城市名稱：")
date1 = input("請輸入開始日期：")
date2 = input("請輸入結束日期：")

#開啟溫度檔案
file = "C:\\Users\\user\\Desktop\\107-2\\商管程式設計\\Final Project\\Tem_Data\\" + city + ".csv"

#每個月分的天數
month = [31,28,31,30,31,30,31,31,30,31,30,31]

#把日期換成每年第幾天
day1 = 0
day2 = 0
	
for i in range(10 * int(date1[4]) + int(date1[5])-1) :
	day1 += month[i]

day1 += 10 * int(date1[6]) + int(date1[7])


for i in range(10 * int(date2[4]) + int(date2[5])-1) :
	day2 += month[i]

day2 += 10 * int(date2[6]) + int(date2[7])
	
#找到那天的氣溫資料	
n = 0
with open(file, newline='') as csvFile:
	#直接讀取：讀取 CSV 檔案內容
	rows = csv.reader(csvFile)
	# 迴圈輸出 每一列
	for row in rows:
		n += 1 
		if day1 <= n <= day2 + 1:
			print("最高氣溫：" + str(row[1]))
			print("最低氣溫：" + str(row[2]))

