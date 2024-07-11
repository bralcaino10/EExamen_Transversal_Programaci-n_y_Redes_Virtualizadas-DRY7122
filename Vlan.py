# Función para determinar el tipo de VLAN
def determinar_tipo_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "Rango Normal"
    elif 1006 <= vlan_id <= 4094:
        return "Rango Extendido"
    else:
        return "Número de VLAN no válido"

# Solicitar al usuario que ingrese el número de VLAN
vlan_id = int(input("Por favor, ingrese el número de VLAN: "))

# Determinar y mostrar el tipo de VLAN
tipo_vlan = determinar_tipo_vlan(vlan_id)
print(f"El número de VLAN {vlan_id} corresponde al {tipo_vlan}.")