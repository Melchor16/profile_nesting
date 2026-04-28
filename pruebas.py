perfiles = {
    '2" x 2" x 1/4" Angle': 240,
    '4" x 2" x 1/2" PTR': 480,
    '2" x 1/4" Flat Bar': 120,
}

partes = {
    '2" x 2" x 1/4" Angle': [
        {"item": 1, "length": 85, "qty": 1, "profile": '2" x 2" x 1/4" Angle'},
        {"item": 2, "length": 85, "qty": 1, "profile": '2" x 2" x 1/4" Angle'},
        {"item": 3, "length": 27, "qty": 1, "profile": '2" x 2" x 1/4" Angle'},
        {"item": 4, "length": 12, "qty": 1, "profile": '2" x 2" x 1/4" Angle'},
        {"item": 5, "length": 7,  "qty": 1, "profile": '2" x 2" x 1/4" Angle'},
    ],
    '4" x 2" x 1/2" PTR': [
        {"item": 1, "length": 92, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 2, "length": 75, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 3, "length": 34, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 4, "length": 18, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 5, "length": 12, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
    ],
    '4" x 2" x 1/2" PTR': [
        {"item": 1, "length": 92, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 2, "length": 75, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 3, "length": 34, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 4, "length": 18, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
        {"item": 5, "length": 12, "qty": 1, "profile": '4" x 2" x 1/2" PTR'},
    ],
    '2" x 1/4" Flat Bar': [
        {"item": 1, "length": 75, "qty": 1, "profile": '2" x 1/4" Flat Bar'},
        {"item": 2, "length": 75, "qty": 1, "profile": '2" x 1/4" Flat Bar'},
        {"item": 3, "length": 23, "qty": 1, "profile": '2" x 1/4" Flat Bar'},
        {"item": 4, "length": 19, "qty": 1, "profile": '2" x 1/4" Flat Bar'},
        {"item": 5, "length": 19, "qty": 1, "profile": '2" x 1/4" Flat Bar'},
    ],
}


def nesting(profile_length, parts_length):
    bars = []

    for part in parts_length:
        placed = False

        for bar in bars:
            if sum(bar) + part <= profile_length:
                bar.append(part)
                placed = True
                break
        if not placed:
            bars.append([part])
    
    return bars


for perfil, lista_partes in partes.items():
    profile_length = perfiles[perfil]

    lengths = [p["length"] for p in lista_partes]
    lengths.sort(reverse = True)

    resultado = nesting(profile_length, lengths)

    print(perfil, ": ", resultado)


parts = {
    "name1":{
        "nestings": [1, 2, 3, 4],
        "profile_length": 120,
    },
    "name2":{
        "nestings": [5, 6, 7, 8],
        "profile_length": 140,
    },
    "name3":{
        "nestings": [9, 10, 11, 12],
        "profile_length": 240,
    },
}