import math
import pandas


def calculator(excel_path, price_index):
    df = pandas.read_excel(excel_path)

    x = float(df['Price'][price_index])
    y = float(input('Enter the value of y: '))

    result = round(math.pow(x/y, 2))
    return result