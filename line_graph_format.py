from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

# 以下两行用于支持中文字符在图中的显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


#fig为画板对象，ax为大小为1*1的的坐标系对象
fig,ax=plt.subplots(figsize=(10,10))

y1=[10,13,5,40,30,60,70,12,55,25] 
x1=range(0,10) 
x2=range(0,10) 
y2=[5,8,0,30,20,40,50,10,40,15]
'''
linewidth定义线的宽度
linestyle定义折线图线的种类（详见parameter.txt文档）
color定义线颜色。（详见parameter.txt文档）
marker代表在折现节点处添加的记号，有多种取值。（详见parameter.txt文档）
markerfacecolor填充在marker图形中的颜色
markersize是marker大小

'''
ax.plot(x1,y1,label='Frist line',linewidth=3,color='r',marker='s', markerfacecolor='yellow',markersize=12) 
ax.plot(x2,y2,label='第二条折线') 
ax.set_xlabel('Plot Number') 
ax.set_ylabel('Important var') 
ax.set_title('Interesting Graph\nCheck it out')

#loc定义图例的位置,有多种取值。（详见parameter.txt文档）
ax.legend(loc="upper left")

#保存图片，一定放在plt.show()之前
plt.savefig('line_graph_format.png')

plt.show()


