# #Задание №1
# def list_reorder(rl):
#     a1 = rl[0]    #Принимается стартовые значения
#     surnames = rl[1] #
#     new = []
#     for i in a1:
#      a = []
#     a.append(i)                        #
#     a.append(surnames[a1.index(i)]) # Условия
#     new.append(a)                      #
#     return new
# #Задание №2
# def del_rep(num):
#  num.sort()
#  num = list(set(num))   #Функция "set" исключает все совпадения, а "sort" сортирует по возрастанию
#  return num
# #Задание №3
# def lim_max(nums, limit):
#     a = -1
#     for i in nums:
#         if i < limit and i > a:   #Строка задает лимиты
#             a = i
#             return a #Возвращает к изначальному этапу
# #Задание №4
# temp = int(input("Введите градусную меру: "))
# if temp < 0 and temp > -25:
#     print("Холодно")
# elif temp < 0 and temp > -20:
#     print("Прохладно")
# if temp < 15 and temp > 0:    #Условия ищут соответствия с задаными параметрами в инпуте
#     print("Зябко")
# elif temp > 15 and temp < 25:
#     print("Тепло")
# if temp > 25:
#     print("Жарко")
# #Задание №5
# def main(stra: str):
#     stra = ''.join(stra.split())                                                               #
#     c1 = stra.startswith('+7') or stra.startswith('8')                                         #
#     c2 = all(stra.split('-'))                                                                  #
#     c3 = (stra.count('(') == 1 and stra.count(')') == 1 and stra.find('(') < stra.find(')'))   #Условия
#     c4 = stra.count('(') == 0 and stra.count(')') == 0                                         #
#     if c1 and c2 and (c3 or c4):                                                               #
#         for c in '()-': stra = stra.replace(c, '')                                             #







