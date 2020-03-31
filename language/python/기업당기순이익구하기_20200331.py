#!/usr/bin/env python
# coding: utf-8

#Json이용한 상장사의 원하는 기간동안 당기순이익을 구하는 코드임. 
import requests
import re
from io import BytesIO
import json

#Step0: 고유번호를 구하는 코드를 이용해 회사명으로 고유번호 구해서 입력할 것.
corp_code = '00126380'                                #삼성전자 고유번호
corp_name = '삼성전자'
api_key = 'c5bef4a07d6cf77d1ec49e10e019c1aa351bee9e' #자신의 API
find_year = 2016                                      #검색할 시작 년도
end_year = 2021                                       #검색 마지막 년도
report_code_list = ['11013', '11012', '11014', '11011'] #1~4분기 보고서 코드

#d = {'11013':'1분기보고서', '11012':'반기보고서', '11014':'3분기보고서', '11011':'사업보고서'}

#Step2: 4분기 보고서는 1~3분기 당기순이익이 누적되어 있으므로 순수당기 순이익을 계산해 준다. 
def find_NetIncome(corp_code, start_year, end_year, report_code):
    url = f'https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json?crtfc_key={api_key}&corp_code={corp_code}&bsns_year={str(find_year)}&reprt_code={report_code}&fs_div=CFS'
    #print(url)
    r = requests.get(url)   
    if(json.loads(r.text)['status'] != '000'):
        print(json.loads(r.text))
        return ;
    jsonList = json.loads(r.text)['list']
    for info in jsonList:        
        if info['account_nm'] == '당기순이익(손실)' and info['sj_nm'] == '포괄손익계산서':
            net_income_list.insert(rpt_cnt, int(info['thstrm_amount']))
            if rpt_cnt != 3:
                print(info['bsns_year'],"년","당기순이익",rpt_cnt+1, "분기 =",info['thstrm_amount'])
            else : #4분기 사업보고서는 1~3분기 당기순이익 전체 합이므로 4분기 순수 당기 순이익 계산해줘야 한다.                
                net_income_list[rpt_cnt] = net_income_list[3] - (net_income_list[2]+ net_income_list[1] + net_income_list[0])
                print(info['bsns_year'],"년","당기순이익",rpt_cnt+1,"분기 =", net_income_list[rpt_cnt])

#Step1: 원하는 기간의 1~4분기 보고서의 포괄손익 계산서에서 당기순이익 구하는 함수 호출
while find_year < end_year:
    print("{}년도 {} 분기별 당기순이익입니다.".format(find_year, corp_name))
    rpt_cnt = 0
    net_income_list = []
    for report_code in report_code_list:
        #print(report_code)
        find_NetIncome(corp_code, find_year, end_year, report_code)
        rpt_cnt += 1
    find_year += 1

### ================================================================================================
### 회사 고유 번호 구하는 코드
### 필요한 모듈
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import xml.etree.ElementTree as ET

### 회사고유번호 데이터 불러오기
url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=c5bef4a07d6cf77d1ec49e10e019c1aa351bee9e'
with urlopen(url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('corp_num')

### 압축파일 안의 xml 파일 읽기
tree = ET.parse('CORPCODE.xml')
root = tree.getroot()

### 회사 이름으로 회사 고유번호 찾기
def find_corp_num(find_name):
    for country in root.iter("list"):
        if country.findtext("corp_name") == find_name:
            return country.findtext("corp_code")
print(find_corp_num('삼성전자'))


### ================================================================================================




