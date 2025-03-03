# Contraseña transformada
transformed_password = "6!!sbn*ass%84z@84c(8o_^4#_#8b0)5m_&j}y$vvw!h"

# 1. Revertir sub_14a6 (NOT y XOR)
def reverse_sub_14a6(s):
    return "".join(chr(~(ord(c) ^ 0xff) & 0xff) for c in s)

# 2. Revertir sub_1418 (Inversión)
def reverse_sub_1418(s):
    return s[::-1]

# 3. Revertir sub_12cb (Eliminar caracteres especiales)
def reverse_sub_12cb(s):
    result = []
    i = 0
    while i < len(s):
        result.append(s[i])
        if (len(result) + 1) % 4 == 0:
            i += 1  # Saltar el carácter especial
        i += 1
    return "".join(result)

# 4. Revertir sub_1199 (Sustitución inversa)
def reverse_sub_1199(s):
    charset = "0123456789abcdefghijklmnopqrstuvwxyz_{}"
    result = []
    for c in s:
        idx = charset.find(c)
        if idx != -1:
            result.append(charset[(idx - 7) % len(charset)])
        else:
            result.append(c)
    return "".join(result)

# Aplicar las transformaciones en orden inverso
step1 = reverse_sub_14a6(transformed_password)
step2 = reverse_sub_1418(step1)
step3 = reverse_sub_12cb(step2)
step4 = reverse_sub_1199(step3)

# Ajustar el formato de la flag
if step4.startswith("apoorvctf{") and step4.endswith("}"):
    print("Contraseña original:", step4)
else:
    # Si no coincide, intentar corregir manualmente
    print("Posible contraseña original:", step4)
    print("Ajusta manualmente para que coincida con 'apoorvctf{flag}'.")