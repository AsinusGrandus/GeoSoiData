import datetime
import pandas as pd

data = []
c = "soi"

with open(f"{c}.txt", "r") as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    linelist = line.split()
    if index != 0:
        for i in range(len(linelist)):
            if i == 0:
                year = int(linelist[i])
            else:
                data.append(
                    [datetime.datetime(year, i, 1), float(linelist[i])])

df = pd.DataFrame(data, columns=["date", f"{c}-index"])
df["MA-6"] = df[f"{c}-index"].rolling(window=6).mean()
df["MA-12"] = df[f"{c}-index"].rolling(window=12).mean()
df.to_csv(f"out-{c}.txt", "\t", index=False)
