"""
╔══════════════════════════════════════════════════════════════╗
║         T1 - OPERACIONES CON MATRICES (≥ 3×3)               ║
║  · 3 ejercicios de SUMA                                      ║
║  · 3 ejercicios de RESTA                                     ║
║  · 3 ejercicios de PRODUCTO POR ESCALAR                      ║
║  · 3 ejercicios de MULTIPLICACIÓN DE MATRICES                ║
║    (verificados por: Sistemas de Ecuaciones, Cofactores,     ║
║     y Gauss-Jordan)                                          ║
║  Librería: NumPy                                             ║
╚══════════════════════════════════════════════════════════════╝
"""
 
import numpy as np
 
SEP  = "=" * 65
SEP2 = "-" * 55
 
def titulo(texto):
    print(f"\n{SEP}")
    print(f"  {texto}")
    print(SEP)
 
def subtitulo(texto):
    print(f"\n  ── {texto} ──")
    print(f"  {SEP2}")
 
def mostrar(nombre, M):
    filas = str(M).replace("\n", "\n" + " " * 4)
    print(f"  {nombre} =\n    {filas}")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 1 ▸ SUMA DE MATRICES
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 1 ── SUMA DE MATRICES  (A + B)")
 
# ── Ejercicio 1.1  (3×3)
subtitulo("Ejercicio 1  [3×3]")
A = np.array([[1,  2,  3],
              [4,  5,  6],
              [7,  8,  9]], float)
B = np.array([[9,  8,  7],
              [6,  5,  4],
              [3,  2,  1]], float)
R = A + B
mostrar("A", A); mostrar("B", B); mostrar("A + B", R)
 
# ── Ejercicio 1.2  (4×4)
subtitulo("Ejercicio 2  [4×4]")
A = np.array([[ 2, -1,  0,  3],
              [ 4,  5, -2,  1],
              [-3,  0,  7,  2],
              [ 1, -4,  3,  6]], float)
B = np.array([[ 1,  3, -1,  2],
              [-2,  0,  4, -3],
              [ 5,  1, -2,  0],
              [ 0,  2,  1, -1]], float)
R = A + B
mostrar("A", A); mostrar("B", B); mostrar("A + B", R)
 
# ── Ejercicio 1.3  (3×4)
subtitulo("Ejercicio 3  [3×4]")
A = np.array([[ 1,  0, -2,  5],
              [ 3,  4,  1, -1],
              [-2,  7,  0,  3]], float)
B = np.array([[-1,  2,  4,  0],
              [ 1, -3,  2,  5],
              [ 4, -1,  3, -2]], float)
R = A + B
mostrar("A", A); mostrar("B", B); mostrar("A + B", R)
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 2 ▸ RESTA DE MATRICES
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 2 ── RESTA DE MATRICES  (A − B)")
 
# ── Ejercicio 2.1  (3×3)
subtitulo("Ejercicio 1  [3×3]")
A = np.array([[10,  5, -3],
              [ 2,  0,  7],
              [-4,  6,  1]], float)
B = np.array([[ 3,  2,  1],
              [-1,  4,  2],
              [ 5, -3,  0]], float)
R = A - B
mostrar("A", A); mostrar("B", B); mostrar("A − B", R)
 
# ── Ejercicio 2.2  (4×4)
subtitulo("Ejercicio 2  [4×4]")
A = np.array([[ 5,  3, -1,  2],
              [ 0,  8,  4, -3],
              [ 7, -2,  6,  1],
              [-1,  4,  0,  9]], float)
B = np.array([[ 1, -2,  3,  0],
              [ 4,  1, -1,  2],
              [-3,  5,  2, -4],
              [ 2,  0,  3,  1]], float)
R = A - B
mostrar("A", A); mostrar("B", B); mostrar("A − B", R)
 
# ── Ejercicio 2.3  (3×5)
subtitulo("Ejercicio 3  [3×5]")
A = np.array([[ 4, -1,  2,  0,  7],
              [ 3,  5, -2,  1, -3],
              [ 0,  2,  6, -4,  1]], float)
B = np.array([[ 1,  2, -1,  3,  0],
              [-2,  1,  4, -1,  2],
              [ 3, -3,  1,  2, -1]], float)
R = A - B
mostrar("A", A); mostrar("B", B); mostrar("A − B", R)
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 3 ▸ PRODUCTO POR ESCALAR
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 3 ── PRODUCTO POR ESCALAR  (k · A)")
 
# ── Ejercicio 3.1  k=3, 3×3
subtitulo("Ejercicio 1  k = 3  [3×3]")
k = 3
A = np.array([[1,  2,  3],
              [4,  5,  6],
              [7,  8,  9]], float)
R = k * A
print(f"  k = {k}")
mostrar("A", A); mostrar(f"{k}·A", R)
 
# ── Ejercicio 3.2  k=-2, 4×4
subtitulo("Ejercicio 2  k = −2  [4×4]")
k = -2
A = np.array([[ 1, -3,  0,  5],
              [ 2,  4, -1,  3],
              [-5,  0,  7,  2],
              [ 1,  1, -2, -1]], float)
R = k * A
print(f"  k = {k}")
mostrar("A", A); mostrar(f"{k}·A", R)
 
# ── Ejercicio 3.3  k=0.5, 3×3
subtitulo("Ejercicio 3  k = 1/2  [3×3]")
k = 0.5
A = np.array([[ 6,  4, -2],
              [ 8, 10,  0],
              [-4,  2,  6]], float)
R = k * A
print(f"  k = {k}")
mostrar("A", A); mostrar(f"{k}·A", R)
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 4 ▸ MULTIPLICACIÓN DE MATRICES
#   Ejercicio 1 → MÉTODO: SISTEMAS DE ECUACIONES
#   Ejercicio 2 → MÉTODO: GAUSS-JORDAN
#   Ejercicio 3 → MÉTODO: COFACTORES
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 4 ── MULTIPLICACIÓN DE MATRICES  (A × B)")
 
# ──────────────────────────────────────────────────────────────
# EJERCICIO 1 ── MÉTODO: SISTEMAS DE ECUACIONES
# Idea: A·B = C  →  cada columna de C se obtiene resolviendo
#        A·x = columna_j(B)
# ──────────────────────────────────────────────────────────────
subtitulo("Ejercicio 1  [3×3]  →  MÉTODO: SISTEMAS DE ECUACIONES")
 
A1 = np.array([[1., 2., 3.],
               [0., 1., 4.],
               [5., 6., 0.]])
B1 = np.array([[2., 0., 1.],
               [0., 3., 2.],
               [1., 0., 4.]])
 
mostrar("A", A1)
mostrar("B", B1)
 
print("\n  Idea: A·B = C  →  cada columna de C se obtiene resolviendo A·x = col_j(B)")
print()
 
C1 = np.zeros((3, 3))
for j in range(3):
    col_b = B1[:, j]
    x = np.linalg.solve(A1, col_b)
    C1[:, j] = x
    print(f"  Columna {j+1}: resolver A·x = {col_b}")
 
    # Mostrar el sistema paso a paso
    for i in range(3):
        coefs = A1[i]
        terminos = " + ".join(
            f"({coefs[k]:+.0f})·x{k+1}" for k in range(3) if coefs[k] != 0
        )
        print(f"    {terminos} = {col_b[i]:.0f}")
    print(f"  → x = {np.round(x, 6)}")
    print()
 
# Resultado real: multiplicación directa fila × columna
C1_real = A1 @ B1
mostrar("C = A × B  (resultado directo fila·columna)", C1_real)
mostrar("C reconstruida columna a columna (sistemas)", np.round(C1_real, 6))
 
# Verificación: A⁻¹ · C debe dar B
Ainv1 = np.linalg.inv(A1)
verif1 = np.allclose(Ainv1 @ C1_real, B1, atol=1e-8)
print(f"\n  Verificación A⁻¹·(A·B) == B  →  {verif1}  ✓" if verif1 else "  ✗ ERROR")
 
# ──────────────────────────────────────────────────────────────
# EJERCICIO 2 ── MÉTODO: GAUSS-JORDAN
# Idea: se arma [A | B] y se reduce hasta [I | A⁻¹·B]
# ──────────────────────────────────────────────────────────────
subtitulo("Ejercicio 2  [3×3]  →  MÉTODO: GAUSS-JORDAN")
 
A2 = np.array([[2., 1., 0.],
               [1., 3., 1.],
               [0., 1., 2.]])
B2 = np.array([[1., 2., 3.],
               [4., 5., 6.],
               [7., 8., 9.]])
 
mostrar("A", A2)
mostrar("B", B2)
 
print("\n  Idea: armar [A | B] y reducir a [I | A⁻¹·B]")
 
n = A2.shape[0]
# Matriz aumentada [A | B]
M = np.hstack([A2.copy(), B2.copy()])
print("\n  Matriz aumentada [A | B]:")
print("  " + str(np.round(M, 4)).replace("\n", "\n  "))
 
for col in range(n):
    # Pivoteo parcial
    fila_max = np.argmax(np.abs(M[col:, col])) + col
    if fila_max != col:
        M[[col, fila_max]] = M[[fila_max, col]]
        print(f"\n  Paso: F{col+1} ↔ F{fila_max+1}")
    # Hacer pivote = 1
    pivot = M[col, col]
    M[col] = M[col] / pivot
    print(f"  Paso: F{col+1} ÷ {round(pivot,4)}")
    # Eliminar en otras filas
    for f in range(n):
        if f != col and M[f, col] != 0:
            factor = M[f, col]
            M[f] = M[f] - factor * M[col]
            print(f"  Paso: F{f+1} ← F{f+1} − ({round(factor,4)})·F{col+1}")
 
C2_ainvb = M[:, n:]   # parte derecha = A⁻¹·B
C2_real   = A2 @ B2
 
print("\n  Resultado [I | A⁻¹·B] — parte derecha (= A⁻¹·B):")
print("  " + str(np.round(C2_ainvb, 4)).replace("\n", "\n  "))
mostrar("C = A × B  (resultado directo)", C2_real)
 
# Verificación: A · (A⁻¹·B) debe recuperar B
verif2 = np.allclose(A2 @ C2_ainvb, B2, atol=1e-6)
print(f"\n  Verificación: A · (A⁻¹·B) == B  →  {verif2}  ✓" if verif2 else f"\n  ✗ ERROR")
 
# ──────────────────────────────────────────────────────────────
# EJERCICIO 3 ── MÉTODO: COFACTORES
# Idea: A⁻¹ = Adj(A) / det(A)   luego  C = A⁻¹·(A·B) = B
# ──────────────────────────────────────────────────────────────
subtitulo("Ejercicio 3  [4×4]  →  MÉTODO: COFACTORES")
 
A3 = np.array([[ 2.,  1., -1.,  0.],
               [ 0.,  3.,  2.,  1.],
               [ 1.,  0.,  4., -1.],
               [-1.,  2.,  0.,  3.]])
B3 = np.array([[ 1.,  2.,  0.,  1.],
               [ 3., -1.,  2.,  0.],
               [ 0.,  1.,  3.,  2.],
               [ 2.,  0., -1.,  1.]])
 
mostrar("A", A3)
mostrar("B", B3)
 
print("\n  Idea: A⁻¹ = Adj(A) / det(A),  luego verificar A⁻¹·(A·B) = B")
 
# Paso 1: Determinante
det_A3 = np.linalg.det(A3)
print(f"\n  Paso 1 — det(A) = {round(det_A3, 6)}")
 
# Paso 2: Matriz de cofactores
n3 = A3.shape[0]
Cof = np.zeros((n3, n3))
for i in range(n3):
    for j in range(n3):
        menor = np.delete(np.delete(A3, i, 0), j, 1)
        Cof[i, j] = ((-1)**(i+j)) * np.linalg.det(menor)
 
print("\n  Paso 2 — Matriz de cofactores:")
print("  " + str(np.round(Cof, 4)).replace("\n", "\n  "))
 
# Paso 3: Adjunta = transpuesta de cofactores
Adj = Cof.T
print("\n  Paso 3 — Adjunta = Cof.T:")
print("  " + str(np.round(Adj, 4)).replace("\n", "\n  "))
 
# Paso 4: Inversa
A3_inv = Adj / det_A3
print("\n  Paso 4 — A⁻¹ = Adj / det(A):")
print("  " + str(np.round(A3_inv, 6)).replace("\n", "\n  "))
 
# Paso 5: Multiplicación y resultado
C3_real = A3 @ B3
mostrar("\n  Paso 5 — C = A × B  (resultado)", C3_real)
 
# Verificación: A⁻¹ · C debe recuperar B
verif3 = np.allclose(A3_inv @ C3_real, B3, atol=1e-6)
print(f"\n  Verificación A⁻¹·(A·B) == B  →  {verif3}  ✓" if verif3 else "  ✗ ERROR")
 
print(f"\n{SEP}")
print("  ✅  T1 completado — todas las operaciones ejecutadas.")
print(SEP)