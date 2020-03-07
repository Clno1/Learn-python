
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)     #获得url的回复     
print("Status code:", r.status_code)

response_dict=r.json()   #把信息变成json格式
print("Total repositories:", response_dict['total_count'])

repo_dicts=response_dict['items']
print("Repositories returned:", len(repo_dicts))

#把项目名字和stars数存储在两个list中
names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

#把两个list的数据可视化
my_style=LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

'''
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
'''