import numpy as np
from matplotlib import pyplot as plt

# 以下两行用于支持中文字符在图中的显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#fig为画板对象，ax为大小为1*1的的坐标系对象
fig,ax=plt.subplots(figsize=(10,10)) 
x_label=['1','2','3','4','5','6','7','8','9','10']
y_data=[1044, 4114, 696, 736, 1053, 85, 0, 676, 565, 397]
color=['red', 'orange', 'yellow', 'green', 'blue', 'gray', 'goldenrod','black','indianred','steelblue']
explode=[0,0.5,0,0,0,0,0,0,0,0]
'''
调用pie()函数编辑柱状图:
autopct计算并在图中每一个扇形中展示其所占百分比
color列表保存自定义的每个数据需要的颜色（也可不传入该参数，使用默认设置）
explode列表表示如果将某一扇形分割出来，数越大，分割距离越大
如果有分隔开来的扇形，shadow定义为True可以在边缘显示阴影，有立体感
startangle =90, #逆时针起始角度设置
pctdistance = 0.6 #扇形上显示的数值距圆心半径倍数的距离

'''
ax.pie(y_data,labels=x_label,explode=explode,colors=color,shadow=True,autopct='%1.1f%%',startangle =90,pctdistance = 0.6) 

'''
给ax坐标系（子图）添加文字,(x,y)坐标系原点在圆心；默认圆的半径为单位1；
ax.text(0,1.5,"贡献统计",ha="center",va="center",size=10,alpha=0.5)
'''
#给ax坐标系（子图）设置标题更简单的方法:
ax.set_title("贡献统计")
        
'''
legend()表示在figure中显示图例:
bbox_to_anchor定义图例显示的位置,x,y范围一般在[0,1]当中，否则会离开当前子图的范围
 
 '''
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')

#显示图例，bbox_to_anchor表示图例在该坐标系中的位置x,y属于[0,1]。
ax.legend(bbox_to_anchor=(0, 0.5))

#保存图片，一定放在plt.show()之前
plt.savefig('pie_chart_format.png') 

#显示figure(画板)
plt.show()
