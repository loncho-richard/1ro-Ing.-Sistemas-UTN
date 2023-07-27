shops = [[1, "asd"],
         [2, "asd"],
         [3, "asd"],
         [5, "asd"],
         [4, "asd"],
         [6, "asd"],
         [8, "asd"],
         [14, "asd"],
         [7, "asd"],
         [88, "asd"]]

def question(idx):
    if idx < 10:
        return f"|O{idx}"
    elif idx == "":
        return "|00"
    else:
        return f"|{idx}"

def map_shops(db):
    i = 0
    for floor in range(1):
        print(f"Piso {floor + 1}")
        for row in range(2):
            print("+--+--+--+--+--+")
            id_1 = db[i][0]
            i += 1
            id_2 = db[i][0]
            i += 1
            id_3 = db[i][0]
            i += 1
            id_4 = db[i][0]
            i += 1
            id_5 = db[i][0]
            i += 1  
            print(f"{question(id_1)}{question(id_2)}{question(id_3)}{question(id_4)}{question(id_5)}|")
        
        print("+--+--+--+--+--+")
        print("  (...)   ")

map_shops(shops)