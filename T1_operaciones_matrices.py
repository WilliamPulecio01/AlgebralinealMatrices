"""
╔══════════════════════════════════════════════════════════════╗
║         T1 - OPERACIONES CON MATRICES                        ║
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
#   Tres ejercicios, cada uno verificado con:
#     (a) Sistemas de Ecuaciones Lineales
#     (b) Método de Cofactores  (para calcular la inversa de A)
#     (c) Eliminación de Gauss-Jordan
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 4 ── MULTIPLICACIÓN DE MATRICES  (A × B)")
 
def inversa_por_sistemas(A):
    """A⁻¹ resuelta columna a columna: A·xⱼ = eⱼ"""
    n = A.shape[0]
    I = np.eye(n)
    cols = [np.linalg.solve(A, I[:, j]) for j in range(n)]
    return np.column_stack(cols)
 
def inversa_por_cofactores(A):
    """A⁻¹ = adj(A) / det(A)"""
    n = A.shape[0]
    d = np.linalg.det(A)
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            menor = np.delete(np.delete(A, i, 0), j, 1)
            C[i, j] = ((-1)**(i+j)) * np.linalg.det(menor)
    return C.T / d
 
def inversa_por_gauss_jordan(A):
    """Reducción [A|I] → [I|A⁻¹]"""
    n = A.shape[0]
    M = np.hstack([A.copy().astype(float), np.eye(n)])
    for col in range(n):
        # Pivoteo parcial
        fila_max = np.argmax(np.abs(M[col:, col])) + col
        M[[col, fila_max]] = M[[fila_max, col]]
        M[col] /= M[col, col]
        for f in range(n):
            if f != col:
                M[f] -= M[f, col] * M[col]
    return M[:, n:]
 
def verificar_multiplicacion(label, A, B):
    """Calcula A@B por NumPy y verifica con los tres métodos de inversión."""
    print(f"\n  {'─'*55}")
    print(f"  ▶  {label}")
    print(f"  {'─'*55}")
    mostrar("A", A)
    mostrar("B", B)
 
    P_directo = A @ B
    mostrar("P = A × B  (directo)", P_directo)
 
    # ── (a) Verificación por Sistemas de Ecuaciones
    #   Si conocemos P = A@B, entonces B = A⁻¹@P  →  A@B debe dar P
    print("\n  ▷ Verificación (a): Sistemas de Ecuaciones")
    Ainv_sis = inversa_por_sistemas(A)
    P_verif_sis = Ainv_sis @ (A @ B)   # debe dar B
    ok_sis = np.allclose(P_verif_sis, B, atol=1e-8)
    print(f"    A⁻¹_sis @ (A@B) == B  →  {ok_sis}")
 
    # ── (b) Verificación por Cofactores
    print("  ▷ Verificación (b): Cofactores")
    Ainv_cof = inversa_por_cofactores(A)
    P_verif_cof = Ainv_cof @ (A @ B)
    ok_cof = np.allclose(P_verif_cof, B, atol=1e-8)
    print(f"    A⁻¹_cof @ (A@B) == B  →  {ok_cof}")
 
    # ── (c) Verificación por Gauss-Jordan
    print("  ▷ Verificación (c): Gauss-Jordan")
    Ainv_gj = inversa_por_gauss_jordan(A)
    P_verif_gj = Ainv_gj @ (A @ B)
    ok_gj = np.allclose(P_verif_gj, B, atol=1e-8)
    print(f"    A⁻¹_gj  @ (A@B) == B  →  {ok_gj}")
 
    estado = "✓  VERIFICADO" if (ok_sis and ok_cof and ok_gj) else "✗  DISCREPANCIA"
    print(f"\n  Resultado final: {estado}")
    return P_directo
 
subtitulo("Ejercicio 1  [3×3 × 3×3]")
A1 = np.array([[1., 2., 3.],
               [0., 1., 4.],
               [5., 6., 0.]])
B1 = np.array([[2., 0., 1.],
               [0., 3., 2.],
               [1., 0., 4.]])
verificar_multiplicacion("A₁ × B₁", A1, B1)
 
subtitulo("Ejercicio 2  [3×3 × 3×3]")
A2 = np.array([[2., 1., 0.],
               [1., 3., 1.],
               [0., 1., 2.]])
B2 = np.array([[1., 2., 3.],
               [4., 5., 6.],
               [7., 8., 9.]])
verificar_multiplicacion("A₂ × B₂", A2, B2)
 
subtitulo("Ejercicio 3  [4×4 × 4×4]")
A3 = np.array([[2.,  1., -1.,  0.],
               [0.,  3.,  2.,  1.],
               [1.,  0.,  4., -1.],
               [-1., 2.,  0.,  3.]])
B3 = np.array([[1.,  2.,  0.,  1.],
               [3., -1.,  2.,  0.],
               [0.,  1.,  3.,  2.],
               [2.,  0., -1.,  1.]])
verificar_multiplicacion("A₃ × B₃", A3, B3)
 
print(f"\n{SEP}")
print("  ✅  T1 completado — todas las operaciones ejecutadas.")
print(SEP)