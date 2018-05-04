zaIsplatit = int(input("Koliko zelite novca: "))

novcanicaod5000 = 0
novcanicaod2000 = 0
novcanicaod1000 = 0
novcanicaod500 = 0
novcanicaod200 = 0
novcanicaod100 = 0
novcanicaod50 = 0
novcanicaod20 = 0
novcanicaod10 = 0
novcanicaod5 = 0
novcanicaod2 = 0
novcanicaod1 = 0

while zaIsplatit >= 5000:
    zaIsplatit -= 5000
    novcanicaod5000 += 1
    
while zaIsplatit >= 2000:
    zaIsplatit -= 2000
    novcanicaod2000 += 1
    
while zaIsplatit >= 1000:
    zaIsplatit -= 1000
    novcanicaod1000 += 1
    
while zaIsplatit >= 500:
    zaIsplatit -= 500
    novcanicaod500 += 1
    
while zaIsplatit >= 200:
    zaIsplatit -= 200
    novcanicaod200 += 1
    
while zaIsplatit >= 100:
    zaIsplatit -= 100
    novcanicaod100 += 1
    
while zaIsplatit >= 50:
    zaIsplatit -= 50
    novcanicaod50 += 1
    
while zaIsplatit >= 20:
    zaIsplatit -= 20
    novcanicaod20 += 1
    
while zaIsplatit >= 10:
    zaIsplatit -= 10
    novcanicaod10 += 1
    
while zaIsplatit >= 5:
    zaIsplatit -= 5
    novcanicaod5 += 1
    
while zaIsplatit >= 2:
    zaIsplatit -= 2
    novcanicaod2 += 1
    
while zaIsplatit >= 1:
    zaIsplatit -= 1
    novcanicaod1 += 1

if novcanicaod5000 > 0:
    print("Novcanica od 5000 treba: " + str(novcanicaod5000))
          
if novcanicaod2000 > 0:
    print("Novcanica od 2000 treba: " + str(novcanicaod2000))

if novcanicaod1000 > 0:
    print("Novcanica od 1000 treba: " + str(novcanicaod1000))

if novcanicaod500 > 0:
    print("Novcanica od 500 treba: " + str(novcanicaod500))
          
if novcanicaod200 > 0:
    print("Novcanica od 200 treba: " + str(novcanicaod200))

if novcanicaod100 > 0:
    print("Novcanica od 100 treba: " + str(novcanicaod100))

if novcanicaod50 > 0:
    print("Novcanica od 50 treba: " + str(novcanicaod50))
          
if novcanicaod20 > 0:
    print("Novcanica od 20 treba: " + str(novcanicaod20))

if novcanicaod10 > 0:
    print("Novcanica od 10 treba: " + str(novcanicaod10))

if novcanicaod5 > 0:
    print("Novcanica od 5 treba: " + str(novcanicaod5))
          
if novcanicaod2 > 0:
    print("Novcanica od 2 treba: " + str(novcanicaod2))

if novcanicaod1 > 0:
    print("Novcanica od 1 treba: " + str(novcanicaod1))



    
