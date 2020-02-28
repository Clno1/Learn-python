
import matplotlib.pyplot as plt

x_values=list(range(0,1001))
y_values=[x**2 for x in x_values]
#c设置点颜色，edgecolors设置点轮廓颜色，s设置了绘制图形时使用的点的尺寸
#plt.scatter(x_values,y_values,c='red',edgecolors='none',s=20)
#plt.scatter(x_values,y_values,c=(0.5,0.5,0.5),edgecolors='none',s=20)

#颜色映射，颜色深浅根据映射数据，下图将y值映射为Blue
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,edgecolor='none', s=20)

#散点图名字，x轴/y轴 名称字体大小
plt.title("Squares Number",fontsize=25)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#刻度标记大小
plt.tick_params(axis='both',labelsize=14)

#plt.show()
#保存图表：保存到py所在目录，以下参数是文件名和裁剪图表周围多余空白
plt.savefig('squares_plot.png', bbox_inches='tight')