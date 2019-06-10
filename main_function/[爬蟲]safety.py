# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
import html5lib

url = 'https://www.boca.gov.tw/sp-trwa-list-1.html'
table = pd.read_html(url, header=1)    # 讀入網站，將表格的第1行設定為header
df = pd.DataFrame(table[0])            # 第0張表格為東亞國家


"""清理dataframe內的資料，將第一欄'國家'的中文與英文分開"""
tmp_country_list = list( df['國家'] )    # 把'國家'那一欄的資料轉換成list
country_list = list()

for country in tmp_country_list:
    chn_eng = country.split()
    
    # 若只含一個中文，一個英文
    if len(chn_eng) == 2:
        new_sublist = [ chn_eng[0], chn_eng[1] ]
    
    # 若國家英文超過一個單字以上
    if len(chn_eng) > 2:
        tmplist = chn_eng[1:]
        eng = ''
        for i in range(len(tmplist)):
            if i == 0:
                eng += tmplist[i]
                continue
            eng += ' ' + tmplist[i]
        new_sublist = [ chn_eng[0], eng ]
    
    country_list.append(new_sublist)

df2 = pd.DataFrame(country_list, columns = ['國家(中文)', '國家(英文)'])


"""結合兩張dataframe，分別是清理過後的df2與從網頁爬下來的df"""
df3 = pd.merge(df2, df[['國家地區','最新警示提醒']], right_index=True, left_index=True)
df4 = df3.set_index( '國家(中文)' )


"""輸出目標國家，並匯出成csv"""
df5 = df4.loc[ ['韓國', '日本', '泰國', '新加坡'], ['國家地區', '最新警示提醒'] ]

country_needed = input()

for i in range(len(df5)):    
    if df5.iloc[i]['國家地區'] == '日本 - 福島縣(第一核電廠半徑30公里內區域及計畫避難區域) Japan - Fukushima' and df5.iloc[i]['最新警示提醒'] == '紅色警示-不宜前往，宜儘速離境':
        df5.iloc[i]['最新警示提醒'] = '福島地區 紅色警示-不宜前往，宜儘速離境；其餘地區 沒有警示'
        continue
    
    if df5.iloc[i]['最新警示提醒'] == '灰色警示-提醒注意':
        df5.iloc[i]['最新警示提醒'] = '沒有警示'

if df5['國家(中文)'] == country_needed:
    print(df5['最新警示提醒'])
