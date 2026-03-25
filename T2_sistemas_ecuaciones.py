"""
╔══════════════════════════════════════════════════════════════╗
║      T2 - SISTEMAS DE ECUACIONES LINEALES                    ║
║  · 3 sistemas con SOLUCIÓN ÚNICA                             ║
║  · 3 sistemas con INFINITAS SOLUCIONES                       ║
║  · 3 sistemas INCONSISTENTES (sin solución)                  ║
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
 
def mostrar_sistema(A, b):
    vars_ = ["x", "y", "z"]
    print("  Sistema:")
    for i in range(len(b)):
        terminos = []
        for j in range(len(vars_)):
            c = int(A[i][j])
            if c == 0:
                continue
            if c == 1:
                terminos.append(f"{vars_[j]}")
            elif c == -1:
                terminos.append(f"-{vars_[j]}")
            else:
                terminos.append(f"{c}{vars_[j]}")
        ec = " + ".join(terminos).replace("+ -", "- ")
        print(f"    {ec} = {int(b[i])}")
 
def mostrar_aumentada(M):
    n = M.shape[0]
    print("  Matriz aumentada [A|b]:")
    for i in range(n):
        fila = "  | "
        for j in range(n):
            fila += f"{M[i,j]:6.1f} "
        fila += f"| {M[i,n]:6.1f} |"
        print(fila)
 
def gauss_pasos(A_orig, b_orig):
    n = len(b_orig)
    M = np.array([list(A_orig[i]) + [b_orig[i]] for i in range(n)], dtype=float)
    print("\n  Matriz aumentada inicial:")
    mostrar_aumentada(M)
    for col in range(n):
        fila_pivot = np.argmax(np.abs(M[col:, col])) + col
        if fila_pivot != col:
            M[[col, fila_pivot]] = M[[fila_pivot, col]]
            print(f"\n  Intercambiar F{col+1} ↔ F{fila_pivot+1}")
            mostrar_aumentada(M)
        pivot = M[col, col]
        if np.isclose(pivot, 0):
            continue
        for fila in range(col + 1, n):
            factor = M[fila, col] / pivot
            if not np.isclose(factor, 0):
                M[fila] = M[fila] - factor * M[col]
                fs = f"{factor:.4g}".rstrip('0').rstrip('.')
                print(f"\n  F{fila+1} <- F{fila+1} - ({fs}) * F{col+1}")
                mostrar_aumentada(M)
    return M
 
def sustitucion_regresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if np.isclose(M[i, i], 0):
            if not np.isclose(M[i, n], 0):
                return None
            continue
        x[i] = M[i, n]
        for j in range(i + 1, n):
            x[i] -= M[i, j] * x[j]
        x[i] /= M[i, i]
    return x
 
def clasificar(A, b):
    Ab = np.column_stack([A, b])
    rA  = np.linalg.matrix_rank(A)
    rAb = np.linalg.matrix_rank(Ab)
    n   = A.shape[1]
    if rA != rAb:
        return "INCONSISTENTE"
    elif rA == n:
        return "SOLUCION UNICA"
    else:
        return "INFINITAS SOLUCIONES"
 
# ══════════════════════════════════════════════════════════════
#  SECCION 1 -- SOLUCION UNICA
# ══════════════════════════════════════════════════════════════
titulo("SECCION 1 -- SISTEMAS CON SOLUCION UNICA")
 
subtitulo("Ejemplo 1")
A = np.array([[1,1,1],[2,1,1],[1,2,3]], float)
b = np.array([6,9,14], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
M = gauss_pasos(A, b)
x = sustitucion_regresiva(M)
print(f"\n  Sustitucion hacia atras:")
print(f"    z = {x[2]:.4g}")
print(f"    y + z = {int(M[1,2]*x[2]+M[1,3] if False else -M[1,2]):.0f}  =>  y = {x[1]:.4g}")
print(f"    x + y + z = {int(b[0]):.0f}  =>  x = {x[0]:.4g}")
print(f"\n  Solucion: x = {x[0]:.4g},  y = {x[1]:.4g},  z = {x[2]:.4g}")
res = np.max(np.abs(A @ x - b))
print(f"  Verificacion ||Ax - b|| = {res:.2e}  {'OK' if res < 1e-8 else 'ERROR'}")
 
subtitulo("Ejemplo 2")
A = np.array([[1,1,1],[2,3,1],[1,2,3]], float)
b = np.array([3,7,10], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
M = gauss_pasos(A, b)
x = sustitucion_regresiva(M)
print(f"\n  Sustitucion hacia atras:")
print(f"    z = {x[2]:.4g}")
print(f"    y = {x[1]:.4g}")
print(f"    x = {x[0]:.4g}")
print(f"\n  Solucion: x = {x[0]:.4g},  y = {x[1]:.4g},  z = {x[2]:.4g}")
res = np.max(np.abs(A @ x - b))
print(f"  Verificacion ||Ax - b|| = {res:.2e}  {'OK' if res < 1e-8 else 'ERROR'}")
 
subtitulo("Ejemplo 3")
A = np.array([[2,1,1],[1,1,1],[1,2,3]], float)
b = np.array([7,6,14], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
M = gauss_pasos(A, b)
x = sustitucion_regresiva(M)
print(f"\n  Sustitucion hacia atras:")
print(f"    z = {x[2]:.4g}")
print(f"    y = {x[1]:.4g}")
print(f"    x = {x[0]:.4g}")
print(f"\n  Solucion: x = {x[0]:.4g},  y = {x[1]:.4g},  z = {x[2]:.4g}")
res = np.max(np.abs(A @ x - b))
print(f"  Verificacion ||Ax - b|| = {res:.2e}  {'OK' if res < 1e-8 else 'ERROR'}")
 
# ══════════════════════════════════════════════════════════════
#  SECCION 2 -- INFINITAS SOLUCIONES
# ══════════════════════════════════════════════════════════════
titulo("SECCION 2 -- SISTEMAS CON INFINITAS SOLUCIONES")
 
def gauss_inf(A_orig, b_orig):
    n = len(b_orig)
    M = np.array([list(A_orig[i]) + [b_orig[i]] for i in range(n)], dtype=float)
    print("\n  Matriz aumentada inicial:")
    mostrar_aumentada(M)
    for col in range(n):
        pivot = M[col, col]
        if np.isclose(pivot, 0):
            continue
        for fila in range(col + 1, n):
            factor = M[fila, col] / pivot
            if not np.isclose(factor, 0):
                M[fila] = M[fila] - factor * M[col]
                fs = f"{factor:.4g}".rstrip('0').rstrip('.')
                print(f"\n  F{fila+1} <- F{fila+1} - ({fs}) * F{col+1}")
                mostrar_aumentada(M)
    return M
 
subtitulo("Ejemplo 1")
A = np.array([[1,1,1],[2,2,2],[3,3,3]], float)
b = np.array([3,6,9], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
gauss_inf(A, b)
Ab = np.column_stack([A, b])
print(f"\n  La matriz escalonada tiene filas de ceros -> infinitas soluciones")
print(f"  Solucion general:  x = 3 - y - z  (y, z son parametros libres)")
print(f"  rank(A) = {np.linalg.matrix_rank(A)}  |  rank(A|b) = {np.linalg.matrix_rank(Ab)}  -> compatible indeterminado")
 
subtitulo("Ejemplo 2")
A = np.array([[1,1,1],[2,2,2],[1,1,1]], float)
b = np.array([2,4,2], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
gauss_inf(A, b)
Ab = np.column_stack([A, b])
print(f"\n  La matriz escalonada tiene filas de ceros -> infinitas soluciones")
print(f"  Solucion general:  x = 2 - y - z  (y, z son parametros libres)")
print(f"  rank(A) = {np.linalg.matrix_rank(A)}  |  rank(A|b) = {np.linalg.matrix_rank(Ab)}  -> compatible indeterminado")
 
subtitulo("Ejemplo 3")
A = np.array([[2,2,2],[1,1,1],[3,3,3]], float)
b = np.array([8,4,12], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
gauss_inf(A, b)
Ab = np.column_stack([A, b])
print(f"\n  La matriz escalonada tiene filas de ceros -> infinitas soluciones")
print(f"  Solucion general:  x = 4 - y - z  (y, z son parametros libres)")
print(f"  rank(A) = {np.linalg.matrix_rank(A)}  |  rank(A|b) = {np.linalg.matrix_rank(Ab)}  -> compatible indeterminado")
 
# ══════════════════════════════════════════════════════════════
#  SECCION 3 -- INCONSISTENTES
# ══════════════════════════════════════════════════════════════
titulo("SECCION 3 -- SISTEMAS INCONSISTENTES (sin solucion)")
 
def gauss_incon(A_orig, b_orig):
    n = len(b_orig)
    M = np.array([list(A_orig[i]) + [b_orig[i]] for i in range(n)], dtype=float)
    print("\n  Matriz aumentada inicial:")
    mostrar_aumentada(M)
    for col in range(n):
        pivot = M[col, col]
        if np.isclose(pivot, 0):
            continue
        for fila in range(col + 1, n):
            factor = M[fila, col] / pivot
            if not np.isclose(factor, 0):
                M[fila] = M[fila] - factor * M[col]
                fs = f"{factor:.4g}".rstrip('0').rstrip('.')
                print(f"\n  F{fila+1} <- F{fila+1} - ({fs}) * F{col+1}")
                mostrar_aumentada(M)
    for i in range(n):
        if np.allclose(M[i, :n], 0) and not np.isclose(M[i, n], 0):
            print(f"\n  Contradiccion en F{i+1}: 0 = {M[i,n]:.4g}  -> SIN SOLUCION")
    return M
 
subtitulo("Ejemplo 1")
A = np.array([[1,1,1],[1,1,1],[2,2,2]], float)
b = np.array([3,5,6], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
gauss_incon(A, b)
Ab = np.column_stack([A, b])
print(f"  rank(A) = {np.linalg.matrix_rank(A)}  |  rank(A|b) = {np.linalg.matrix_rank(Ab)}  -> inconsistente")
 
subtitulo("Ejemplo 2")
A = np.array([[2,1,1],[2,1,1],[1,1,1]], float)
b = np.array([4,1,2], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
gauss_incon(A, b)
Ab = np.column_stack([A, b])
print(f"  rank(A) = {np.linalg.matrix_rank(A)}  |  rank(A|b) = {np.linalg.matrix_rank(Ab)}  -> inconsistente")
 
subtitulo("Ejemplo 3")
A = np.array([[1,1,1],[2,2,2],[3,3,3]], float)
b = np.array([2,5,6], float)
mostrar_sistema(A, b)
print(f"\n  Clasificacion: {clasificar(A, b)}")
gauss_incon(A, b)
Ab = np.column_stack([A, b])
print(f"  rank(A) = {np.linalg.matrix_rank(A)}  |  rank(A|b) = {np.linalg.matrix_rank(Ab)}  -> inconsistente")
 
print(f"\n{SEP}")
print("  T2 completado -- 9 sistemas clasificados y resueltos.")
print(SEP)