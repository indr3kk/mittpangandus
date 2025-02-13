#ALLA KERIDES ON NÄHA MINU KONSPEKTI LINKI!!!
#SEE ON MINU PANGANDUSSÜSTEEMI KOOD


#(Parent Class)
class User():
    def __init__(self, name, age, gender):  # Konstruktor, mis salvestab kasutaja nime, vanuse ja soo
        self.name = name  # Salvestab kasutaja nime
        self.age = age  # Salvestab kasutaja vanuse
        self.gender = gender  # Salvestab kasutaja soo

    def show_details(self):  # Funktsioon, mis kuvab kasutaja andmed
        print("Personal Details")  # Prindib pealkirja
        print("")
        print("Name ", self.name)  # Prindib kasutaja nime
        print("Age  ", self.age)  # Prindib kasutaja vanuse
        print("Gender ", self.gender)  # Prindib kasutaja soo


#(Child Class), mis pärib User klassi omadused
class Bank(User):
    def __init__(self, name, age, gender):  # konstruktor, mis lisaks kasutaja andmetele lisab ka pangakonto
        super().__init__(name, age, gender)  # tuleb välja vanemklassi konstruktor
        self.balance = 0  # Algväärtus pangakontole on 0 eurot

    def deposit(self, amount):  # Funktsioon raha sissemakseks
        self.amount = amount  # Salvestab sissemakstava summa
        self.balance = self.balance + self.amount  # Uuendab kontojääki, lisades sissemakstud summa
        print("Account balance has been updated : €", self.balance)  # Kuvab uue kontojäägi

    def withdraw(self, amount):  # Funktsioon raha väljavõtmiseks
        self.amount = amount  # Salvestab väljavõetava summa
        if self.amount > self.balance:  # Kontrollib, kas kontol on piisavalt raha
            print("Insufficient Euro | Balance Available : €", self.balance)  # Teade, kui raha ei ole piisavalt
        else:
            self.balance = self.balance - self.amount  # Lahutab väljavõetava summa kontojäägist
            print("Account balance has been updated : €", self.balance)  # Kuvab uue kontojäägi

    def view_balance(self):  # Funktsioon, mis näitab kasutaja andmeid ja kontojääki
        self.show_details()  # Kutsub välja kasutaja detailide kuvamise funktsiooni
        print("Account balance: €", self.balance)  # Kuvab kontojäägi



# https://docs.google.com/document/d/1Q8qf_GcopbVahgQjlR5bVVpB4c9sDxmeq0iyKCEPtKY/edit?usp=sharing
# see on link minu konspektile.