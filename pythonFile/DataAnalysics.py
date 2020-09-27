import pandas as pd
fileName = r'C:\Users\zhangkeke\Desktop\python数据分析.xlsx'
xls = pd.ExcelFile(fileName, dtype='object')
sales = xls.parse('Sheet1', dtype='object')
salesDf=sales.dropna(subset=['购药时间','社保卡号'],how='any')
print('删除前大小',sales.shape)
sales = sales.dropna(subset=['购药时间','社保卡号'], how='any')
sales['销售数量'] = sales['销售数量'].astype('float')
sales['应收金额'] = sales['应收金额'].astype('float')
sales['实收金额'] = sales['实收金额'].astype('float')
print('after as type:', sales.dtypes)


def  saleTimeTransfer(timeStr):
    timeList = []
    for value in timeStr:
        dateStr = value.split(' ')[0]
        timeList.append(dateStr)
    timeSer = pd.Series(timeList)  # 将列表转行为一维数据Series类型
    return timeSer

    time= sales.loc[:,'购药时间']
    newDate= saleTimeTransfer(time)
    sales.loc[:,'购药时间'] = newDate
    sales.loc[:, '购药时间'] = pd.to_datetime(sales.loc[:,'购药时间'], format='%Y-%m-%d', errors='coerce')
    salesDf = salesDf.dropna(subset=['购药时间', '社保卡号'], how='any')

