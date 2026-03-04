import csv

data=[]

title='test'
author='aaa'
nrec='18'

data.append([title, author, nrec])

with open('pttnba.csv','w', newline='', encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['標題', '作者', '推文數'])
    writer.writerows(data)

print("成功寫入")
