
"""
TRABAJO FINAL - ÁLGEBRA LINEAL
PROPIEDADES DE LOS DETERMINANTES
Verificación con Python (SymPy)
 
Las 9 propiedades con 2 ejemplos cada una:
  P1  det(I) = 1
  P2  Fila o columna de ceros → det = 0
  P3  Dos filas iguales → det = 0
  P4  Intercambio de filas → det cambia de signo
  P5  Fila multiplicada por k → det se multiplica por k
  P6  det(A·B) = det(A) · det(B)
  P7  det(Aᵀ) = det(A)
  P8  det(A⁻¹) = 1 / det(A)
  P9  det(k·A) = kⁿ · det(A)
"""
 
import sympy as sp
 
def sep(n, titulo):
    print(f"\n{'='*55}")
    print(f"  PROPIEDAD {n}: {titulo}")
    print(f"{'='*55}")
 
def ok(cond):
    return "✓ VERIFICADO" if cond else "✗ ERROR"
 
# ─────────────────────────────────────────────────────────
# P1: det(I) = 1
# ─────────────────────────────────────────────────────────
sep(1, "det(Iₙ) = 1")
 
I3 = sp.eye(3)
I4 = sp.eye(4)
print(f"\n  Ejemplo 1 — Identidad 3×3:")
sp.pprint(I3)
print(f"  det(I₃) = {I3.det()}  →  {ok(I3.det() == 1)}")
 
print(f"\n  Ejemplo 2 — Identidad 4×4:")
sp.pprint(I4)
print(f"  det(I₄) = {I4.det()}  →  {ok(I4.det() == 1)}")
 
# ─────────────────────────────────────────────────────────
# P2: Fila (o columna) de ceros → det = 0
# ─────────────────────────────────────────────────────────
sep(2, "Fila o columna de ceros → det = 0")
 
P2a = sp.Matrix([[1, 2, 3],
                 [0, 0, 0],
                 [4, 5, 6]])
P2b = sp.Matrix([[3, 0, -1, 2],
                 [1, 0,  4, 5],
                 [2, 0,  0, 3],
                 [4, 0,  1,-1]])
 
print(f"\n  Ejemplo 1 — Fila 2 es de ceros (3×3):")
sp.pprint(P2a)
print(f"  det = {P2a.det()}  →  {ok(P2a.det() == 0)}")
 
print(f"\n  Ejemplo 2 — Columna 2 es de ceros (4×4):")
sp.pprint(P2b)
print(f"  det = {P2b.det()}  →  {ok(P2b.det() == 0)}")
 
# ─────────────────────────────────────────────────────────
# P3: Dos filas iguales → det = 0
# ─────────────────────────────────────────────────────────
sep(3, "Dos filas iguales → det = 0")
 
P3a = sp.Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [1, 2, 3]])    # fila 1 == fila 3
P3b = sp.Matrix([[ 2, -1, 0,  3],
                 [ 1,  4,-2,  5],
                 [ 3,  0, 1, -1],
                 [ 1,  4,-2,  5]])  # fila 2 == fila 4
 
print(f"\n  Ejemplo 1 — Filas 1 y 3 iguales (3×3):")
sp.pprint(P3a)
print(f"  det = {P3a.det()}  →  {ok(P3a.det() == 0)}")
 
print(f"\n  Ejemplo 2 — Filas 2 y 4 iguales (4×4):")
sp.pprint(P3b)
print(f"  det = {P3b.det()}  →  {ok(P3b.det() == 0)}")
 
# ─────────────────────────────────────────────────────────
# P4: Intercambio de dos filas → det cambia de signo
# ─────────────────────────────────────────────────────────
sep(4, "Intercambio de filas → det cambia de signo")
 
P4 = sp.Matrix([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 10]])
# Intercambio correcto de filas usando indexing directo
r0 = list(P4.row(0))
r1 = list(P4.row(1))
r2 = list(P4.row(2))
P4_swap = sp.Matrix([r1, r0, r2])  # F1 ↔ F2
 
print(f"\n  Ejemplo 1 — Intercambio F1 ↔ F2 (3×3):")
print("  Original:"); sp.pprint(P4)
print("  Con F1 ↔ F2:"); sp.pprint(P4_swap)
print(f"  det(A)      = {P4.det()}")
print(f"  det(A_swap) = {P4_swap.det()}")
print(f"  {ok(P4_swap.det() == -P4.det())}")
 
P4b = sp.Matrix([[ 2,  1,-1, 0],
                 [ 0,  3, 2, 1],
                 [ 1,  0, 4,-1],
                 [-1,  2, 0, 3]])
rb0 = list(P4b.row(0))
rb1 = list(P4b.row(1))
rb2 = list(P4b.row(2))
rb3 = list(P4b.row(3))
P4b_swap = sp.Matrix([rb0, rb3, rb2, rb1])  # F2 ↔ F4
 
print(f"\n  Ejemplo 2 — Intercambio F2 ↔ F4 (4×4):")
print(f"  det(A)      = {P4b.det()}")
print(f"  det(A_swap) = {P4b_swap.det()}")
print(f"  {ok(P4b_swap.det() == -P4b.det())}")
 
# ─────────────────────────────────────────────────────────
# P5: Multiplicar una fila por k → det se multiplica por k
# ─────────────────────────────────────────────────────────
sep(5, "Fila × k → det se multiplica por k")
 
P5 = sp.Matrix([[1, 2, 3],
                [1, 0, 1],
                [2, 1, 0]])
k = 2
P5_mod = P5.copy()
P5_mod[0, :] = k * P5_mod[0, :]   # multiplicar fila 1 por k
 
print(f"\n  Ejemplo 1 — k = {k}, fila 1 escalada (3×3):")
print("  Original:"); sp.pprint(P5)
print(f"  det(A)     = {P5.det()}")
print(f"  Con fila 1 × {k}:"); sp.pprint(P5_mod)
print(f"  det(A_mod) = {P5_mod.det()}")
print(f"  k × det(A) = {k} × {P5.det()} = {k * P5.det()}")
print(f"  {ok(P5_mod.det() == k * P5.det())}")
 
P5b = sp.Matrix([[3, -1, 2],
                 [1,  4, 0],
                 [2,  1,-3]])
k2 = sp.Rational(-3)
P5b_mod = P5b.copy()
P5b_mod[1, :] = k2 * P5b_mod[1, :]   # multiplicar fila 2 por -3
 
print(f"\n  Ejemplo 2 — k = {k2}, fila 2 escalada (3×3):")
print(f"  det(A)     = {P5b.det()}")
print(f"  det(A_mod) = {P5b_mod.det()}")
print(f"  k × det(A) = {k2} × {P5b.det()} = {k2 * P5b.det()}")
print(f"  {ok(P5b_mod.det() == k2 * P5b.det())}")
 
# ─────────────────────────────────────────────────────────
# P6: det(A·B) = det(A) · det(B)
# ─────────────────────────────────────────────────────────
sep(6, "det(A·B) = det(A) · det(B)")
 
P6A = sp.Matrix([[1, 2, 3],
                 [0, 1, 4],
                 [5, 6, 0]])
P6B = sp.Matrix([[2, 0, 1],
                 [0, 3, 2],
                 [1, 0, 4]])
 
print(f"\n  Ejemplo 1 — Matrices 3×3:")
print(f"  det(A)         = {P6A.det()}")
print(f"  det(B)         = {P6B.det()}")
print(f"  det(A·B)       = {(P6A * P6B).det()}")
print(f"  det(A)·det(B)  = {P6A.det() * P6B.det()}")
print(f"  {ok((P6A * P6B).det() == P6A.det() * P6B.det())}")
 
P6C = sp.Matrix([[ 2,  1,-1, 0],
                 [ 0,  3, 2, 1],
                 [ 1,  0, 4,-1],
                 [-1,  2, 0, 3]])
P6D = sp.Matrix([[ 1,  2, 0, 1],
                 [ 3, -1, 2, 0],
                 [ 0,  1, 3, 2],
                 [ 2,  0,-1, 1]])
 
print(f"\n  Ejemplo 2 — Matrices 4×4:")
print(f"  det(A)         = {P6C.det()}")
print(f"  det(B)         = {P6D.det()}")
print(f"  det(A·B)       = {(P6C * P6D).det()}")
print(f"  det(A)·det(B)  = {P6C.det() * P6D.det()}")
print(f"  {ok((P6C * P6D).det() == P6C.det() * P6D.det())}")
 
# ─────────────────────────────────────────────────────────
# P7: det(Aᵀ) = det(A)
# ─────────────────────────────────────────────────────────
sep(7, "det(Aᵀ) = det(A)")
 
P7 = sp.Matrix([[1, 2, 3],
                [1, 0, 1],
                [2, 1, 0]])
 
print(f"\n  Ejemplo 1 — Matriz 3×3:")
print("  A:"); sp.pprint(P7)
print("  Aᵀ:"); sp.pprint(P7.T)
print(f"  det(A)  = {P7.det()}")
print(f"  det(Aᵀ) = {P7.T.det()}")
print(f"  {ok(P7.det() == P7.T.det())}")
 
P7b = sp.Matrix([[1, 2, 3, 4],
                 [0, 1, 2, 3],
                 [0, 0, 1, 2],
                 [0, 0, 0, 1]])
 
print(f"\n  Ejemplo 2 — Matriz 4×4 (triangular):")
print(f"  det(A)  = {P7b.det()}")
print(f"  det(Aᵀ) = {P7b.T.det()}")
print(f"  {ok(P7b.det() == P7b.T.det())}")
 
# ─────────────────────────────────────────────────────────
# P8: det(A⁻¹) = 1 / det(A)
# ─────────────────────────────────────────────────────────
sep(8, "det(A⁻¹) = 1 / det(A)")
 
P8 = sp.Matrix([[2, 1, 0],
                [1, 3, 1],
                [0, 1, 2]])
 
print(f"\n  Ejemplo 1 — Matriz 3×3:")
print(f"  det(A)    = {P8.det()}")
print(f"  det(A⁻¹)  = {P8.inv().det()}")
print(f"  1/det(A)  = {sp.Rational(1, P8.det())}")
print(f"  {ok(P8.inv().det() == sp.Rational(1, P8.det()))}")
 
P8b = sp.Matrix([[3,  1, 2, 0],
                 [1,  4,-1, 1],
                 [2, -1, 5, 2],
                 [0,  1, 2, 3]])
 
print(f"\n  Ejemplo 2 — Matriz 4×4:")
print(f"  det(A)    = {P8b.det()}")
print(f"  det(A⁻¹)  = {P8b.inv().det()}")
print(f"  1/det(A)  = {sp.Rational(1, P8b.det())}")
print(f"  {ok(P8b.inv().det() == sp.Rational(1, P8b.det()))}")
 
# ─────────────────────────────────────────────────────────
# P9: det(k·A) = kⁿ · det(A)
# ─────────────────────────────────────────────────────────
sep(9, "det(k·A) = kⁿ · det(A)   (n = orden de la matriz)")
 
P9 = sp.Matrix([[1, 2, 3],
                [0, 4, 5],
                [1, 0, 6]])
k3, n3 = 2, 3
 
print(f"\n  Ejemplo 1 — k = {k3}, A de orden {n3}×{n3}:")
print(f"  det(A)       = {P9.det()}")
print(f"  det({k3}·A)     = {(k3*P9).det()}")
print(f"  {k3}³·det(A)    = {k3**n3 * P9.det()}")
print(f"  {ok((k3*P9).det() == k3**n3 * P9.det())}")
 
P9b = sp.Matrix([[ 2,  1,-1, 0],
                 [ 0,  3, 2, 1],
                 [ 1,  0, 4,-1],
                 [-1,  2, 0, 3]])
k4, n4 = 3, 4
 
print(f"\n  Ejemplo 2 — k = {k4}, A de orden {n4}×{n4}:")
print(f"  det(A)       = {P9b.det()}")
print(f"  det({k4}·A)     = {(k4*P9b).det()}")
print(f"  {k4}⁴·det(A)    = {k4**n4 * P9b.det()}")
print(f"  {ok((k4*P9b).det() == k4**n4 * P9b.det())}")
 
# ─────────────────────────────────────────────────────────
# RESUMEN
# ─────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print("  RESUMEN — 9 PROPIEDADES")
print(f"{'='*55}")
props = [
    "P1 : det(I) = 1",
    "P2 : Fila/col ceros → det = 0",
    "P3 : Dos filas iguales → det = 0",
    "P4 : Intercambio de filas → det cambia signo",
    "P5 : Fila × k → det × k",
    "P6 : det(A·B) = det(A)·det(B)",
    "P7 : det(Aᵀ) = det(A)",
    "P8 : det(A⁻¹) = 1/det(A)",
    "P9 : det(k·A) = kⁿ·det(A)",
]
for p in props:
    print(f"  ✅  {p}")
 
print(f"\n{'='*55}")
print("  Todas las propiedades verificadas con SymPy.")
print(f"{'='*55}")
 