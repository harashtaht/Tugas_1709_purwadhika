# z = ''
# for item in range(1):
#     for item1 in range(0, item+5):
#         z += ' * '
#     z += '\n'
#     for item2 in range(0, item+4):
#         z += ' * '
#     z += '\n'
#     for item3 in range(0, item+3):
#         z += ' * '
#     z += '\n'
#     for item4 in range(0, item+2):
#         z += ' * '
#     z += '\n'
#     for item5 in range(0, item+1):
#         z += ' * '
#     z += '\n'
# print(z)


# No 2
# z = ''
# for item in range(1):
#     for item1 in range(0, item+5):
#         z += ' * '
#     z += '\n'
#     for item2 in range(0, item+4):
#         z += ' * '
#     z += '\n'
#     for item3 in range(0, item+3):
#         z += ' * '
#     z += '\n'
#     for item4 in range(0, item+2):
#         z += ' * '
#     z += '\n'
#     for item5 in range(0, item+1):
#         z += ' * '
#     z += '\n'
#     for item in range (4):
#         for item1 in range(0, item+2):
#             z += ' * '
#         z += '\n'
# print(z)



# No 3
# for item in range (10,0,-1):
#     a = item * '   '
#     b = (11-item)*' * '
#     c = (10-item)*' * '
#     print (a+b+c)



# No 4
# z = ''
# for item in range (10):
#     for item1 in range (0,item):
#         z += '   '
#     for item2 in range (0, 10-item):
#         z += ' * '
#     for item3 in range (1, 10-item):
#         z += ' * '
#     z += '\n'
# print(z)


# No 5
# z = ''
# for item in range (10):
#     for item2 in range (0, item+4):
#         z += '   '
#     for item3 in range (0, 5-item):
#         z += ' * '
#     for item in range (-6, item+4):
#         z += ' * '
#     for item1 in range (-6, 4-item):
#         z += '   '
#     z += '\n'
# print (z)



# BONUS
bintang = int(input('Masukkan Bintang : '))
y =''
z =''
for item1 in range (bintang,0,-1):
    for a in range (0, item1):
        y += ' * '
    for b in range (0,bintang-item1):
        y += '   '
    for c in range (0, (bintang-1)-item1):
        y += '   '
    for d in range (0,item1-1):
        y += ' * '
    if (item1==bintang):
        y+='   '
    else :
        y+= ' * '
    y += '\n'
for item2 in range (0,(bintang-1)):
    for e in range (0, item2+2):
        z += ' * '
    for f in range (0, (bintang-2)-item2):
        z += '   '
    for g in range (0, (bintang-2)-item2):
        z += '   '
    for h in range (0, item2+1):
        z += ' * '
    if (item2==(bintang-2)):
        z += '   '
    else:
        z += ' * '
    z += '\n'
print (y+z)