stringa = input("Inserire una stringa: ")

if len(stringa) > 10:
    risultato = stringa[:10] + "..."
    print("Risultato: " + risultato)
else:
    print("Risultato: " + stringa)
