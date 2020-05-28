import pandas as  pd
"""
绝对路径(不适用于控制台输入):
path = r'E:\学习\python\code\python数据分析与挖掘实战\第三章\数据集\catering_sale.xls'
如果需要将py文件整体运行,建议采用下边的path
"""
path = r'../数据集/catering_sale.xls'

data = pd.read_excel(path,index_col=u'日期')
#指定列属性'日期'为索引

print(data.describe())

lenth = len(data)#结果有201个,count显示有200个非空值,显然有一个缺失值

import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()#创建一个图像

p = data.boxplot(return_type='dict')
"""
用dataframe自带的函数画箱型图,return_type中返回的参数p
包括了各个标签的信息,如fliers是异常值的标签
boxes：显示四分位数和中位数的置信区间（如果启用的话）（其实就是绕着主体矩形四个顶点环绕一周）
median：每一个box的横隔线
whiskers:  延伸到不大于异常值的点的垂线
caps: 边界线
fliers: 所有的异常值点
means: 代表均值的点或者线
"""
x = p['fliers'][0].get_xdata()#获取异常点的坐标
y = p['fliers'][0].get_ydata()#获取异常点的值
#鉴于x轴坐标一致,不妨对y值进行排序
y.sort()
#用annotate添加注释
#其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制。
#以下参数都是经过调试的，需要具体问题具体调试。
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
plt.show()#展示箱线图

"""
从图中可以看出，箱型图中的超过上下界的7个销售额数据可能为异常值。
结合具体业务可以把865、4060.3、4065.2归为正常值，将22、51、60、6607.4、9106.44归为异常值。
最后确定过滤规则为：日销量在400以下5000以上则属于异常数据，编写过滤程序，进行后续处理。
"""
data = data[(data>400) & (data<5000)]#筛选
data = data.dropna()#去掉空值





