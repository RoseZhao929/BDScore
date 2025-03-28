import pandas as pd

# df = pd.read_excel('post-idd/model_results/huatuo2_idd_fu_info.xlsx')
# df['predicted_disease'] = df['modeldisease-idd']
# df = df[['id', 'text', 'disease', 'predicted_disease', 'age', 'gender']]
# df.to_excel('post-idd/model_results/huatuo2_result.xlsx',index=False)

df = pd.read_excel('post-idd/model_results/palm2_idd_fu_info.xlsx')
id2serious = dict(zip(df['id'], df['serious']))
id2repeat = dict(zip(df['id'], df['repeat']))
id2drepeat = dict(zip(df['id'], df['d_repeat']))
df = pd.read_excel('post-idd/model_results/medpalm2_result.xlsx')
df['serious'] = ""
df['repeat'] = ""
df['d_repeat'] = ""
for rowid, row in df.iterrows():
    df.at[rowid, 'repeat'] = id2repeat[row['id']]
    df.at[rowid, 'serious'] = id2serious[row['id']]
    df.at[rowid, 'd_repeat'] = id2drepeat[row['id']]
df.to_excel('post-idd/model_results/medpalm2_result.xlsx',index=False)