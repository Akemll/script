import bcrypt, random

lista = []
tudo = [1,2,3,4,5,6,7,8,9,0, "a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
hesh, vezes = b"$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom", 0
while True:
    palavra = ""
    for e in range(0, 4):
       escolha = str(random.choice(tudo))
       if escolha.isalpha():
           if random.choice((True, False)):
               escolha = escolha.upper()
       palavra += escolha
    print(escolha)
    if palavra not in lista:
        vezes += 1
        lista.append(palavra)
        palavra = palavra.encode()
        print(palavra)
        if bcrypt.checkpw(palavra, hesh):
            print(f"Achou {palavra}")
            break
        print(vezes)
