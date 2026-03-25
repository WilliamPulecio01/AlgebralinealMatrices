"""
TRABAJO FINAL - ÁLGEBRA LINEAL
SISTEMAS DE ECUACIONES LINEALES
Verificación con Python (SymPy)
 
Casos:
  - 2 sistemas con solución única
  - 2 sistemas con infinitas soluciones
  - 2 sistemas sin solución (inconsistentes)
"""
 
import sympy as sp
 
x, y, z = sp.symbols('x y z')
 
print("=" * 55)
print("       SISTEMAS DE ECUACIONES LINEALES")
print("=" * 55)
 
# ─────────────────────────────────────────────────────────
# CASO 1: SOLUCIÓN ÚNICA
# ─────────────────────────────────────────────────────────
print("\n── SOLUCIÓN ÚNICA ──────────────────────────────────")
 
# Sistema 1
print("\nSistema 1:")
print("  x +  y +  z = 6")
print("  2x -  y +  z = 3")
print("  x + 2y -  z = 3")
s1 = [
    sp.Eq(x + y + z,   6),
    sp.Eq(2*x - y + z, 3),
    sp.Eq(x + 2*y - z, 3)
]
sol1 = sp.solve(s1, (x, y, z))
print("  Solución:", sol1)
 
A1 = sp.Matrix([[1,1,1],[2,-1,1],[1,2,-1]])
b1 = sp.Matrix([6, 3, 3])
print("  Verificación A·x = b →", A1 * sp.Matrix(list(sol1.values())) == b1)
 
# Sistema 2
print("\nSistema 2:")
print("  2x +  y -  z = 1")
print("   x -  y + 2z = 3")
print("  3x +  y +  z = 7")
s2 = [
    sp.Eq(2*x + y - z,  1),
    sp.Eq(x - y + 2*z,  3),
    sp.Eq(3*x + y + z,  7)
]
sol2 = sp.solve(s2, (x, y, z))
print("  Solución:", sol2)
 
A2 = sp.Matrix([[2,1,-1],[1,-1,2],[3,1,1]])
b2 = sp.Matrix([1, 3, 7])
print("  Verificación A·x = b →", A2 * sp.Matrix(list(sol2.values())) == b2)
 
# ─────────────────────────────────────────────────────────
# CASO 2: INFINITAS SOLUCIONES
# ─────────────────────────────────────────────────────────
print("\n── INFINITAS SOLUCIONES ─────────────────────────────")
 
# Sistema 3
print("\nSistema 3:")
print("   x +  y +  z = 3")
print("  2x + 2y + 2z = 6  (fila 2 = 2 × fila 1)")
print("   x -  y +  z = 1")
s3 = [
    sp.Eq(x + y + z,       3),
    sp.Eq(2*x + 2*y + 2*z, 6),
    sp.Eq(x - y + z,       1)
]
sol3 = sp.solve(s3, (x, y, z), dict=True)
print("  Solución (parámetros libres):", sol3)
Ab3 = sp.Matrix([[1,1,1,3],[2,2,2,6],[1,-1,1,1]])
print("  rank(A) =", Ab3[:, :3].rank(),
      "| rank(A|b) =", Ab3.rank(),
      "→ compatible indeterminado")
 
# Sistema 4
print("\nSistema 4:")
print("   x + 2y +  z = 4")
print("  2x + 4y + 2z = 8  (fila 2 = 2 × fila 1)")
print("   x -  y +  z = 1")
s4 = [
    sp.Eq(x + 2*y + z,       4),
    sp.Eq(2*x + 4*y + 2*z,  8),
    sp.Eq(x - y + z,         1)
]
sol4 = sp.solve(s4, (x, y, z), dict=True)
print("  Solución (parámetros libres):", sol4)
Ab4 = sp.Matrix([[1,2,1,4],[2,4,2,8],[1,-1,1,1]])
print("  rank(A) =", Ab4[:, :3].rank(),
      "| rank(A|b) =", Ab4.rank(),
      "→ compatible indeterminado")
 
# ─────────────────────────────────────────────────────────
# CASO 3: SIN SOLUCIÓN (INCONSISTENTES)
# ─────────────────────────────────────────────────────────
print("\n── SIN SOLUCIÓN (INCONSISTENTES) ────────────────────")
 
# Sistema 5
print("\nSistema 5:")
print("   x +  y +  z = 2")
print("  2x + 2y + 2z = 5  (fila 2 = 2×fila1 pero 5 ≠ 2×2)")
print("   x -  y +  z = 1")
s5 = [
    sp.Eq(x + y + z,       2),
    sp.Eq(2*x + 2*y + 2*z, 5),
    sp.Eq(x - y + z,       1)
]
sol5 = sp.solve(s5, (x, y, z))
print("  Solución:", sol5, "← conjunto vacío = sin solución")
Ab5 = sp.Matrix([[1,1,1,2],[2,2,2,5],[1,-1,1,1]])
print("  rank(A) =", Ab5[:, :3].rank(),
      "| rank(A|b) =", Ab5.rank(),
      "→ inconsistente (rangos distintos)")
 
# Sistema 6
print("\nSistema 6:")
print("   x +  y +  z = 1")
print("  2x + 2y + 2z = 3  (fila 2 = 2×fila1 pero 3 ≠ 2×1)")
print("   x +  y +  z = 4  (fila 3 = fila 1 pero 4 ≠ 1)")
s6 = [
    sp.Eq(x + y + z,       1),
    sp.Eq(2*x + 2*y + 2*z, 3),
    sp.Eq(x + y + z,       4)
]
sol6 = sp.solve(s6, (x, y, z))
print("  Solución:", sol6, "← conjunto vacío = sin solución")
Ab6 = sp.Matrix([[1,1,1,1],[2,2,2,3],[1,1,1,4]])
print("  rank(A) =", Ab6[:, :3].rank(),
      "| rank(A|b) =", Ab6.rank(),
      "→ inconsistente (rangos distintos)")
 
print("\n" + "=" * 55)
print("  Todos los sistemas verificados correctamente.")
print("=" * 55)