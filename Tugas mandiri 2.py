datalist1 = ['red', 'green', 'blue']
datalist2 = ['#FF0000','#008000','#0000FF']
d = dict()
for key, value in zip(datalist1, datalist2):
    d[key] = value
print(d)