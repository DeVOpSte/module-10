import matplotlib.pyplot as stc


fig, ax = stc.subplots()

data = {
    "ExxonMobil": 87.52,
    "Apple": 175.28,
    "Microsoft": 88.08,
    "General Electric": 18.76,
    "IBM":163.14,
    "Altria":69.61,
    "Johnson & Johnson":145.76,
    "General Motors": 0.0,
    "Cheveron":133.60,
    "Walmart":100.87
}

x_data_data = data.keys()
y_data_data = data.values()

ax.bar(x_data_data,y_data_data)

ax.set(ylim = [0,200],
       ylabel = "Cost ($)",
       xlabel = "Company",
       title = "Highest lifetime profit stocks (1926-2016)"
       )

stc.show()

