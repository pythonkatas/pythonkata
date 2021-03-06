# -*- coding: utf-8 -*
''' Add and Search products in a file '''

# Zero Function - Add Product to file:
def add_products_to_file(n):
  '''
  Input: n - number of products
  Return: file with products
  '''
  new_file = open('data.txt', 'w')

  for i in range(n):
    # make product properties:
    product = str(input('Название продукта: '))
    country = str(input('Страна продукта: '))
    value = input('Объем продукта: ')
    # add product properties to list:
    list_of_product = [product, country, value]
    # convert list to string:
    string_of_product = ' '.join(list_of_product)
    # add product to file
    print(string_of_product, file=new_file)

  new_file.close()

  return 'data.txt'

'''

HERE: Python Katas 3 ( Python Median level)

'''

# file variable:
number_of_product = int(input('Введите количество товаров, которые надо записать:'))
data_file = add_products_to_file(number_of_product)

'''

HERE: Python Katas 3 ( Python Median level)

'''
