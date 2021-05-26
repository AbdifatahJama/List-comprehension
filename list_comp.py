a = ['hello' + " " + str(i) for i in range(1,5)] # [exp for i in range(a,b)]

print(a)

# List of squares first 100 positvie intergers

sqaure = [i**2 for i in range(1,101)]
print(sqaure)

# Remainders of squares

sqaureRem = [i**2 %5 for i in range(1,101)]
print(sqaureRem)

sqaureRem11 = [i**2%11 for i in range(1,101)]
print(sqaureRem11)

movieTitles = ['The Shawshank Redemption','The Godfather','The Godfather: Part II','The Dark Knight','12 Angry Men','Schindlers List','The Lord of the Rings: The Return of the King','Pulp Fiction']

gtitles = [i for i in movieTitles if i.startswith('P') and i.endswith('n')]
print(gtitles)

movieandDates = [('The Shawshank Redemption',1994),('The Godfather',1972),('The Godfather: Part II',1974),('The Dark Knight',2008),('12 Angry Men',1957),('Schindlers List',1993),('The Lord of the Rings: The Return of the King',2003),('Pulp Fiction',1994)]

before2000 = [i[0] for i in movieandDates if i[1]<2000 ]
print(before2000)

after2000 = [i[0] for i in movieandDates if i[1]>2000]
print(after2000)

randomlistof100intergers = [i for i in range(1,100)]
print(randomlistof100intergers)

by3 = [i*3 for i in randomlistof100intergers]
print(by3)

a = [1,2,3,4,5,6,7,8,9,10]
b = [2,4,6,8,10,12,14,16,18,20]
print('---------------')
cartesianProduct = [(i,j) for i in a for j in b]
print(cartesianProduct)







