"""
TRABAJO FINAL - ÁLGEBRA LINEAL
DETERMINANTES
Verificación con Python (SymPy)
 
3 matrices calculadas con métodos distintos:
  - Matriz A → Eliminación de Gauss
  - Matriz B → Regla de Sarrus
  - Matriz C → Expansión por Cofactores
"""
 
import sympy as sp
 
print("=" * 55)
print("              DETERMINANTES")
print("=" * 55)
 
# ─────────────────────────────────────────────────────────
# MATRIZ A — Eliminación de Gauss (triangulación)
# ─────────────────────────────────────────────────────────
print("\n── MÉTODO: Eliminación de Gauss ─────────────────────")
 
A = sp.Matrix([[1, 2, 3],
               [2, 5, 3],
               [1, 0, 8]])
 
print("\n  A =")
sp.pprint(A)
 
# Triangulación manual con operaciones de fila
M = A.tolist()
print("\n  Pasos de triangulación:")
 
# F2 ← F2 - 2*F1
factor1 = sp.Rational(M[1][0], M[0][0])
print(f"  F2 ← F2 − ({factor1}) × F1")
for j in range(3):
    M[1][j] = M[1][j] - factor1 * M[0][j]
 
# F3 ← F3 - 1*F1
factor2 = sp.Rational(M[2][0], M[0][0])
print(f"  F3 ← F3 − ({factor2}) × F1")
for j in range(3):
    M[2][j] = M[2][j] - factor2 * M[0][j]
 
# F3 ← F3 - (M[2][1]/M[1][1])*F2
factor3 = sp.Rational(M[2][1], M[1][1])
print(f"  F3 ← F3 − ({factor3}) × F2")
for j in range(3):
    M[2][j] = M[2][j] - factor3 * M[1][j]
 
T = sp.Matrix(M)
print("\n  Matriz triangular superior:")
sp.pprint(T)
det_gauss = T[0,0] * T[1,1] * T[2,2]
print(f"\n  det(A) = {T[0,0]} × {T[1,1]} × {T[2,2]} = {det_gauss}")
print(f"  Verificación SymPy: det(A) = {A.det()}")
print(f"  ¿Coincide? {det_gauss == A.det()}")
 
# ─────────────────────────────────────────────────────────
# MATRIZ B — Regla de Sarrus
# ─────────────────────────────────────────────────────────
print("\n── MÉTODO: Regla de Sarrus ──────────────────────────")
 
B = sp.Matrix([[2,  1, 3],
               [0, -1, 4],
               [5,  2, 0]])
 
print("\n  B =")
sp.pprint(B)
 
# Diagonales principales (+) y secundarias (−)
b = B.tolist()
diag_pos = (b[0][0]*b[1][1]*b[2][2] +
            b[0][1]*b[1][2]*b[2][0] +
            b[0][2]*b[1][0]*b[2][1])
diag_neg = (b[0][2]*b[1][1]*b[2][0] +
            b[0][0]*b[1][2]*b[2][1] +
            b[0][1]*b[1][0]*b[2][2])
 
print(f"\n  Diagonales (+): {b[0][0]}·{b[1][1]}·{b[2][2]}"
      f" + {b[0][1]}·{b[1][2]}·{b[2][0]}"
      f" + {b[0][2]}·{b[1][0]}·{b[2][1]} = {diag_pos}")
print(f"  Diagonales (−): {b[0][2]}·{b[1][1]}·{b[2][0]}"
      f" + {b[0][0]}·{b[1][2]}·{b[2][1]}"
      f" + {b[0][1]}·{b[1][0]}·{b[2][2]} = {diag_neg}")
 
det_sarrus = diag_pos - diag_neg
print(f"  det(B) = {diag_pos} − {diag_neg} = {det_sarrus}")
print(f"  Verificación SymPy: det(B) = {B.det()}")
print(f"  ¿Coincide? {det_sarrus == B.det()}")
 
# ─────────────────────────────────────────────────────────
# MATRIZ C — Expansión por Cofactores (fila 1)
# ─────────────────────────────────────────────────────────
print("\n── MÉTODO: Expansión por Cofactores (fila 1) ────────")
 
C = sp.Matrix([[3, 2, 1],
               [1, 0, 2],
               [4, 1, 3]])
 
print("\n  C =")
sp.pprint(C)
 
# Expansión por la primera fila: Σ c_{0j} * C_{0j}
c = C.tolist()
print("\n  Expansión por fila 1:  det = c₁₁·C₁₁ + c₁₂·C₁₂ + c₁₃·C₁₃")
 
cofactores = []
for j in range(3):
    menor = C.minor_submatrix(0, j)
    Cof   = ((-1)**(0+j)) * menor.det()
    cofactores.append(Cof)
    signo = "+" if (-1)**(j) > 0 else "−"
    print(f"  C[0,{j}]: signo={signo}  menor={menor.tolist()}  "
          f"det(menor)={menor.det()}  → cofactor = {Cof}")
 
det_cof = sum(c[0][j] * cofactores[j] for j in range(3))
print(f"\n  det(C) = {c[0][0]}·({cofactores[0]})"
      f" + {c[0][1]}·({cofactores[1]})"
      f" + {c[0][2]}·({cofactores[2]}) = {det_cof}")
print(f"  Verificación SymPy: det(C) = {C.det()}")
print(f"  ¿Coincide? {det_cof == C.det()}")
 
print("\n" + "=" * 55)
print("  Los 3 determinantes verificados correctamente.")
print("=" * 55)