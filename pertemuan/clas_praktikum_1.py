# class Hero:
#     def __init__(self, name, health, attack, armor):
#         self.name = name
#         self.health = health
#         self.attack = attack
#         self.armor = armor

#     def serang(self, lawan):
#         print(f"{self.name} menyerang {lawan.name}")
#         lawan.diserang(self)

#         def diserang(self, lawan):
#             print(f"{self.name} diserang {lawan.name}")
#             self.health -= lawan.attack - self.armor
#             print(f"{self.name} memiliki sisa darah {self.health}")

#     # balmond = Hero("Balmond", 100, 40, 10)
#     # print(balmond.__dict__)
#     # print(balmond.serang())

# balmond = Hero("Balmond", 100, 40, 10)
# Roger = Hero("Roger", 500,20,10)

# print(balmond.name)
# print(Roger.name)

# def name(self):
#     return self._name

# sniper = Hero("Sniper", 100, 15, 5)
# print(sniper.__dict__)
# def armor(self):
#     return self._armor

def _str_(self):

    class Hero():
        def __init__(self, name,Healt,mana,armor,attack,gold, daftar_skill=50):
            self.name = name
            self.healt = Healt
            self.mana = mana
            self.armor = armor
            self.attack = attack

balmond = Hero ("balmond",100,15,4 )
print(balmond)

# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.pemilik = pemilik
#         self.__saldo = saldo # private

#     def tarik_saldo(self, jumlah):
#         if jumlah > self.__saldo:
#             print("Saldo tidak cukup.")
#         elif jumlah <= 0:
#             print("Jumlah penarikan tidak valid.")
#         else:
#             self.__saldo -= jumlah
#             print(f"Berhasil menarik {jumlah}. Sisa saldo: {self.__saldo}")
#     def cek_saldo(self):
#             print(f"Saldo saat ini: {self.__saldo}")

# rekening = RekeningBank("Budi", 100000)
# rekening.tarik_saldo(30000)
# rekening.cek_saldo()
# print(rekening.__saldo)

# class Hero():
#         def __init__(self, name, health, mana, armor, attack, gold, daftar_skill):
#              self.name = name
#              self.health = health
#              self.mana = mana
#              self.armor = armor
#              self.attack = attack
#              self.gold = gold
#              self.inventory = []
#              self._skills = [skill(nama,dmg,mana) for nama,dmg,mana in daftar_skill]

#self = intance method
#cls = class method
#kosong = statik method
# ASOSIASI

# class Shop():
#         def __init__(self,name):
#             self.name = name

#         def proses_pembelian(self,hero,item):
#              if hero.gold >= item.harga:
#                 hero.gold -= item.harga #proses transaksi berhasil
#                 print(f' [{self.name} {hero.name} membeli item {item.name}, harga item{item.harga} ]')
#                 return True
#              print(f'{self.name} Gold {hero.name} tidak cukup untuk membeli {item}')

# class Item:
#         def __init__(self, name,harga, bonus_attack=0, bonus_armor=0):
#             self.name = name
#             self.harga = harga
#             self.bonus_attack = bonus_attack
#             self.bonus_armor = bonus_armor

#         def __str__(self):
#               return (f"item : {self.name} | + ")

#         def beli_item(self,shop,item):#roger
#             if len(self._inventory) >= Hero.MAKS_SLOT:
#                   print(f'slot penuh')
#                   return
#             if shop.proses_pembelian(self, item):
#                 self._inventory.append(item)

#         def cast_skill(self,nomor,lawan):
#              skill = self._skills[nomor-1]
#              if self.mana < skill.mana_cost:
#                   print(f' mana tidak cukup')
#                   return
#              self.mana -= skill.mana_cost
#             lawan.health -= skill.damage
#         print(f'{selft.name} memakai {skill.name} ke {lawan.name} sisa health')

# roger = Hero('roger' ,100,30,4,15,5000)
# bod = Item('bod, 3200,350,0')
# shop = Shop('shop')
# #print(roger.__dict__)
# #print(roger.name)
# class Skill():
#      def __init__(self,name,damage,mana_cost):
#         self.name = name
#         self.damage = damage
#         self.mana_cost = mana_cost

class Hero():
    def __init__(self, name, heakth, attack, armor, mana=50): # -> hero
        self.name = name
        self.health = self.health
        self.attack = attack
        self.armor = armor
        self.mana = mana

    def __str__(): #magic method
        return f'nama hero {self.name}'

    def diserang(self,jumlah):
        self._health = max(self._health - jumlah,0) # 0 = agar tidak mines

    def serang(self,target):
        damage = max(self.attack - target.armor ,0)
        target.diserang(damage)
        print(f'{self.name} menyerang {target.name}, damage {damage}')

class Marksman(Hero):
    def __init__(self, name, heakth, attack, armor, mana=50, missChance=50):
        super().__init__(name, heakth, attack, armor, mana=50)
        self.missChance = missChance

    def serang(self,target):
        damage = max(self.attack - target.armor ,0)
        target.diserang(damage)
        print(f'{self.name} menyerang {target.name}, dengan panah')

class EnergyMarksman(Marksman):
    def __init__(self, name, heakth, attack, armor, mana=50, missChance=50, energi=100):
        super().__init__(name, heakth, attack, armor, mana=50)
        self.energi = energi

    def serang(self,target):
        if self.energi > 20:
            damage = max(self.attac * 2 - target.armor, 0)
            target.diserang(damage)
            print(f'{self.name} menyerang {target.name}, damage {damage} sisa energi')
        else: 
            print(f'energi')

class Fighter(Hero):
    pass

balmond = Hero('balmond' ,100,15,4)
layla = Marksman('layla' ,80,20,4,30)
kimmy = EnergyMarksman('Kimmy' ,100,10,4,50,10,100)
print(layla.__dict__)

# layla.serang(balmond)
# print(layla.__dict__)
# print(balmond)