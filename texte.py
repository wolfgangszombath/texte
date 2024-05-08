namen = input("Gib Deinen Namen ein!\n")
print(namen)
with open("textdatei.txt","r") as file:
    for zeile in file:
        print(zeile)
