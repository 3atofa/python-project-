import pandas as p


df = p.DataFrame(p.read_excel("russian.xlsx"))
df.to_csv("ruscs.csv", index=None, header=True)



print(df)