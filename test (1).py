nimi = input("Tere! Mis su nimi on? ")  # Küsi kasutaja nime
tunnetus = input(f"{nimi}, kuidas sul läheb? ")  # Küsi, kuidas tal läheb

# Tervita kasutajat
print(f"Tere, {nimi}! Tore, et sa siin oled! Sul läheb: {tunnetus}")

class cal():  #klass nimega cal
    def __init__(self, a, b):  # Konstruktor, mis initsialiseerib objekti, võtma argumente a ja b
        self.a = a  #esimene number objekti attribuudiks
        self.b = b  #teine number objekti attribuudiks

    def liitmine(self):  # funktsioon mille abil saab liitmise teostamiseks
        return self.a + self.b  # Siit saan vastuse a ja b jaoks

    def lahutamine(self):  # lahutamise teostamiseks
        return self.a - self.b  #  Siit saan vastuse a ja b jaoks

    def korrutamine(self):  # korrutamise teostamiseks
        return self.a * self.b  #  Siit saan vastuse a ja b jaoks

    def jagamine(self):  #  jagamise teostamiseks
        return self.a / self.b  #  Siit saan vastuse a ja b jaoks

    def jaak(self):  #  jäägi leidmiseks
        return self.a % self.b  #  Siit saan vastuse a ja b jaoks

    def ruutjuur(self):  # ruutjuure leidmiseks
        return self.a ** self.b  #  Siit saan vastuse a ja b jaoks


# Küsimine kasutajalt esimest numbrit
a = int(input("Sisesta esimene number: "))  # Kasutaja sisestab esimese numbri ja konverteerib selle täisarvuks

# Küsimine kasutajalt teist numbrit
b = int(input("Sisesta teine number: "))  # Kasutaja sisestab teise numbri ja konverteerib selle täisarvuks

kalk = cal(a, b)  # Loome cal klassist objekti 'kalk', kasutades antud a ja b väärtusi

while True:  # Loodud tsükkel, mis jätkub kuni see katkestatakse
    def menu():  # Funktsioon menüü kuvamiseks
        x = (
            '1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine. ')  # Menüü valikud
        print(x)  # Kuvame menüü valikud


    menu()  #menüü funktsioon
    valik = int(input('Sisesta üks valikutest: '))  # Kasutaja sisestab menüüst valiku

    if valik == 1:  # Kontrollib, kas kasutaja valis liitmise
        print("Vastus: ", kalk.liitmine())  # Kuvame liitmise tulemuse
        break  # Katkestame tsükli
    elif valik == 2:  # Kontrollib, kas kasutaja valis lahutamise
        print("Vastus: ", kalk.lahutamine())  # Kuvame lahutamise tulemuse
        break  # Katkestame tsükli
    elif valik == 3:  # Kontrollib, kas kasutaja valis korrutamise
        print("Vastus: ", kalk.korrutamine())  # Kuvame korrutamise tulemuse
        break  # Katkestame tsükli
    elif valik == 4:  # Kontrollib, kas kasutaja valis jagamise
        print("Vastus: ", kalk.jagamine())  # Kuvame jagamise tulemuse
        break  # Katkestame tsükli
    elif valik == 5:  # Kontrollib, kas kasutaja valis jäägi leidmise
        print("Vastus: ", kalk.jaak())  # Kuvame jäägi tulemuse
        break  # Katkestame tsükli
    elif valik == 6:  # Kontrollib, kas kasutaja valis ruutjuure leidmise
        print("Vastus: ", kalk.ruutjuur())  # Kuvame ruutjuure tulemuse, kuigi see on tegelikult astendamine
        break  # Katkestame tsükli
    elif valik == 0:  # Kontrollib, kas kasutaja valis vale valiku
        print('Sisesta uuesti üks liitmise operaator')  # Teavitame kasutajat veast
        break  # Katkestame tsükli


        #https://github.com/indr3kk/mittpangandus/blob/master/test%20(1).py
