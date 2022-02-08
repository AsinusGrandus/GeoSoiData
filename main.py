import json

data = {
    "ANOMALY": {},
    "STANDARDIZED DATA": {}
}

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

with open('soi.txt', 'r') as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    linelist = line.split()

    type = "ANOMALY" if index <= round(len(lines)/2) else "STANDARDIZED DATA"

    if len(linelist) == 13 and not "YEAR" in linelist:
        for i in range(0,12):
            data[type][f"{linelist[0]}-{months[i]}"] = float(linelist[i+1])