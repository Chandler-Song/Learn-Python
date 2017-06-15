#--coding:utf-8--

import matplotlib.pyplot as  plt

year = [1970,1980,1990,2000,2010]
population =[1.0,1.262,1.650]+[3.789,5.301,8.902,9.405,9.533]
newYear = [1940,1950,1960] + year
# plt.plot(newYear,population)
plt.fill_between(newYear,population,0,color='green')

#横轴
plt.xlabel('Year')
#纵轴
plt.ylabel('Population')
#标题
plt.title('World Population Projections')
#刻度 万亿作为单位
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

plt.show()