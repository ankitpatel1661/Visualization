import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#%matplotlib inline
plt.style.use('fivethirtyeight')

df =pd.read_csv(r"dataset\countries-aggregated.csv", parse_dates=['Date'])
df["Total cases"] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
# Worldwide cases

worldwide_df = df.groupby(['Date']).sum()
w = worldwide_df.plot(figsize = (160,5))
w.set_xlabel("Date")
w.set_ylabel('# of cases worldwide')
w.title.set_text('Worldwide COVID Insight')

plt.show()

#USA vs Woorldwide
ind_df=df[df['Country']=='US'].groupby(['Date']).sum()

fig= plt.figure(figsize=(12,5))
ax=fig.add_subplot(111)

ax.plot(worldwide_df[['Total Cases']], label='Worldwide')
ax.plot(ind_df[['Total Cases']], lable='India')
ax.set_xlabel("Date")
ax.set_ylabel('# of Total Cases')
ax.title.set_text('Worldwide vs. India Total Cases')

plt.legend(loc='upper left')
plt.show()