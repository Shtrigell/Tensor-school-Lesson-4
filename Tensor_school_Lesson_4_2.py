dictionary_of_colors={"red":(220,20,0),"orange":(255,69,0),"yellow":(255,255,0),"green":(0,128,0),"blue":(0,0,255),"purple":(128,0,128)}
print("Словарь цветов: ")
for key, value in dictionary_of_colors.items():
  print("{0}: {1}".format(key,value))
while True:
    question = input("Если хотите добавить цвет введите 'Да': ")
    if question=="Да":
        dictionary_of_colors[input("Введите название цвета: ")]=tuple(input("Введите его RGB кодировку: "))
    else:
        break
for key, value in dictionary_of_colors.items():
  print("{0}: {1}".format(key,value))