import csv
with open('database.txt', 'rt') as f:
  reader = csv.reader(f, delimiter=' ', skipinitialspace=True)

  lineData = list()

  cols = next(reader)
  # print(cols)

  for col in cols:
    # Create a list in lineData for each column of data.
    lineData.append(list())


  for line in reader:
    for i in range(0, len(lineData)):
      # Copy the data from the line into the correct columns.
      lineData[i].append(line[i])

  data = dict()

  for i in range(0, len(cols)):
    # Create each key in the dict with the data in its column.
    data[cols[i]] = lineData[i]

print(data)