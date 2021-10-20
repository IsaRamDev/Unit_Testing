def convercion(numero_decimal, base):
    numero_binario = 0
    longitud_base = len(str(base))
    multiplicador = 1

    while numero_decimal != 0:
        # dividimos por la base indicada
        numero_binario = numero_binario + numero_decimal % base * multiplicador
        numero_decimal //= base
        multiplicador *= 10 ** longitud_base

    if base<10:
        return numero_binario
    else:
        numero_binario= "0"+ str(numero_binario)
        split_strings = []
        res= []
        n  = 2
        for index in range(0, len(numero_binario), n):
            split_strings.append(numero_binario[index : index + n])
        for i in split_strings:
            if i=="10":
                res.append("A")
            elif i=="11":
                res.append("B")
            elif i=="12":
                res.append("C")
            elif i=="13":
                res.append("D")
            elif i=="14":
                res.append("E")
            elif i=="15":
                res.append("F")
            else:
                res.append(i[1])
        return ("".join(res))
print(convercion(5476,16))

