
from random import choice

""" 一个生成随机漫步数据的类 """
class RandomWalk():
    def __init__(self,num_point=5000):
        self.num_point=num_point

        #漫步开始于(0,0)
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        while len(self.x_values)<self.num_point:
            #随机生成x走的方向/距离
            x_direction=choice([-1,1])
            x_distance =choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            #随机生成y走的方向/距离
            y_direction=choice([-1,1])
            y_distance =choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            if x_step==0 and y_step==0:
                continue

            #计算出下一步x/y的位置
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
