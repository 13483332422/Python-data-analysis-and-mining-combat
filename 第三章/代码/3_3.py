import pandas as  pd
"""
绝对路径(不适用于控制台输入):
path = r'E:\学习\python\code\python数据分析与挖掘实战\第三章\数据集\catering_dish_profit.xls'
如果需要将py文件整体运行,建议采用下边的path
"""
path = r'../数据集/catering_dish_profit.xls'
data = pd.read_excel(path,index_col=u'菜品名')
data = data[u'盈利']
data.sort_values(ascending=False)#从大到小排序
#因为根据帕累托法则,我们需要销量更好的
#帕累托法则:认为20%的商品创造了80%的营业额
#换句话说我们只要累计营业额占到了80%的即可当然85%也行

import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
data.plot(kind='bar')
plt.ylabel(u'y盈利')
pa = 1.0*data.cumsum()/data.sum()#计算累计贡献率
pa.plot(color='r',secondary_y=True,style='-o',linewidth=2)
plt.annotate(format(pa[6],'.4%'),xy=(6,pa[6]),xytext=(6*0.9,pa[6]*0.9),
             arrowprops = dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
#添加注释，即85%的标记。这里包括了指定箭头样式。
plt.ylabel(u'盈利（比例）')
plt.show()



