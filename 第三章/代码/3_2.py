import pandas as  pd
"""
绝对路径(不适用于控制台输入):
path = r'E:\学习\python\code\python数据分析与挖掘实战\第三章\数据集\catering_sale.xls'
如果需要将py文件整体运行,建议采用下边的path
"""
path = r'../数据集/catering_sale.xls'

data = pd.read_excel(path,index_col=u'日期')
#指定列属性'日期'为索引
data = data[(data[u'销量']>400) & (data[u'销量']<5000)]#过滤
status = data.describe()
status.loc['range'] =status.loc['max'] - status.loc['min'] #极差
status.loc['var'] = status.loc['std']/status.loc['mean']#变异系数
status.loc['dis']=status.loc['75%']-status.loc['25%']#四分位数间距
print(status)
