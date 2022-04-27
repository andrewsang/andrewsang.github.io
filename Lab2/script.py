import pandas as pd
df = pd.read_csv("assets/data.csv")
cont = df[df['text'].str.contains("happy")]
print(cont)
cont.to_csv('out.csv')
#print(df)