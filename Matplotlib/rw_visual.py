
import matplotlib.pyplot as plt

from RandomWalk import RandomWalk

def main():
    while True:
        rw=RandomWalk(50000)
        rw.fill_walk()

        #设置画布的尺寸
        #plt.figure(dpi=128,figsize=(10,6))

        #通过映射使得往后的点颜色越深
        point_numbers=list(range(rw.num_point))
        plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
                    cmap=plt.cm.Blues,edgecolor='none',s=3)
        #把起点/终点再画一次以突出起点/终点
        plt.scatter(rw.x_values[0],rw.y_values[0],c='green',edgecolors='none',s=10)
        plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

        #隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running=input('Make another walk? (y/n)')
        if keep_running=='n':
            break

if __name__=="__main__":
    main()