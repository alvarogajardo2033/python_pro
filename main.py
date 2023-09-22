meme_dict = {
    'CRINGE': 'Pena Ajena',
    'LOL': 'Una respuesta común a algo gracioso',
    'ROFL':  'una respuesta a una broma',
    'SHEESH': 'Ligera desaprobación',
    'CREEPY': 'aterrador, siniestro',
    'AGGRO': 'ponerse agresivo/enojado'
}



word = input("escribe una palabra que no entiendas(con mayusculas)")

if word in meme_dict.keys():
    # que debiramos aser si se encuentra la palabra
    print(meme_dict[word])

else:
    # que hacer si no se encuentra la palabra
    print("tu palabra no esta lo siento")
