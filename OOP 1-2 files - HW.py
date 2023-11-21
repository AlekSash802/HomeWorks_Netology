
from pprint import pprint
#from collections import Counter

def cook_book(name_file='MenuFile.txt'):
  """ Задача №1 
  В файле может быть произвольное количество блюд. 
  Читать список рецептов из этого файла. 
  Соблюдайте кодстайл, разбивайте логику на ф-ции и не используйте глобальных переменных.
  
  book =  {'Омлет':
                [{'prd': 'Яйцо', 'qty': '2', 'mer': 'шт'},
                {'prd': 'Молоко', 'qty': '100', 'mer': 'мл'},
                {'prd': 'Помидор', 'qty': '2', 'mer': 'шт'}],
          'Утка по-пекински':
                [{'prd': 'Утка', 'qty': '1', 'mer': 'шт'}, 
                {'prd': 'Вода', 'qty': '2', 'mer': 'л'}, 
                {'prd': 'Мед', 'qty': '3', 'mer': 'ст.л'}, 
                {'prd': 'Соевый соус', 'qty': '60', 'mer': 'мл'}]
          } 
  
  Функция читает файл с книгой и возвращает словарь 
  со всеми блюдами меню из файла согласно заданию. 
  Файл 'MenuFile.txt' имеет образец формата содержания меню 
  для правильной работы функции и понимания о корректном редактирование файла. 
  Так как файл должен иметь специальную структуру.
  """
  
  menu = []
  book = {}

  with open(name_file, 'r', encoding='utf-8') as file:
    for l in file.readlines():
      l = l.strip()
      if l.isdigit() == True:
        menu.append(int(l))
      elif l.find(' | ') != -1 or l != '':
        menu.append(l.split(' | '))
  ingr = len(menu)
  
  for el in menu:
    if type(el) == list and len(el) == 1:
      menu.append([el[0], menu[menu.index(el) + 1]])
    elif type(el) == list and len(el) == 3:
      menu.append({'prd': el[0], 'qty': el[1], 'mer': el[2]})
  del menu[:ingr]

  for i in menu:
    if type(i) == list:
      num = menu.index(i)
      book[i[0]] = menu[num + 1:num + 1 + i[1]]
  
  menu.clear()
  # print('\nlen(menu) =', len(menu), '\nmenu =', menu)
  return book #, pprint(book), print(book)

def get_shop(dish, pers_count):
   """ Задача №2
   Нужно написать функцию, которая принимает список блюд из cook_book и количество персон 
   get_shop_list_by_dishes(dishes, person_count) 
   На выходе получить словарь с названием ингредиентов и его количества для блюда.
   get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) 
   Должен быть следующий результат: 
   {
    'Картофель': {'measure': 'кг', 'quantity': 2}, 
    'Молоко': {'measure': 'мл', 'quantity': 200}, 
    'Помидор': {'measure': 'шт', 'quantity': 4}, 
    'Сыр гауда': {'measure': 'г', 'quantity': 200}, 
    'Яйцо': {'measure': 'шт', 'quantity': 4}, 
    'Чеснок': {'measure': 'зубч', 'quantity': 6}
    }
    Обратите внимание, что ингредиенты могут повторяться
    """
   
   recp = {}
   for d_key in cook_book():
      if type(pers_count) == int and d_key in dish:
         for igr in cook_book()[d_key]:
            if igr['prd'] not in recp.keys():
               recp.update({
                  igr['prd']: dict(mer=igr['mer'], qty=int(igr['qty']) * pers_count)
                  })
            else:
               recp[igr['prd']]['qty'] += int(igr['qty']) * pers_count
   return print('\n{', *[f"  {': '.join(map(str, v))}  " for v in list(recp.items())], '}', sep='\n')#, pprint(recp), print('\n', recp, '\n{', *recp.items(), '}', sep='\n'), print(f'\n{dish}', *cook_book().keys(), sep='\n')


get_shop(['Запеченный картофель', 'Омлет', 'Фахитос', 'Раг'], 2)
