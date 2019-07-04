import json
import pygal
from pygal.style import LightColorizedStyle
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

#根据人口数量将所有国家分为三组
cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
for cc, pop in cc_populations.items():
    if pop<10000000:
        cc_pops_1[cc]=pop
    elif pop<1000000000:
        cc_pops_2[cc]=pop
    else:
        cc_pops_3[cc]=pop

wm_style= LightColorizedStyle
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title='world population in 2010,by country'

wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population.svg')