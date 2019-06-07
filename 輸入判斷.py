#打開kkday ouput.csv
import csv
fn = 'kkday_csv/tample.csv'
fh = open(fn, 'r', newline = '', encoding = 'utf-8')
csv = csv.DictReader(fh)
fields = csv.fieldnames

#輸入關鍵字(kw)，用空格分隔後存進kwList
kwList = input().split()

result = 0 #查找到幾筆結果
#走訪ouput.csv的info
for aline in csv:
    count = 0 #檢查找到的kw數
    info = aline[fields[4]]
#走訪kwList中的關鍵字，查看是否皆出現在某行程的'info'中
    for kw in kwList:
        if kw in info:
            count += 1
    if count == len(kwList):
        result += 1
        print('行程名稱：' + aline[fields[2]])
        print('價格：' + aline[fields[3]])
        print('介紹：' + aline[fields[4]])
        print('連結：' + 'https://www.kkday.com/zh-tw/product/' + aline[fields[1]])

if result == 0:
    print('查無符合的結果！')

