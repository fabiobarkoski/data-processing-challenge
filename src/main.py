import pandas as pd

file_chart = ''
file_acc = ''

df1 = pd.read_excel(file_chart)
chart = df1['account']

df2 = pd.read_excel(file_acc)
acc = df2['account']
value = df2['value']

list = []
list2 = []
list3 = []

for c in chart:
    v = (df2.loc[df2['account'] == c, 'value']).sum()
    leng = len(str(c)) - 2
    list.append([c[1:leng], v])

    if v.sum() != 0:
        with open('result.txt', 'a') as f:
            f.write(f'{c} == {v.sum()}\n')

        df = pd.DataFrame(list, columns=['account', 'value'])

for d in df['account']:
    r = (df.loc[df['account'] == d, 'value']).sum()
    leng2 = len(str(d)) - 2
    list2.append([d[0:leng2], r])

pf = pd.DataFrame(list2, columns=['account', 'value'])
pf.drop_duplicates(subset="value", keep="last", inplace=True)

for p in pf['account']:
    print(p)


for p in pf['account']:
    leng3 = len(str(p)) - 2
    list3.append([p[0:leng3], pf['value'].sum()])

    pf2 = pd.DataFrame(list3, columns=['account', 'value'])
    pf2.drop_duplicates(subset="value", keep="last", inplace=True)

print(pf2)
