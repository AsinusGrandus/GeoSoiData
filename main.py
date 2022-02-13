import datetime
import pandas

data = []

with open("soi.txt", "r") as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    linelist = line.split()
    if index != 0:
        for i in range(len(linelist)):
            if i == 0:
                year = int(linelist[i])
            else:
                data.append(
                    [str(datetime.datetime(year, i, 1)), float(linelist[i])])

df = pandas.DataFrame(data, columns=["date", "soi-index"])
df.to_csv("out-soi.txt", "\t", index=False)
