"""
╔══════════════════════════════════════════════════════════════╗
║              T3 - MATRICES                                   ║
║  · 3 ejercicios  MATRIZ ROTACIONAL                           ║
║  · 3 ejercicios  MATRIZ SIMÉTRICA                            ║
║  · 3 ejercicios  MATRIZ ANTISIMÉTRICA                        ║
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
    print(f"\n  ┌─ {texto}")
    print(f"  └{'─'*54}")
 
def mostrar(nombre, M, dec=4):
    filas = np.round(M, dec)
    s = str(filas).replace("\n", "\n    ")
    print(f"  {nombre} =\n    {s}")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 1 ▸ MATRICES ROTACIONALES
#  R es ortogonal: R·Rᵀ = I  y  det(R) = +1
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 1 ── MATRICES ROTACIONALES")
 
def R2D(deg):
    t = np.radians(deg)
    return np.array([[np.cos(t), -np.sin(t)],
                     [np.sin(t),  np.cos(t)]])
 
def Rx(deg):
    t = np.radians(deg)
    return np.array([[1, 0,           0          ],
                     [0, np.cos(t), -np.sin(t)   ],
                     [0, np.sin(t),  np.cos(t)   ]])
 
def Ry(deg):
    t = np.radians(deg)
    return np.array([[ np.cos(t), 0, np.sin(t)],
                     [ 0,         1, 0         ],
                     [-np.sin(t), 0, np.cos(t) ]])
 
def Rz(deg):
    t = np.radians(deg)
    return np.array([[np.cos(t), -np.sin(t), 0],
                     [np.sin(t),  np.cos(t), 0],
                     [0,          0,         1]])
 
def propiedades_rotacion(R, label):
    RRt     = np.round(R @ R.T, 8)
    es_ort  = np.allclose(RRt, np.eye(R.shape[0]), atol=1e-8)
    det_R   = np.round(np.linalg.det(R), 6)
    print(f"\n  Propiedades de {label}:")
    print(f"    R · Rᵀ = I  →  {es_ort}")
    print(f"    det(R) = {det_R}  (debe ser +1)  →  {np.isclose(det_R, 1.0)}")
 
# ── Ejercicio 1: Rotación 3D alrededor del eje Z en 45°
subtitulo("Ejercicio 1 ── Rotación 3D alrededor del eje Z, θ = 45°")
R1 = Rz(45)
v1 = np.array([1., 0., 0.])
mostrar("R_z(45°)", R1)
print(f"  Vector original:  v  = {v1}")
print(f"  Vector rotado: R·v  = {np.round(R1 @ v1, 4)}")
propiedades_rotacion(R1, "Rz(45°)")
 
# ── Ejercicio 2: Rotación 3D alrededor del eje X en 60°
subtitulo("Ejercicio 2 ── Rotación 3D alrededor del eje X, θ = 60°")
R2 = Rx(60)
v2 = np.array([0., 1., 0.])
mostrar("R_x(60°)", R2)
print(f"  Vector original:  v  = {v2}")
print(f"  Vector rotado: R·v  = {np.round(R2 @ v2, 4)}")
propiedades_rotacion(R2, "Rx(60°)")
 
# ── Ejercicio 3: Rotación 3D combinada Ry(30°)·Rz(90°)·Rx(45°)
subtitulo("Ejercicio 3 ── Rotación 3D combinada  Ry(30°)·Rz(90°)·Rx(45°)")
R3 = Ry(30) @ Rz(90) @ Rx(45)
v3 = np.array([1., 1., 1.]) / np.sqrt(3)
mostrar("R_comb", R3)
print(f"  Vector unitario original:  v      = {np.round(v3, 4)}")
print(f"  Vector unitario rotado:  R·v    = {np.round(R3 @ v3, 4)}")
print(f"  Norma conservada: ||v|| = {np.round(np.linalg.norm(v3),4)},  "
      f"||R·v|| = {np.round(np.linalg.norm(R3@v3),4)}")
propiedades_rotacion(R3, "R_comb")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 2 ▸ MATRICES SIMÉTRICAS
#  S = Sᵀ   →  todos los eigenvalores son reales
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 2 ── MATRICES SIMÉTRICAS  (S = Sᵀ)")
 
def verificar_simetrica(S, label):
    es_sim = np.allclose(S, S.T, atol=1e-10)
    evals  = np.round(np.linalg.eigvalsh(S), 4)
    print(f"\n  Verificaciones para {label}:")
    print(f"    S == Sᵀ  →  {es_sim}")
    print(f"    Eigenvalores (todos reales): {evals}")
    # Descomposición espectral: S = Q·D·Qᵀ
    D_diag, Q = np.linalg.eigh(S)
    reconstruida = Q @ np.diag(D_diag) @ Q.T
    ok = np.allclose(reconstruida, S, atol=1e-8)
    print(f"    S = Q·D·Qᵀ reconstruida  →  {ok}")
 
subtitulo("Ejercicio 1 ── Simétrica 3×3 definida positiva")
S1 = np.array([[4., 2., 1.],
               [2., 5., 3.],
               [1., 3., 6.]])
mostrar("S1", S1)
verificar_simetrica(S1, "S1")
 
subtitulo("Ejercicio 2 ── Simétrica 4×4")
S2 = np.array([[ 2., -1.,  0.,  1.],
               [-1.,  4.,  2., -1.],
               [ 0.,  2.,  6.,  3.],
               [ 1., -1.,  3.,  5.]])
mostrar("S2", S2)
verificar_simetrica(S2, "S2")
 
subtitulo("Ejercicio 3 ── Simétrica 3×3 generada como A·Aᵀ")
np.random.seed(7)
A_base = np.array([[1., 2., 0.],
                   [3., 1., 4.],
                   [2., 5., 1.]])
S3 = A_base @ A_base.T        # siempre simétrica y semidefinida positiva
mostrar("A_base", A_base)
mostrar("S3 = A·Aᵀ", S3)
verificar_simetrica(S3, "S3")
 
# ══════════════════════════════════════════════════════════════
#  SECCIÓN 3 ▸ MATRICES ANTISIMÉTRICAS
#  K = −Kᵀ  →  diagonal = 0, det = 0 si n impar
# ══════════════════════════════════════════════════════════════
titulo("SECCIÓN 3 ── MATRICES ANTISIMÉTRICAS  (K = −Kᵀ)")
 
def verificar_antisimetrica(K, label):
    es_anti = np.allclose(K, -K.T, atol=1e-10)
    diag_cero = np.allclose(np.diag(K), 0, atol=1e-10)
    det_K = np.round(np.linalg.det(K), 6)
    n = K.shape[0]
    evals = np.round(np.linalg.eigvals(K), 4)
    print(f"\n  Verificaciones para {label}:")
    print(f"    K == −Kᵀ  →  {es_anti}")
    print(f"    Diagonal = 0  →  {diag_cero}")
    print(f"    det(K) = {det_K}")
    if n % 2 == 1:
        print(f"    (n={n} impar  →  det debe ser 0: {np.isclose(det_K, 0)})")
    print(f"    Eigenvalores (puramente imaginarios o 0): {evals}")
 
subtitulo("Ejercicio 1 ── Antisimétrica 3×3")
K1 = np.array([[ 0.,  3., -2.],
               [-3.,  0.,  1.],
               [ 2., -1.,  0.]])
mostrar("K1", K1)
verificar_antisimetrica(K1, "K1")
 
subtitulo("Ejercicio 2 ── Antisimétrica 4×4")
K2 = np.array([[ 0.,  4., -1.,  2.],
               [-4.,  0.,  3., -5.],
               [ 1., -3.,  0.,  6.],
               [-2.,  5., -6.,  0.]])
mostrar("K2", K2)
verificar_antisimetrica(K2, "K2")
 
subtitulo("Ejercicio 3 ── Antisimétrica 3×3 generada como (A − Aᵀ)/2")
A_base2 = np.array([[ 3.,  5., -1.],
                    [ 2.,  0.,  4.],
                    [-3.,  1.,  7.]])
K3 = (A_base2 - A_base2.T) / 2
mostrar("A_base2", A_base2)
mostrar("K3 = (A − Aᵀ)/2", K3)
verificar_antisimetrica(K3, "K3")
 
# ── Bonus: Descomposición de una matriz en S + K
print(f"\n  {'─'*55}")
print("  BONUS ── Descomposición A = Simétrica + Antisimétrica")
print(f"  {'─'*55}")
A_test = np.array([[5., 3., -1.],
                   [2., 7.,  4.],
                   [0., 1.,  2.]])
S_part = (A_test + A_test.T) / 2
K_part = (A_test - A_test.T) / 2
mostrar("A_test", A_test)
mostrar("Parte simétrica  S = (A+Aᵀ)/2", S_part)
mostrar("Parte antisimétrica K = (A−Aᵀ)/2", K_part)
print(f"  S + K == A  →  {np.allclose(S_part + K_part, A_test)}")
 
print(f"\n{'='*65}")
print("  ✅  T3 completado — 9 ejercicios de matrices especiales.")
print(f"{'='*65}")