voto_1 = 0
voto_2 = 0
zero = 0

while True:

    print("-------------------------------")

    voto = int(input("Candidato 1: Adilson \nCandidato 2: Jorge \nSeu voto: "))

    if voto == 1:
        voto_1 += 1
    elif voto == 2:
        voto_2 += 1
    else:
        zero += 1


    print("-------------------------------")
    print("-------------------------------")
    print("CONTABILIZANDO VOTOS... ADILSON: {}, JORGE: {}\n Nulos... {}" .format(voto_1, voto_2, zero))
    print("-------------------------------")  

        