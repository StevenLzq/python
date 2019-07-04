import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename='sitka_weather_2014.csv'

with open (filename)as f:
    reader=csv.reader(f)
    header_row=next(reader)


    dates,highs,lows=[],[],[]
    for row in reader:#遍历每行
        current_date=datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(current_date)

        high=int(row[1])
        highs.append(high)

        low=int(row[3])
        lows.append(low)

    print(highs)

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#fill_between()ta接受一个x值和两个y值并填充之间的区域


#设置图形格式
plt.title('Daily high and low tempratures, 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制斜置日期防止重叠-
plt.ylabel('temperature(f)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()