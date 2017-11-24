#Исходные значения
tovar1=50
tovar2=300
tovar3=200
#
# tovar1=213550
# tovar2=234523300
# tovar3=23452345200

sum_discount = 150 #размер скидки

list_tovar = [tovar1,tovar2,tovar3] #берем список товаров, чтоб перебрать все товары, хз как там в пыхе

sum_tovar = sum(list_tovar) #сумма без скидки, поидее это значение исходное!!!

dict_itogo = {} # наверное пихать все в словарь удобней

percent_discout = round(sum_discount/sum_tovar*100,2) #процент скидки по чеку (для печати на чеке) --> 27.27

coefficie_percent_discout = sum_discount/sum_tovar #коэфициент скидки (для расчета) --> 0.2727272727272727

sum_voucher= sum_tovar - sum_discount #итоговая сумма в чеке -->> 400

dict_tovar_discount = {} # здесь будем хранить сумму скидки по каждому товару, если это надо
dict_tovat_new_price = {} # здесь итоговую стоимость по товару

for e,tovar in enumerate(list_tovar): # перебираем товары
    dict_tovar_discount['tovar_'+str(e+1)+'_rub_discount']=round(tovar*coefficie_percent_discout,2) #Записываем размер скидки -->{'tovar_2_rub_discount': 81.82, 'tovar_1_rub_discount': 13.64, 'tovar_3_rub_discount': 54.55}
    dict_itogo['dict_tovar_discount']= dict_tovar_discount # пишем в главный словарь
    dict_tovat_new_price['tovar_' + str(e + 1) + '_new_price'] = tovar - round(tovar * coefficie_percent_discout, 2) #Итоговая стоимость товара -->{'tovar_1_new_price': 36.36, 'tovar_3_new_price': 145.45, 'tovar_2_new_price': 218.18}
    dict_itogo['dict_tovat_new_price'] = dict_tovat_new_price # пишем в главный словарь


if sum(dict_itogo['dict_tovat_new_price'].values()) != sum_voucher: #если сумма товаров со скидкой не ровна исходной итоговой сумме
    # то к последнему товару прибавить разницу
    dict_itogo['dict_tovat_new_price'][max(dict_itogo['dict_tovat_new_price'])] += round(sum(dict_itogo['dict_tovar_discount'].values())- sum_discount, 2)

if sum(dict_itogo['dict_tovat_new_price'].values()) == sum_voucher: #проверям, ровна ли теперь сумма товаров со скидкой с исходной суммой?
    print('ok')

#дальше уже брать из словаря
print((dict_itogo['dict_tovat_new_price']))
#{'tovar_2_new_price': 218.18, 'tovar_1_new_price': 36.36, 'tovar_3_new_price': 145.45999999999998}
# тут питоновский косяк с дробями, нужно подключить модуль для расчетов
print(145.45+0.01) #145.45999999999998 получаеться тоже самое
# в пыхе может он нормально складывает?