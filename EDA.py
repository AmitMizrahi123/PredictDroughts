import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from data.utilities import returnStates

states = returnStates()
df = pd.read_csv('files/merge.csv')
df['Week'] = pd.to_datetime(df['Week'], infer_datetime_format=True)

# df.LEVEL.value_counts().head(5).plot(kind='bar', color='blue', alpha=0.5)
# plt.xlabel('LEVEL')
# plt.ylabel('COUNT')
# plt.title('Drought hist level count')
# plt.show()

# dfLevelD0 = df[df['LEVEL'] == 0].reset_index(drop=True)
# dfLevelD1 = df[df['LEVEL'] == 1].reset_index(drop=True)
# dfLevelD2 = df[df['LEVEL'] == 2].reset_index(drop=True)
# dfLevelD3 = df[df['LEVEL'] == 3].reset_index(drop=True)
# dfLevelD4 = df[df['LEVEL'] == 4].reset_index(drop=True)
# sizes = [len(dfLevelD0), len(dfLevelD1), len(dfLevelD2), len(dfLevelD3), len(dfLevelD4)]
# labels = ['DO', 'D1', 'D2', 'D3', 'D4']
# explode = (0.05, 0.05, 0.05, 0.05, 0.05)
# fig, ax = plt.subplots()
# ax.pie(sizes,explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=180)
# ax.legend(bbox_to_anchor=(1.0, .5), prop={'size': 12})
# plt.title('Total Drought Hist Level Count')
# plt.show()

# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(df.Latitude, df.Longitude)
# plt.show()

# fig = plt.figure()
# ax = plt.axes()
# ax.scatter(df.Latitude, df.Longitude)
# ax.scatter(df.Latitude[df.LEVEL == 0], df.Longitude[df.LEVEL == 0], c='red')
# ax.scatter(df.Latitude[df.LEVEL == 1], df.Longitude[df.LEVEL == 1], c='green')
# ax.scatter(df.Latitude[df.LEVEL == 2], df.Longitude[df.LEVEL == 2], c='yellow')
# ax.scatter(df.Latitude[df.LEVEL == 3], df.Longitude[df.LEVEL == 3], c='black')
# ax.scatter(df.Latitude[df.LEVEL == 4], df.Longitude[df.LEVEL == 4], c='pink')
# plt.title('The most droughts that ever happened')
# plt.xlabel('Latitude')
# plt.ylabel('Longitude')
# ax.legend(bbox_to_anchor=(1.0, .5), prop={'size': 12})
# plt.show()

# stateLevel4 = df.State[df['LEVEL'] == 4]
# wc = WordCloud(width=800, height=400, max_words=200,).generate_from_frequencies(stateLevel4.value_counts())
# plt.figure(figsize=(7, 7))
# plt.imshow(wc, interpolation='bilinear')
# plt.axis('off')
# plt.show()

# ct = pd.crosstab(df['Week'].dt.year, df['LEVEL'])
# ct.plot.bar(stacked=True)
# plt.legend(title='Level')
# plt.show()

# pd.crosstab(df['Week'].dt.year, df['LEVEL']).plot(linewidth=1, grid=True)
# plt.title('Crosstabed Pandas DataFrame by year and level')
# plt.legend(loc=1, fontsize = 'small', title='Categories')
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.show()

sns.boxplot(df['LEVEL'])
plt.show()