from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# 以下两行用于支持中文字符在图中的显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


#fig为画板对象，ax为大小为1*1的的坐标系对象
fig,ax=plt.subplots(figsize=(10,10))

#设置随机数种子
np.random.seed (10)

#在0-100（不包括100）整数范围内随机选择数字组成100*2矩阵
a=np.random.choice(100,size=(100,2),replace=True)

#获取矩阵第一列作为横坐标
x=list(x[0] for x in a)
#获取矩阵第二列作为纵坐标
y=list(x[1] for x in a)

'''
label用于定义图例中的显示
marker定义散点形状。（详见parameter.txt文档）
s定义散点的大小
color（详见parameter.txt文档）

'''
#显示第一类样本
ax.scatter(x[0:50],y[0:50],label='first class', marker = '+', s = 25,color='r',alpha=0.8)
#显示第二类样本
ax.scatter(x[50:100],y[50:100],label='second class', marker = 'o', s = 25,color='b',alpha=0.8) 

#用于在每个点处标注该点的坐标信息
'''
for x, y in zip(x1, y1):
    plt.annotate('(%s,%s)'%(x,y), xy=(x,y),xytext = (0, -10), textcoords = 'offset points',ha = 'center', va = 'top')
'''
ax.set_xlabel('第一维属性取值') 
ax.set_ylabel('第二维属性取值') 
ax.set_title('二维特征样本在特征空间内分布')

#loc定义图例的位置,有多种取值。（详见parameter.txt文档）
ax.legend(loc="upper left")

#保存图片，一定放在plt.show()之前
plt.savefig('./scatter_graph_format.png')

plt.show()
