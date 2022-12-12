import random
set_1=[]
set_2=[]
for i in range(0,5):
    set_1.append(random.randint(0,10))
    set_2.append(random.randint(0,10))
set_1=set(set_1)
set_2=set(set_2)
print("Первый набор: ",set_1, "Второй набор: ", set_2)
print("Эти числа входят одновременно в оба набора: ", set_1 & set_2)
print("Эти числа входят в первый набор или во второй, но не в оба одновременно: ", set_1 ^ set_2)
print("Эти числа входят только в 1-й набор: ", set_1-set_2)
print("Эти числа входят только в 2-й набор: ", set_2-set_1)
