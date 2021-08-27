import pandas as pd

# path to chart of accounts and general ledger
file_chart = '/path/to/file.xlsx'
file_acc = '/path/to/file.xlsx'

# create the dataframe of the chart
df1 = pd.read_excel(file_chart)
chart = df1['account']

# create the dataframe of the general
df2 = pd.read_excel(file_acc)

# create lists to append the accounts and value results
list = []
list2 = []
list3 = []

for c in chart:
    # get the accounts with same name and use the sum function from pandas
    v = (df2.loc[df2['account'] == c, 'value']).sum()
    # append on the list the accounts, but remove the last number.
    # for example: 1.2.1 -> 1.2
    leng = len(str(c)) - 2
    list.append([c[1:leng], v])

    # check and ignore the accounts with value equal to 0
    if v.sum() != 0:
        # write on the file the first step
        with open('result.txt', 'a') as f:
            f.write(f'{c} == {v.sum()}\n')
        # make a dataframe with the list
        df = pd.DataFrame(list, columns=['account', 'value'])

for d in df['account']:
    # again get the accounts with same name and sum them
    r = (df.loc[df['account'] == d, 'value']).sum()
    # again append
    leng2 = len(str(d)) - 2
    list2.append([d[0:leng2], r])

# make a dataframe and remove the duplicate rows
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
