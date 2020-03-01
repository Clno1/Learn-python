
import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename="./data/sitka_weather_2018_full.csv";

with open(filename) as f:
    #reader 取得文件中以逗号分隔的第一行数据
    reader=csv.reader(f)
    header_row=next(reader)

    '''
    #利用enumerate取得column的索引
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    '''

    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2], "%Y-%m-%d")  #日期在第二列
        dates.append(current_date)

        high=0
        if row[8]!='':
            high=int(row[8].strip())    #最高温在第8列
        highs.append(high)

        low=0
        if row[9]!='':
            low=int(row[9].strip())
        lows.append(low)

    #传入数据 以绘制图形
    fig=plt.figure(dpi=128,figsize=(10,6))
    # Alpha 值为 0 表示折线完全透明,1（默认设置）表示完全不透明
    plt.plot(dates,highs,c='red',alpha=0.5)   #把dates加入这里以显示x轴
    plt.plot(dates,lows,c='blue',alpha=0.5)   #再加一个plt.plot就能加多一条折线图
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.2)

    #设置图形样式
    plt.title("Daily weather",fontsize=24);
    plt.xlabel("",fontsize=16)
    fig.autofmt_xdate()     #调整x轴标签以不重叠
    plt.ylabel("Temperature",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()
