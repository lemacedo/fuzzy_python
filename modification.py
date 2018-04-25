import csv
with open('database.txt', 'rt') as f:
  reader = csv.reader(f, delimiter=' ', skipinitialspace=True)

  lineData = list()


print(lineData)