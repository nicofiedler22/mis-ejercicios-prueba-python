
print("Este es un programa que permite calcular sus beneficios en base a su nivel académico y socioeconómico.")
print("A continuación, por favor, ingrese los datos que se le solicitarán.")

prom = float(input("Ingrese su promedio: "))
quintil = int(input("Ingrese a qué quintil pertenece (1, 2, 3, 4 o 5): "))
arancel = 1800000
matricula = 90000


if prom > 6.0 and quintil == 1 or quintil == 2:
    arancel = arancel - (arancel * 0.20)
    matricula = matricula - (matricula * 0.15)

    print("Según los datos entregados, se han aplicado los siguientes beneficios:")
    print(f"El valor del arancel equivale a: {arancel}")
    print(f"El valor de la matrícula equivale a: {matricula}")
elif prom > 6.0 and quintil == 3 or quintil == 4:
    arancel = arancel - (arancel * 0.15)
    if quintil == 3:
        matricula = matricula - (matricula * 0.15)
    else:
        matricula = matricula

    print("Según los datos entregados, se han aplicado los siguientes beneficios:")
    print(f"El valor del arancel equivale a: {arancel}")
    print(f"El valor de la matrícula equivale a: {matricula}")

elif 5.0 < prom <= 6.0 and quintil == 1 or quintil == 2:
    arancel = arancel - (arancel * 0.13)
    if prom >= 5.5:
        matricula = matricula - (matricula * 0.15)
    else:
        matricula = matricula - (matricula * 0.10)
    print("Según los datos entregados, se han aplicado los siguientes beneficios:")
    print(f"El valor del arancel equivale a: {arancel}")
    print(f"El valor de la matrícula equivale a: {matricula}")

elif 5.0 < prom <= 6.0 and quintil == 3 or quintil == 4:
    arancel = arancel - (arancel * 0.10)
    if prom >= 5.5 and quintil == 3:
        matricula = matricula - (matricula * 0.15)
    else:
        matricula = matricula

    print("Según los datos entregados, se han aplicado los siguientes beneficios:")
    print(f"El valor del arancel equivale a: {arancel}")
    print(f"El valor de la matrícula equivale a: {matricula}")

elif quintil == 5:
    print("Usted no obtiene beneficios, a continuación, se le mostrarán los montos a pagar:")
    print(f"El arancel corresponde a: {arancel}")
    print(f"La matrícula corresponde a: {matricula}")