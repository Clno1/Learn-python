
import pygal
from die import Die

def main():
    die_1=Die(6)
    die_2=Die(8)

    results=[]
    #掷骰子并保存结果
    for roll_num in range(10000):
        result=die_1.roll()+die_2.roll()
        results.append(result)
    #print(results)

    #分析结果
    frequencics=[]
    for value in range(2,die_1.num_sides+die_2.num_sides+1):
        frequency=results.count(value)
        frequencics.append(frequency)
    #print(frequencics)

    #绘直方图显示结果
    hist=pygal.Bar()

    hist.title="Results of rolling one D6 and one D8."
    hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14']
    hist.x_title='Result'
    hist.y_title='Frequency of Result'

    hist.add('D6+D8',frequencics)
    hist.render_to_file('die_visual.svg')
    

if __name__=="__main__":
    main()