from queue import Queue,PriorityQueue

# 使用heapq实现优先队列
#定义一个可比较对象
class pqueue:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __lt__(self, other):        #定义了<，像C++的重载<运算符
        return self.x<other.x


def main():
    pq = PriorityQueue()
    while 1:
        opt=int(input())
        if opt==0:      #输入0，结束测试
            break
        if opt==1:      #输入1，输入数字对
            x,y=map(int,input().split())
            pq.put(pqueue(x,y))	#插入数据
        if opt==2:      #输入2，输出优先队列队头
            tmp=pq.get()
            print(tmp.x,tmp.y)	#提取队头


if __name__=="__main__":
    main()