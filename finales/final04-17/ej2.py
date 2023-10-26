# Consonantes:
# 0x0: p, 0x1: b, 0x2: t, 0x3: d, 0x4: k, 0x5: g, 0x6: sh, 0x7: j,
# 0x8: f, 0x9: v, 0xa: l, 0xb: r, 0xc: m, 0xd: y, 0xe: s,  0xf: z
#
# Vocales:
# 0x0: a,  0x1: e,  0x2: i,  0x3: o,  0x4: u,  0x5: an, 0x6: en, 0x7: in,
# 0x8: un, 0x9: on, 0xa: ai, 0xb: ei, 0xc: oi, 0xd: ui, 0xe: aw, 0xf: ow

def bitspeak(b):

    resultado = ""
    
    diccionario_consonantes = {"0x0": "p", "0x1": "b", "0x2": "t", "0x3": "d", "0x4": "k", "0x5": "g", "0x6": "sh", "0x7": "j", "0x8": "f", "0x9": "v", "0xa": "l", "0xb": "r", "0xc": "m", "0xd":"y", "0xe": "s",  "0xf": "z"}
    diccionario_vocales = {"0x0": "a", "0x1": "e",  "0x2": "i",  "0x3": "o",  "0x4": "u",  "0x5": "an", "0x6": "en", "0x7": "in", "0x8": "un", "0x9": "on", "0xa": "ai", "0xb": "ei", "0xc": "oi", "0xd": "ui", "0xe": "aw", "0xf": "ow"}

    for elemento in b:
        numero = hex(elemento)
        if len(numero) == 3:
            resultado += "p"
            resultado += diccionario_vocales[numero]
        else:
            clave_consonante = numero[:3]
            clave_vocal = numero[:2] + numero[-1]
            resultado += diccionario_consonantes[clave_consonante]
            resultado += diccionario_vocales[clave_vocal]
    
    return resultado

def pruebas():
    assert bitspeak([165, 8]) == "lanpun"

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
