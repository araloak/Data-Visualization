import numpy as np
from matplotlib import pyplot as plt

# 以下两行用于支持中文字符在图中的显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#fig为画板对象，axes为一个2*2的坐标系对象
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(10,10)) 
for i, ax in enumerate(axes.flat): #轮流对每个子图进行操作,属于每个子图的内容和需要进行的操作必须在轮到该子图时才可以进行。
    if i==2:
        x_label=['1','2','3','4','5','6','7','8','9','10']
        x_label_modified=['a','b','c','d','e','f','g','h','i','j']
        y_data=[1044, 4114, 696, 736, 1053, 85, 0, 676, 565, 397]
        '''
        调用bar()函数编辑柱状图:
        x定义横坐标标签
        height定义纵向每个bar的高度
        label保存的字符串用于显示图例
        alpha定义透明度（alpha=1完全不透明）
        width定义每个bar的宽度

        '''
        ax.bar(x = x_label, height = y_data, label="注释数量", color="indianred", alpha=0.8, width=0.3)
        '''
        以下两段语句中任意一段用于对每个bar进行标注
        y_index表示标注的水平位置（传入横坐标列表即可）
        y+10表示在y数据向上10个单位的高度，表示竖直距离
        ha表示标注字符串与x刻度的对齐方式
        va表示标注字符串与y刻度的对齐方式
        '''

        '''
        for y_index,y in zip(x_label,y_data):
            plt.text(y_index,y+10,'%d'% y,ha='center',va='center')

        for y_index, y in enumerate(y_data):
            plt.text(y_index, y + 10, '%d' % y, ha='center', va='bottom')
        ''' 
        #plt.xticks()可用于重新定义坐标轴的标签
        #plt.xticks(x_label,x_label_modified)

        #设置横、纵轴的标签
        ax.set_xlabel('组员')
        ax.set_ylabel('注释条数')

        #给ax坐标系（子图）设置标题
        ax.text(0.5,0.5,"贡献统计",ha="center",va="center",size=10,alpha=0.5)
        #表示在figure中显示图例
        ax.legend()

    if i==3:
        x_data = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']
        y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
        y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
        # 绘图
        ax.bar(x=x_data, height=y_data, label='C语言基础', color='steelblue', alpha=0.8)
        ax.bar(x=x_data, height=y_data2, label='Java基础', color='indianred', alpha=0.8)
        # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
        for x, y in enumerate(y_data):
            ax.text(x, y + 100, '%s' % y, ha='center', va='bottom')
        for x, y in enumerate(y_data2):
            ax.text(x, y + 100, '%s' % y, ha='center', va='top')
        # 设置标题
        ax.set_title("Java与Android图书对比")
        # 为两条坐标轴设置名称
        ax.set_xlabel("年份")
        ax.set_ylabel("销量")
        #表示在figure中显示图例
        ax.legend()      

#显示figure(画板)
plt.show()
