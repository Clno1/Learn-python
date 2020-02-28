
import matplotlib.pyplot as plt
#绘制折线图

input_value=[0,1,2,3,4,5]
squares=[0,1,4,9,16,25]
#输入/输出数据，线条粗细
plt.plot(input_value,squares,linewidth=5)

#折线图名字，x轴/y轴 名称字体大小
plt.title("Squares Number",fontsize=25)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#刻度标记大小
plt.tick_params(axis='both',labelsize=14)

plt.show()