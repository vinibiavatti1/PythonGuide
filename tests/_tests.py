

lst = [i for i in range(10000)]
gen = (i for i in range(10000))
print(lst.__sizeof__())
print(gen.__sizeof__())
