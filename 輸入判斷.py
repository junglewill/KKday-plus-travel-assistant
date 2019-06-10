#打開kkday ouput.csv
import csv
fn = 'kkday_csv/tample.csv'
fh = open(fn, 'r', newline = '', encoding = 'utf-8')
csv = csv.DictReader(fh)
fields = csv.fieldnames

#輸入關鍵字(kw)，用空格分隔後存進kwList
kwList = input('請輸入您期望的條件關鍵字：').split()
noList = input('請輸入您不想要的條件關鍵字：').split()

#SelectCity = '沖繩' #測試時打開
resultNum = 0 #找到幾筆符合結果
resultList = [] #存放符合的結果
#走訪ouput.csv的info
for aline in csv:
    if SelectCity == aline[fields[1]]: 
        count = 0 #檢查找到的kw數
        info = aline[fields[5]]
    #走訪kwList中的關鍵字，查看是否皆出現在某行程的'info'中
        if len(kwList) == 0 and len(noList) == 0:
            count = len(kwList)

        else:
            for kw in kwList:
                if kw in info:
                    count += 1
        #走訪noList中不想要的關鍵字           
            for no in noList:
                if no in info:
                    count -= 1
            
        if count == len(kwList):
            resultNum += 1
            result = [] #存放符合結果的內容
            result.append('行程名稱：' + aline[fields[3]])
            result.append('價格：' + aline[fields[4]])
            result.append('介紹：' + aline[fields[5]])
            result.append('連結：' + 'https://www.kkday.com/zh-tw/product/' + aline[fields[2]])
            resultList.append(result)

if resultNum == 0:
    print('查無符合的結果！')

#for r in resultList:
    #print(r)
