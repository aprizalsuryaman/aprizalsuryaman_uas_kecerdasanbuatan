from sklearn import tree

#datasets
#cuaca = 0 is cerah, 1 is mendung, 2 is hujan
#temperature = 0 is panas, 1 is ringan, 2 is dingin
#kelembaban = 0 is tinggi, 1 is normal
#isaprizalsuryaman? 0 false : 1 true
#cuaca            #temperature        #kelembaban       #aprizalsuryaman
x = [
    [0,                 0,                  0,              0],
    [0,                 0,                  0,              1],
    [1,                 0,                  0,              0],
    [2,                 1,                  0,              0],
    [2,                 2,                  1,              0],
    [2,                 2,                  1,              1],
    [1,                 2,                  1,              1],
    [0,                 1,                  0,              0],
    [0,                 2,                  1,              0],
    [2,                 1,                  1,              0],
    [0,                 1,                  1,              1],
    [1,                 1,                  0,              1],
    [1,                 0,                  1,              0],
    [2,                 1,                  0,              1]
]
y = [0, 0, 1, 1, 1, 0, 1, 0, 1,1,1,1,1,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


def prog() :
    cuaca = int(input("cuaca? (0 is cerah, 1 mendung, 2 hujan) : "))
    kelembaban = int(input("Temperature? (0 is panas, 1 is ringan, 2 is dingin) : "))
    temp = int(input("kelembaban? (0 is tinggi, 1 is normal) : "))
    isaprizalsuryaman = int(input("Is aprizalsuryaman? 0 false, 1 true : " ))
if clf.predict([[cuaca, kelembaban, temp, isaprizalsuryaman]]):
        print("\nSaya akan berangkat bermain bola")
    else:
        print("\nMales bermain bola")


prog()
