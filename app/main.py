import utils as ut
import read_csv as rc
import charts as ch

data = rc.read_csv_2('data.csv')

my_countries = ut.extract('Country/Territory',data)
p2022 = ut.extract('2022 Population',data)
p2020 = ut.extract('2020 Population',data)
p2015 = ut.extract('2015 Population',data)
p2010 = ut.extract('2010 Population',data)
p2000 = ut.extract('2000 Population',data)
p1990 = ut.extract('1990 Population',data)
p1980 = ut.extract('1980 Population',data)
p1970 = ut.extract('1970 Population',data)

search = input('Defina el pais a buscar => ')
ci = my_countries.index(search)

labels = ('2022','2020','2015','2010','2000','1990','1980','1970')
values = [int(p2022[ci]),int(p2020[ci]),int(p2015[ci]),int(p2010[ci]),int(p2000[ci]),int(p1990[ci]),int(p1980[ci]),int(p1970[ci])]
print(values)

ch.generate_bar_chart(search,labels,values)

populations = ut.extract('World Population Percentage',data)

ch.generate_pie_chart(my_countries,populations)




