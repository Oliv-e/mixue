import csv

header = []


def getHeader(database_name):
    global header
    file = open(f'database/{database_name}.csv')
    reader = csv.reader(file)
    header = next(reader)
    return header


def createList(database_name):
    global header
    file = open(f'database/{database_name}.csv')
    reader = csv.reader(file)
    header = next(reader)

    rows = []
    for row in reader:
        rows.append(row)

    return rows


def transform(data):
    result = {}
    for i in range(len(header)):
        column = header[i]
        value = data[i]
        if column == 'price':
            value = float(data[i])

        result[column] = value

    return result


def search(database, column, value):
    data = createList(database)
    col_index = header.index(column)

    for i in range(len(data)):
        if data[i][col_index] == value:
            return transform(data[i])

    return None


def insert(database, row):
    # getHeader(database)
    path = f'database/{database}.csv'
    with open(path, 'a', encoding='UTF8', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=header)
        dict_writer.writerow(row)

    return True
