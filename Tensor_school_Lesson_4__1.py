import random
basic_list = []
choose_func=input("""Выберите способ создания списка:
1.Заполнение случайными числами
2.Ручной ввод
""")
if (choose_func=="1"):
    for i in range(0,10):
        basic_list.append(random.randint(-10,10))
elif(choose_func=="2"):
    iTrue=1
    i=0
    while iTrue==1:
        basic_list.append(input("Введите значения списка, нажмите x для выхода: "))
        if (basic_list[i]=="x"):
            iTrue=0
            basic_list.remove("x")
        i=i+1
else:
    print("Неизвестная операция")
print("Несортированный список", basic_list)
for i in range(0,len(basic_list)-1):
    for j in range(0,len(basic_list)-1):
        if(basic_list[j]>basic_list[j+1]):
            basic_list[j],basic_list[j+1]=basic_list[j+1], basic_list[j]
print("Сортированный список:", basic_list)
