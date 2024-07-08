import pandas as pd

df = pd.read_excel('record.xls',sheet_name=3)

q_description = df.columns[0]
print(f"Question Description: {q_description}")

titles = df.iloc[0,:]
print(titles)

print("titles: ",titles.tolist())
titles = ['user_id','user_name','submission_id','submission_time','result','code']
df = df.iloc[1:,:]
df.columns = titles
print('Type of results: ',df['result'].unique())
WA_samples = df[df['result']=='WA']['code'].tolist()
print("WA sample",WA_samples[0])
