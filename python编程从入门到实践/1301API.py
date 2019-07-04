import requests

url='https://api.github.com/search/repositories?q=language:python&sort=stars'

r=requests.get(url)
print('status code:',r.status_code)#查看网站是否响应

response_dict=r.json()

print('total repositories:',response_dict['total_count'])#打印总的仓库数
repo_dicts=response_dict['items'] #items是一个列表里面存放了很多字典，每个字典是一个仓库信息
print('repositories returned:',len(repo_dicts))#打印出列表长度查看获得多少个仓库的信息


repo_dict=repo_dicts[0]#查看第一个仓库
'''
便利第一个仓库，查看这个仓库包含多少键值对，并把他们的键打印出来方便寻找需要的信息

print('\n keys:' ,len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
'''
print('\nselected information about first repositories')
print('Name:',repo_dict['name'])
print('Owner:',repo_dict['owner']['login'])
print('Star:',repo_dict['stargazers_count'])
print('repository:',repo_dict['html_url'])
print('created:',repo_dict['created_at'])
print('update:',repo_dict['updated-at'])
print('description:',repo_dict['description'])

