import pandas as pd
import matplotlib.pyplot as plt

confrimed = pd.read_csv("C:/Users/mmm/Desktop/pythonProject1/time_series_covid19_confirmed_global.csv")
deaths = pd.read_csv("C:/Users/mmm/Desktop/pythonProject1/time_series_covid19_deaths_global.csv")
recovered = pd.read_csv("C:/Users/mmm/Desktop/pythonProject1/time_series_covid19_recovered_global.csv")

confrimed = confrimed.drop(["Province/State","Lat","Long"],axis=1)
deaths = deaths.drop(["Province/State","Lat","Long"],axis=1)
recovered = recovered.drop(["Province/State","Lat","Long"],axis=1)

confrimed = confrimed.groupby(confrimed["Country/Region"]).aggregate("sum")
deaths = deaths.groupby(deaths["Country/Region"]).aggregate("sum")
recovered = recovered.groupby(recovered["Country/Region"]).aggregate("sum")

confrimed =confrimed.T
deaths=deaths.T
recovered = recovered.T

new_cases=confrimed.copy()
for day in range(1,len(confrimed)):
    new_cases.iloc[day]=confrimed.iloc[day]-confrimed.iloc[day - 1]

growth_rate=confrimed.copy()
for day in range(1,len(confrimed)):
    growth_rate.iloc[day]=(new_cases.iloc[day] / confrimed.iloc[day - 1]) * 100

active_acses=confrimed.copy()
for day in range(0,len(confrimed)):
    active_acses.iloc[day] = confrimed.iloc[day] - deaths.iloc[day] - recovered.iloc[day]

overal_growth_rate=confrimed.copy()
for day in range(1,len(confrimed)):
    overal_growth_rate.iloc[day] = ((active_acses.iloc[day] -  active_acses.iloc[day - 1]) / active_acses.iloc[day - 1])* 100

death_rate=confrimed.copy()
for day in range(0,len(confrimed)):
    death_rate.iloc[day] = (deaths.iloc[day] / confrimed.iloc[day]) * 100

hopitalization_rate_estimte=0.05
hopitalization_needed=confrimed.copy()
for day in range(1,len(confrimed)):
    hopitalization_needed.iloc[day] = active_acses.iloc[day] * hopitalization_rate_estimte



countries=["Italy","Austria","US","China","India","France","Spain","Iran"]
for country  in countries:
    ax = plt.subplot()
    ax.set_facecolor("black")
    ax.figure.set_facecolor("#121212")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.set_title(f"Covid-19 - Total Deaths Cases {country}", color="white")
    death_rate[country].plot.bar()
    plt.show()









