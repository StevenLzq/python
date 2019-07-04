import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename='sitka_weather_07-2014.csv'

with open (filename)as f:
    reader=csv.reader(f)
    header_row=next(reader)


    dates,highs=[],[]
    for row in reader:#遍历每行
        current_date=datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)

    print(highs)

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')


#设置图形格式
plt.title('daily high tempratures,july 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制斜置日期防止重叠-
plt.ylabel('temperature(f)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()