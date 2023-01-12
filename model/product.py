import csv

product_data = []
product_header = []


def createList():
    global product_header
    global product_data
    file = open("database/product.csv")
    reader = csv.reader(file)
    product_header = next(reader)

    rows = []
    for row in reader:
        rows.append(row)

    if len(product_data) <= 0:
        product_data = rows

    return product_data


createList()


def transform(data):
    result = {}
    for i in range(len(product_header)):
        header = product_header[i]
        value = data[i]
        if header == 'price':
            value = float(data[i])

        result[header] = value

    return result


def search(code):
    for i in range(len(product_data)):
        if product_data[i][0] == code:
            return transform(product_data[i])
    return None


if __name__ == '__main__':
    # for testing purpose
    print(product_data)
    print(search('test02'))
