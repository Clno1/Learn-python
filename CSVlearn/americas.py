
import pygal
import pygal_maps_world.maps

def main():
    #创建了一个 Worldmap 实例，并设置了该地图的的 title 属性
    wm=pygal_maps_world.maps.World()
    wm.title="North, Central, and South America"

    #方法 add() ，它接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码
    wm.add('North America', ['ca', 'mx', 'us'])
    wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
    wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])

    #创建一个包含该图表的 .svg 文件
    wm.render_to_file('americas.svg')

if __name__=="__main__":
    main()