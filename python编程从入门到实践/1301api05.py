
# coding=utf-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# 执行API调用并存储响应
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print("Status code:", r.status_code)
# 将API响应存储在一个变量中
repo_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# 研究有关仓库的信息
repo_dicts = response_dict['items']
print ("Number of items:" ,len(repo_dicts)

names ,plot_dicts =[] ,[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict ={'value' :repo_dict['stargazers_count'],
                   'label' :repo_dict['description'],
                   'xlink' :repo_dict['html_url']
                   }
        plot_dicts.append(plot_dict)
    else:
        plot_dict ={'value' :repo_dict['stargazers_count'],
                   'label' :'ABC',
                   'xlink' :repo_dict['html_url']}
        plot_dicts.append(plot_dict)
# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
print plot_dicts
chart.render_to_file('python_repos.svg')
