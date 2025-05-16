import numpy as np
import re

massa_molar_rounded = {
    'Al': 26.982, 'Sb': 121.76, 'Ar': 39.95, 'As': 74.922, 'Ba': 137.33, 'Be': 9.0122, 'Bi': 208.98, 'B': 10.81,
    'Br': 79.904, 'Cd': 112.41, 'Ca': 40.078, 'C': 12.011, 'Ce': 140.12, 'Cs': 132.91, 'Cl': 35.45, 'Cr': 51.996,
    'Co': 58.933, 'Cu': 63.546, 'Dy': 162.50, 'Er': 167.26, 'Eu': 151.96, 'F': 18.998, 'Gd': 157.25, 'Ga': 69.723,
    'Ge': 72.630, 'Au': 196.97, 'Hf': 178.49, 'He': 4.0026, 'Ho': 164.93, 'H': 1.0080, 'In': 114.82, 'I': 126.90,
    'Ir': 192.22, 'Fe': 55.845, 'Kr': 83.798, 'La': 138.91, 'Pb': 207.2, 'Li': 6.94, 'Lu': 174.97, 'Mg': 24.305,
    'Mn': 54.938, 'Hg': 200.59, 'Mo': 95.95, 'Nd': 144.24, 'Ne': 20.180, 'Ni': 58.693, 'Nb': 92.906, 'N': 14.007,
    'Os': 190.23, 'O': 15.999, 'Pd': 106.42, 'P': 30.974, 'Pt': 195.08, 'K': 39.098, 'Pr': 140.91, 'Pa': 231.04,
    'Re': 186.21, 'Rh': 102.91, 'Rb': 85.468, 'Ru': 101.07, 'Sm': 150.36, 'Sc': 44.956, 'Se': 78.971, 'Si': 28.085,
    'Ag': 107.87, 'Na': 22.990, 'Sr': 87.62, 'S': 32.06, 'Ta': 180.95, 'Te': 127.60, 'Tb': 158.93, 'Tl': 204.38,
    'Th': 232.04, 'Tm': 168.93, 'Sn': 118.71, 'Ti': 47.867, 'W': 183.84, 'U': 238.03, 'V': 50.942, 'Xe': 131.29,
    'Yb': 173.05, 'Y': 88.906, 'Zn': 65.38, 'Zr': 91.224
}



def massa_molar(simbolo):
    return massa_molar_rounded.get(simbolo, None)

def estq(MM_ls, x_ls, massa_total):
    massa_esteq = np.array([])
    massa_molar_total = np.sum(MM_ls * x_ls)
    n_mols = massa_total / massa_molar_total
    for i in range(len(MM_ls)):
        massa_i = n_mols * x_ls[i] * MM_ls[i]
        massa_esteq = np.append(massa_esteq, massa_i)
    return massa_esteq

def parse_formula(formula):
    padrao = r'([A-Z][a-z]?)(\d*\.?\d*)'  # aceita inteiros ou decimais
    elementos = re.findall(padrao, formula)
    simbolos = []
    proporcoes = []
    for simbolo, quantidade in elementos:
        MM = massa_molar(simbolo)
        if MM is None:
            raise ValueError(f"Elemento '{simbolo}' não encontrado na tabela.")
        simbolos.append(simbolo)
        proporcoes.append(float(quantidade) if quantidade else 1.0)
    return simbolos, proporcoes

# Interação com o usuário
formula = input("Digite o composto (ex: Ni0.5Te2 / NiTe2): ").strip()
massa_total = float(input("Digite a massa total do composto (em gramas): "))

try:
    simbolos, proporcoes = parse_formula(formula)
except ValueError as e:
    print(e)
    exit()

MM_ls = [massa_molar(s) for s in simbolos]
x_ls = proporcoes

MM_array = np.array(MM_ls)
x_array = np.array(x_ls)

resultado = estq(MM_array, x_array, massa_total)

print("\nMassas estequiométricas:")
for i in range(len(simbolos)):
    print(f"{x_ls[i]} × {simbolos[i]}: {resultado[i]:.4f} g")