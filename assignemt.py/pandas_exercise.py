#1
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]}
df = pd.DataFrame(data)
print(df)

#2
df = pd.read_csv('filename.csv')
print(df)

#3
print(df.head())

#4
print(df.tail())

#5
# loc[] is label-based; iloc[] is index-based.

#6
print(df['column_name'])

#7
print(df[['col1', 'col2']])

#8
print(df[df['column_name'] > value])

#9
print(df.isnull())

#10
df.fillna(value, inplace=True)

#11
df.dropna(inplace=True)

#12
df.dropna(axis=1, inplace=True)

#13
df.replace({'old_value': 'new_value'}, inplace=True)

#14
df.rename(columns={'old_name': 'new_name'}, inplace=True)

#15
df['column_name'] = df['column_name'].astype('new_type')

#16
df.drop_duplicates(inplace=True)

#17
df.reset_index(drop=True, inplace=True)

#18
df.set_index('column_name', inplace=True)

#19
df.sort_values('column_name', inplace=True)

#20
df.sort_values(['col1', 'col2'], inplace=True)