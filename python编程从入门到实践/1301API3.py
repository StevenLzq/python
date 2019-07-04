import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS


url='https://api.github.com/search/repositories?q=language:python&sort=stars'

r=requests.get(url)
print('status code:',r.status_code)#查看网站是否响应

response_dict=r.json()

print('total repositories:',response_dict['total_count'])#打印总的仓库数
repo_dicts=response_dict['items'] #items是一个列表里面存放了很多字典，每个字典是一个仓库信息
names,stars=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style=LS('#333366',base_style=LCS)

my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_size=18
my_config.truncate_label=15#将较长的项目名缩短到15个字符

my_config.show_y_guides=False
my_config.width=1000

char=pygal.Bar(my_config,style=my_style)
char.title='Most_starred python projects om GitHUB'
char.x_labels=names

char.add('',stars)
char.render_to_file('python_repo.svg')

'''
print('repositories returned:',len(repo_dicts))#打印出列表长度查看获得多少个仓库的信息

print('\nselected information about each repository')
for repo_dict in repo_dicts:
    print('\nName:',repo_dict['name'])
    print('owner',repo_dict['owner']['login'])
    print('star',repo_dict['stargazers_count'])
    print('repository',repo_dict['html_url'])
    print('description',repo_dict['description'])

'''