from die import Die
import pygal
die=Die()
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

#结果分析
frequencies=[]
for value in range(1,die.num+1):
    frequency=results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

#绘制直方图
hist=pygal.Bar()

hist.title='result of rolling one D6 1000 times'
hist.xlabels=['1','2','3','4','5','6']
hist.x_title='Result'
hist.y_title='Frequency of result'

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
