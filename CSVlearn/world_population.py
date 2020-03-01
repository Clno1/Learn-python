
import json
from pygal.maps.world import COUNTRIES
import pygal_maps_world.maps
from pygal.style import RotateStyle,LightColorizedStyle

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code

def main():
    filename='./data/population.json'
    with open(filename) as f:
        pop_data=json.load(f)

    #JSON每个元素都是一个字典，我们将每个字典依次存储在 pop_dict中
    cc_population={}
    for pop_dict in pop_data:
        if pop_dict['Year']==2000:
            country_name=pop_dict['Country Name']
            population = int(pop_dict['Value'])
            code=get_country_code(country_name)
            if code:
                cc_population[code]=population

    #根据人数把国家进行分类
    cc_pops1,cc_pops2,cc_pops3={},{},{}
    for cc,pop in cc_population.items():
        if pop<10000000:
            cc_pops1[cc]=pop
        elif pop<100000000:
            cc_pops2[cc]=pop
        else:
            cc_pops3[cc]=pop

    #把分组结果打印出来看看
    print(len(cc_pops1),len(cc_pops2),len(cc_pops3))

    wm=pygal_maps_world.maps.World()
    wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)       #用一个16进制数表示颜色
    wm = pygal_maps_world.maps.World(style=wm_style)     #设置颜色:淡蓝色基色
    wm.title="World Population in 2000, by country."

    wm.add('0-10m',cc_pops1)
    wm.add('10m-1bn',cc_pops2)
    wm.add('>1bn',cc_pops3)

    wm.render_to_file("World_population.svg")

if __name__=="__main__":
    main()