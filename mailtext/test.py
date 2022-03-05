a = ['150203199411250316,150403199912301020,150403196411241011']
b = ','.join(i for i in a)
a = b.split(",")
for i in a:
    print(i)
