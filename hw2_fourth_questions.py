###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #

import pandas as pd

data = pd.read_csv('covid.csv')

data500 = data[data['Active'] >= 500][data['Active'] < 1000]
data1000 = data[data['Active'] >= 1000][data['Active'] < 5000]
data5000 = data[data['Active'] >= 5000]

dataList = [data500, data1000, data5000]

for x in dataList:
    print(f'Average Confirmed Cases: {x["Confirmed"].mean()}')
    print(f'Average Deaths: {x["Deaths"].mean()}')
    print('Countries in the group:')
    print(x['Country'])