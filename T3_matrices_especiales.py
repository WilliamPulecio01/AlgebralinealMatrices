"""
╔══════════════════════════════════════════════════════════════╗
║              T3 - MATRICES ESPECIALES                        ║
║  · 3 ejercicios  MATRIZ ROTACIONAL                           ║
║  · 3 ejercicios  MATRIZ SIMÉTRICA                            ║
║  · 3 ejercicios  MATRIZ ANTISIMÉTRICA                        ║
║  Librería: NumPy                                             ║
╚══════════════════════════════════════════════════════════════╝
"""
 
import numpy as np
 
SEP = "=" * 60
 
def titulo(texto):
    print(f"\n{SEP}")
    print(f"  {texto}")
    print(SEP)
 
def subtitulo(texto):
    print(f"\n  ── {texto}")
    print(f"  {'-'*50}")
 
def mostrar_matriz(nombre, M):
    print(f"\n  {nombre}:")
    for fila in M:
        # redondear valores muy pequeños a cero (como cos(90°) = 6.12e-17)
        fila_limpia = [0.0 if abs(v) < 1e-10 else v for v in fila]
        print("    [" + "  ".join(f"{v:6.4g}" for v in fila_limpia) + "]")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 1 ── MATRICES ROTACIONALES
#  Fórmula: R(θ) = [[cos θ, -sin θ], [sin θ, cos θ]]
#  Rotar un vector v con θ dado → R · v
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 1 ── MATRICES ROTACIONALES")
 
def matriz_rotacion(grados):
    t = np.radians(grados)
    return np.array([[np.cos(t), -np.sin(t)],
                     [np.sin(t),  np.cos(t)]])
 
# ── Ejercicio 1: Rotar (1, 0) con θ = 90°
subtitulo("Ejercicio 1 ── Rotar el vector (1, 0) con θ = 90°")
grados = 90
v = np.array([1, 0])
t = np.radians(grados)
 
print(f"\n  Fórmula de la matriz rotacional:")
print(f"  R(θ) = [[cos θ,  -sin θ],")
print(f"          [sin θ,   cos θ]]")
 
print(f"\n  Sustituir θ = {grados}°:")
cos_val = round(np.cos(t), 10)
sin_val = round(np.sin(t), 10)
print(f"  cos({grados}°) = {cos_val:.4g},   sin({grados}°) = {sin_val:.4g}")
 
R1 = matriz_rotacion(grados)
mostrar_matriz("R", R1)
 
print(f"\n  Multiplicar por el vector v = {v}:")
print(f"  R · v =")
resultado1 = np.round(R1 @ v, 10)
c0 = round(np.cos(t),4); s0 = round(np.sin(t),4)
print(f"    x = ({c0:.4g})({v[0]}) + ({-s0:.4g})({v[1]}) = {resultado1[0]:.4g}")
print(f"    y = ({s0:.4g})({v[0]}) + ({c0:.4g})({v[1]}) = {resultado1[1]:.4g}")
print(f"\n  Resultado: ({resultado1[0]:.4g}, {resultado1[1]:.4g})")
print(f"  Verificación R · Rᵀ = I  →  {np.allclose(R1 @ R1.T, np.eye(2))}")
print(f"  det(R) = {np.round(np.linalg.det(R1), 4)}  (debe ser +1)  →  {np.isclose(np.linalg.det(R1), 1.0)}")
 
# ── Ejercicio 2: Rotar (0, 1) con θ = 45°
subtitulo("Ejercicio 2 ── Rotar el vector (0, 1) con θ = 45°")
grados = 45
v = np.array([0, 1])
t = np.radians(grados)
 
print(f"\n  Fórmula de la matriz rotacional:")
print(f"  R(θ) = [[cos θ,  -sin θ],")
print(f"          [sin θ,   cos θ]]")
 
print(f"\n  Sustituir θ = {grados}°:")
print(f"  cos({grados}°) = {np.cos(t):.4f},   sin({grados}°) = {np.sin(t):.4f}")
 
R2 = matriz_rotacion(grados)
mostrar_matriz("R", R2)
 
print(f"\n  Multiplicar por el vector v = {v}:")
resultado2 = R2 @ v
print(f"    x = ({R2[0,0]:.4f})({v[0]}) + ({R2[0,1]:.4f})({v[1]}) = {resultado2[0]:.4f}")
print(f"    y = ({R2[1,0]:.4f})({v[0]}) + ({R2[1,1]:.4f})({v[1]}) = {resultado2[1]:.4f}")
print(f"\n  Resultado: ({resultado2[0]:.4f}, {resultado2[1]:.4f})")
print(f"  Verificación R · Rᵀ = I  →  {np.allclose(R2 @ R2.T, np.eye(2))}")
print(f"  det(R) = {np.round(np.linalg.det(R2), 4)}  (debe ser +1)  →  {np.isclose(np.linalg.det(R2), 1.0)}")
 
# ── Ejercicio 3: Rotar (1, 1) con θ = 180°
subtitulo("Ejercicio 3 ── Rotar el vector (1, 1) con θ = 180°")
grados = 180
v = np.array([1, 1])
t = np.radians(grados)
 
print(f"\n  Fórmula de la matriz rotacional:")
print(f"  R(θ) = [[cos θ,  -sin θ],")
print(f"          [sin θ,   cos θ]]")
 
print(f"\n  Sustituir θ = {grados}°:")
print(f"  cos({grados}°) = {np.cos(t):.4g},   sin({grados}°) = {np.sin(t):.4g}")
 
R3 = matriz_rotacion(grados)
mostrar_matriz("R", R3)
 
print(f"\n  Multiplicar por el vector v = {v}:")
resultado3 = R3 @ v
print(f"    x = ({R3[0,0]:.4g})({v[0]}) + ({R3[0,1]:.4g})({v[1]}) = {np.round(resultado3[0], 4):.4g}")
print(f"    y = ({R3[1,0]:.4g})({v[0]}) + ({R3[1,1]:.4g})({v[1]}) = {np.round(resultado3[1], 4):.4g}")
print(f"\n  Resultado: ({np.round(resultado3[0],4):.4g}, {np.round(resultado3[1],4):.4g})")
print(f"  Verificación R · Rᵀ = I  →  {np.allclose(R3 @ R3.T, np.eye(2), atol=1e-10)}")
print(f"  det(R) = {np.round(np.linalg.det(R3), 4):.4g}  (debe ser +1)  →  {np.isclose(np.linalg.det(R3), 1.0)}")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 2 ── MATRICES SIMÉTRICAS
#  Definición: A = Aᵀ
#  Paso 1: calcular transpuesta
#  Paso 2: comparar A == Aᵀ
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 2 ── MATRICES SIMÉTRICAS  (A = Aᵀ)")
 
def verificar_simetrica(A, nombre):
    print(f"\n  Definición: una matriz es simétrica si  A = Aᵀ")
    mostrar_matriz(f"A ({nombre})", A)
 
    AT = A.T
    print(f"\n  Paso 1 — Calcular la transpuesta:")
    mostrar_matriz("Aᵀ", AT)
 
    es_sim = np.array_equal(A, AT)
    print(f"\n  Paso 2 — Comparar A == Aᵀ:")
    if es_sim:
        print(f"  A = Aᵀ  →  ✓ ES SIMÉTRICA")
    else:
        print(f"  A ≠ Aᵀ  →  NO es simétrica")
    return es_sim
 
# ── Ejercicio 1
subtitulo("Ejercicio 1")
A1 = np.array([[2, 3, 1],
               [3, 5, 4],
               [1, 4, 6]], float)
verificar_simetrica(A1, "3×3")
 
# ── Ejercicio 2
subtitulo("Ejercicio 2")
A2 = np.array([[1, 2, 3],
               [2, 4, 5],
               [3, 5, 6]], float)
verificar_simetrica(A2, "3×3")
 
# ── Ejercicio 3
subtitulo("Ejercicio 3")
A3 = np.array([[ 4, -1,  2],
               [-1,  3,  0],
               [ 2,  0,  5]], float)
verificar_simetrica(A3, "3×3")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 3 ── MATRICES ANTISIMÉTRICAS
#  Definición: Aᵀ = -A
#  Paso 1: calcular transpuesta Aᵀ
#  Paso 2: calcular negativo -A
#  Paso 3: comparar Aᵀ == -A
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 3 ── MATRICES ANTISIMÉTRICAS  (Aᵀ = -A)")
 
def verificar_antisimetrica(A, nombre):
    print(f"\n  Definición: una matriz es antisimétrica si  Aᵀ = -A")
    mostrar_matriz(f"A ({nombre})", A)
 
    AT = A.T
    neg_A = -A
    print(f"\n  Paso 1 — Calcular la transpuesta:")
    mostrar_matriz("Aᵀ", AT)
 
    print(f"\n  Paso 2 — Calcular el negativo de A:")
    mostrar_matriz("-A", neg_A)
 
    es_anti = np.array_equal(AT, neg_A)
    print(f"\n  Paso 3 — Comparar Aᵀ == -A:")
    if es_anti:
        print(f"  Aᵀ = -A  →  ✓ ES ANTISIMÉTRICA")
        print(f"  Diagonal = {np.diag(A).astype(int)}  (siempre cero en antisimétricas)")
    else:
        print(f"  Aᵀ ≠ -A  →  NO es antisimétrica")
    return es_anti
 
# ── Ejercicio 1
subtitulo("Ejercicio 1")
K1 = np.array([[ 0,  2, -1],
               [-2,  0,  4],
               [ 1, -4,  0]], float)
verificar_antisimetrica(K1, "3×3")
 
# ── Ejercicio 2
subtitulo("Ejercicio 2")
K2 = np.array([[ 0,  3, -5],
               [-3,  0,  2],
               [ 5, -2,  0]], float)
verificar_antisimetrica(K2, "3×3")
 
# ── Ejercicio 3
subtitulo("Ejercicio 3")
K3 = np.array([[ 0,  1, -6],
               [-1,  0,  3],
               [ 6, -3,  0]], float)
verificar_antisimetrica(K3, "3×3")
 
print(f"\n{SEP}")
print("  ✅  T3 completado — 9 ejercicios de matrices especiales.")
print(SEP)