"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 5
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""

#一个对象就是一个物品
class Thing(object):
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight

    @property
    def value(self):
        return self.price/self.weight

def getthing():
    name,price,weight=input().split()
    return Thing(name,int(price),int(weight))

def main():
    m,n=map(int,input().split())
    things=[]
    for _ in range(n):
        things.append(getthing())
    #按性价比大到小排序
    things.sort(key=lambda x:x.value,reverse=True)
    
    now_weight,now_money=0,0
    for i in range(n):
        if (now_weight+things[i].weight<=m):
            now_weight+=things[i].weight
            now_money+=things[i].price

    print("物品总价值：%d" % now_money)
    
if __name__=="__main__":
    main()
