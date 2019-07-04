from die import Die
import pygal
die1=Die()
die2=Die(10)

results=[]
for roll_num in range(50000):
    result=die1.roll()+die2.roll()
    results.append(result)

#结果分析
frequencies=[]
for value in range(2,17):
    frequency=results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

#绘制直方图
hist=pygal.Bar()

hist.title='result of rolling D6 and D10 50000 times'
list=[]
for i in range(1,16):
    num=i+1
    list.append(num)

hist.x_labels=list
hist.x_title='Result'
hist.y_title='Frequency of result'

hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual2.svg')
