import json
import pygal_maps_world.maps
from country_codes import get_country_code


filename='population_data.json'
with open(filename)as f:
    pop_data=json.load(f)

cc_populations={}
#建立这样一个空字典用来把code 和population对应
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        #找到国家和人口对应位置

        code=get_country_code(country)
        #code和国家对应关系
        if code:
            cc_populations[code]=population
            #code和人口关系

#遍历一遍，把所有code和人口对应0

wm = pygal_maps_world.maps.World()
wm.title='world population in 2010,by country'

wm.add('2010',cc_populations)
wm.render_to_file('world_population.svg')

'''
wm = pygal_maps_world.maps.World()
wm.title='population of countries in North America'

#wm.add('North America',['ca','mx','us'])
#wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
#wm.add("South America",['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])


wm.add('North America',{'ca':34126000,'us':309349000,'mx':113423000})
wm.render_to_file('na_population.svg')
'''
