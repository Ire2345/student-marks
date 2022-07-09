import pandas as pd
import statistics 
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean


mean_list=[]

for i in range (0,1000):
    setofmeans=random_set_of_mean(100)
    mean_list.append(setofmeans)

mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)

print(mean)
print(std_deviation)

first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (std_deviation*2), mean + (std_deviation*2)
third_std_deviation_start, third_std_deviation_end = mean - (std_deviation*3), mean + (std_deviation*3)

df = pd.read_csv("School_1_Sample.csv")

data=df["Math_score"].tolist()
meanofsample1=statistics.mean(data)
print(meanofsample1)

fig=ff.create_distplot([mean_list],["studentmarks"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample1, meanofsample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

df = pd.read_csv("School_2_Sample.csv")

data2 = df["Math_score"].tolist()
meanofsample2=statistics.mean(data2)
print(meanofsample2)

fig=ff.create_distplot([mean_list],["studentmarks2"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample2,meanofsample2], y=[0,0.17],mode="lines",name="MEAN OF STUDENTS WHO HAS HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3 END"))
fig.show()

zscore1 = (mean - meanofsample1) / std_deviation
print(zscore1)

zscore2= (mean - meanofsample2) / std_deviation
print(zscore2)