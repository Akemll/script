import bcrypt

hash = "$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"
contar = 0
with open("rockyou.txt", "r", encoding="utf8", errors="ignore") as arquivo:
    for e in arquivo.readlines():
        
        if bcrypt.checkpw(e.encode(), hash.encode()):
            print(f"Achamos: {e}")
            break
        elif e.isalpha():
            if bcrypt.checkpw(e.upper().encode(), hash.encode()) or bcrypt.checkpw(e.lower().encode(), hash.encode()):
                print(f"Achamos: {e}")
                break
        contar += 1
        print(contar)
        
