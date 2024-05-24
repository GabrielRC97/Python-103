def get_population():
    keys = ['col','bol']
    values = [300,400]
    return keys, values

def population_by_country (data, country):
    result = list(filter(lambda i:i['Country'] == country, data))
    return result

def extract(info,data):
    extraction = [data[i][info] for i in range(0,len(data))]
    return extraction
