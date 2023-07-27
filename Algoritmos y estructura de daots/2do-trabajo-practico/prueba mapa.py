def arriba():
    return "+--+--+--+--+--+"

def locales(db):
   global i
   while len(db) > i:
      print(arriba())
      print(f"|0{db[i]}|0{db[i+1]}|0{db[i+2]}|0{db[i+3]}|0{db[i+4]}|")
      i += 5
   print(arriba())


shops = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i = 0
print(locales(shops))
