import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'

r=requests.get(url)
print('status code:',r.status_code)#查看网站是否响应

response_dict=r.json()

print('total repositories:',response_dict['total_count'])#打印总的仓库数
repo_dicts=response_dict['items'] #items是一个列表里面存放了很多字典，每个字典是一个仓库信息
print('repositories returned:',len(repo_dicts))#打印出列表长度查看获得多少个仓库的信息

print('\nselected information about each repository')
for repo_dict in repo_dicts:
    print('\nName:',repo_dict['name'])
    print('owner',repo_dict['owner']['login'])
    print('star',repo_dict['stargazers_count'])
    print('repository',repo_dict['html_url'])
    print('description',repo_dict['description'])