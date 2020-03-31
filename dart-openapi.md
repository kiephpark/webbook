# dart open api에서 재무 정보 읽어 오는 방법 예시

## 1. 종목 정보 가져오기

```python
# This Python file uses the following encoding: utf-8
import requests, zipfile, io
import re
from io import BytesIO
import pandas as pd
import json
import xmltodict

corp_code = '005930'
rcept_no = '20190401004781'
reprt_code= '11011'
api_key = 'xxxxxxxxxxxxxxxxxxx' #opendart에서 신청하기.
url = f'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={api_key}'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

```

- CORPCODE.xml파일로 저장되는데, 아래와 같이 json으로 변환하거나, dict 형태로 변환 가능하다.

```python
import json
import xmltodict
with open("CORPCODE.xml", 'r', encoding='UTF8') as f:
  xmlString = f.read()

# print(xmlString)
dictList = xmltodict.parse(xmlString)
# print(dictList)
jsonString = json.dumps(dictList, indent=2, ensure_ascii=False)
# print(jsonString)
```

## 2. XBRL format 파일 가져오기

- xbrl 라고 재무제표에서 사용하는 표준인 듯 하나.. 쓰임이 있을 지...

```python
# This Python file uses the following encoding: utf-8
import requests, zipfile, io
import re
from io import BytesIO
import pandas as pd
import json
import xmltodict

corp_code = '005930'
rcept_no = '20190401004781'
reprt_code= '11011'
api_key = 'c5bef4a07d6cf77d1ec49e10e019c1aa351bee9e' #opendart에서 신청하기.
url = f'https://opendart.fss.or.kr/api/fnlttXbrl.xml?crtfc_key={api_key}&rcept_no={rcept_no}&reprt_code={reprt_code}'
print(url)
r = requests.get(url)
print(r.status_code)
print(type(r.content))
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
```

## 3. dart open api를 이용하여 제무 정보 읽어오기

### 3.1 dart open api를 이용하여 rcep_no 정보 읽어오기

- 아래 api를 이용하여 제무제표에 필요한 rcept_no를 가져올 수 있다.

```python
import requests, zipfile, io
import re
from io import BytesIO
import json


corp_code = '00356370'
api_key = 'c5bef4a07d6cf77d1ec49e10e019c1aa351bee9e' #opendart에서 신청하기.
url = f'https://opendart.fss.or.kr/api/list.json?crtfc_key={api_key}&corp_code={corp_code}&bgn_de=20190101&pblntf_detail_ty=A001&pblntf_detail_ty=A002&pblntf_detail_ty=A003&corp_cls=Y&page_no=1&page_count=30'
r = requests.get(url)
jsonList = json.loads(r.text)['list']
for info in jsonList:
  print(info['rcept_no'])
  print(info['report_nm'])

```

### 3.2 주요 계정 정보 읽어 오기

- 매출액, 영업이익, 순이익, 자산, 자본, 부채의 주요 정보만 필요하면 아래 api를 이용하면 된다.

```python
url = f'https://opendart.fss.or.kr/api/fnlttMultiAcnt.json?crtfc_key={api_key}&corp_code={corp_code}&bsns_year=2018&reprt_code=11011'
r = requests.get(url)
jsonList = json.loads(r.text)['list']
for info in jsonList:
  print(info['account_nm'])
  print(info['thstrm_amount'])
  print(info['sj_nm'])
```

### 3.3 모든 계정 정보 읽어 오기

- 한 회사의 주요 정보내 정보가 필요할 때 사용하면 된다.

```python
url = f'https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json?crtfc_key={api_key}&corp_code={corp_code}&bsns_year=2018&reprt_code=11011&fs_div=CFS'
r = requests.get(url)
jsonList = json.loads(r.text)['list']
for info in jsonList:
  print("계정명: ", info['account_nm'])
  print("당기금액: ", info['thstrm_amount'])

```

## 4. dart에서 제무 정보를 csv 파일로 저장하기

- csv로 저장하게 되면 excel 함수를 이용하여 다양한 정보를 표현할 수 있음.

```pyyhon
# This Python file uses the following encoding: utf-8
import requests
import re
from io import BytesIO
import pandas as pd


crp_cd = '005930'
api_key = 'c5bef4a07d6cf77d1ec49e10e019c1aa351bee9e' #opendart에서 신청하기.
url = f'https://opendart.fss.or.kr/api/list.xml?crtfc_key={api_key}&corp_code={crp_cd}&bgn_de=20190101&pblntf_detail_ty=A001&pblntf_detail_ty=A002&pblntf_detail_ty=A003&corp_cls=Y&page_no=1&page_count=30'
resp = requests.get(url)
webpage_of_api = resp.content.decode('utf-8')

rcp_no_list = re.findall(r'<rcept_no>(.*?)</rcept_no>', webpage_of_api) #정규식으로 rcp_no만 추출
period_list = re.findall(r'<report_nm>(.*?)</report_nm>', webpage_of_api)#정규식으로 period_no만 추출

dcm_no_list = []
for rcp_no in rcp_no_list:
    resp = requests.get('http://dart.fss.or.kr/dsaf001/main.do?rcpNo={}'.format(rcp_no))
    webpage_of_viewer = resp.content.decode('utf-8')
    dcm_no = re.findall(r"{}', '(.*?)',".format(rcp_no), webpage_of_viewer)[0] #공시 뷰어사이트에서 rcp_no 가지고 dcm_no 구하기
    dcm_no_list.append(dcm_no)

print(rcp_no_list, dcm_no_list, period_list)


def download_excel(rcp_no, dcm_no, period, company):
    url = 'http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=' + rcp_no +'&dcm_no='+ dcm_no +'&lang=ko'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Geck/20100101 Firefox/69.0"
    resp = requests.get(url, headers={"user-agent": user_agent})
    for sheet in ["연결 포괄손익계산서", "연결 재무상태표", "연결 손익계산서"]:
    # sheet="연결 재무상태표"
        table = BytesIO(resp.content)
        data = pd.read_excel(table, sheet_name=sheet,skiprows=5)
        data.to_csv('company_{}_{}.csv'.format(period, sheet), encoding="euc-kr")


for period, rcp_no, dcm_no in zip(period_list, rcp_no_list, dcm_no_list):
    download_excel(rcp_no, dcm_no, period, '삼성전자')


df = pd.read_csv('./company_사업보고서 (2018.12)_연결 손익계산서.csv', encoding='euc-kr')

df == '영업이익(손실)' #읽어온 행,열중에서 영업이익만 true로 보여주기
print(df)
df_boolean = df == '영업이익(손실)'
#df_boolean
#영업이익(손실) 위치 구하기.
x = df_boolean.sum(axis=1).values.argmax()
y = df_boolean.sum(axis=0).values.argmax()
#영업이익(손실)의 값의 위치
df.iloc[x, y+1] #iloc란 table에서 행,열의 값 가져오기

#현재 디렉토리에 있는 모든 엑셀 파일들을 읽어서 당기순이익을 프린트 하기 
os.listdir('./csv')
for filename in os.listdir('./csv'): #현재 디렉토리에 있는 모든 엑셀 파일들의 파일이름을 얻어와서
    df = pd.read_csv('./csv/{}'.format(filename), encoding='euc-kr') #각각의 엑셀 파일을 읽는다.
    df_boolean = df == '당기순이익(손실)'
    #df_boolean
    #당기순이익(손실) 위치 구하기.
    x = df_boolean.sum(axis=1).values.argmax()
    y = df_boolean.sum(axis=0).values.argmax()
    num = df.iloc[x, y+1] #당기순이익 금액
    print(filename[8:23], num)
```
