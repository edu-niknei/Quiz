
antal_rätt = []
antal_frågor = []
svar1 = int(input("vilken huvudstad har sverige?\n1. Oslo\n2. Stockholm\n3. Köpenhamn\n"))
if svar1 == 2:
    print(f"ditt val: {svar1}")
    print("Rätt!")
    antal_rätt.append(1)
    antal_frågor.append(1)
else:
    print("Fel rätt svar var: Stockholm")
    antal_frågor.append(1)

svar2 = int(input("Vilken huvudstad har Norge?\n1. Oslo\n2. Bergen\n3. Trondheim\n"))
if svar2 == 1:
    print(f"ditt val: {svar2}")
    print("Rätt!")
    antal_rätt.append(1)
    antal_frågor.append(1)
else:
    print("Fel, rätt svar var: Oslo")
    antal_frågor.append(1)

svar3 = int(input("vilket år började andra världskriget?\n1. 1914\n2. 1939\n3. 1945\n"))
if svar3 == 2:
    print(f"ditt val: {svar3}")
    print("Rätt!")
    antal_rätt.append(1)
    antal_frågor.append(1)
else:
    print("Fel rätt svar var: 1939")
    antal_frågor.append(1)

print(f"du fick {len(antal_rätt)} av {len(antal_frågor)} rätt.")