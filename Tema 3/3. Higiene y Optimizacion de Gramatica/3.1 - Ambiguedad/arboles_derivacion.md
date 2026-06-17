# 3.1 Ambigüedad — Dos árboles de derivación

Cadena analizada: `id + id * id`  
Gramática: `E → E + E | E * E | id`

---

## Árbol 1 — La suma se evalúa primero

```
            E
          / | \
         E  +  E
         |    / | \
        id   E  *  E
             |     |
            id    id
```

**Derivación paso a paso:**

```
E
⇒  E + E                  (E → E + E)
⇒  id + E                 (E → id,  izquierda)
⇒  id + E * E             (E → E * E)
⇒  id + id * E            (E → id)
⇒  id + id * id           (E → id)
```

Resultado semántico: `id + (id * id)`  
La multiplicación queda anidada dentro de la suma → suma tiene mayor profundidad.

---
## Árbol 2 — La multiplicación se evalúa primero

```
            E
          / | \
         E  *  E
       / | \   |
      E  +  E  id
      |     |
     id    id
```

**Derivación paso a paso:**

```
E
⇒  E * E                  (E → E * E)
⇒  E + E * E              (E → E + E,  izquierda)
⇒  id + E * E             (E → id)
⇒  id + id * E            (E → id)
⇒  id + id * id           (E → id)
```

Resultado semántico: `(id + id) * id`  
La suma queda anidada dentro de la multiplicación → producto tiene mayor profundidad.

---

## Conclusión

| | Árbol 1 | Árbol 2 |
|-|---------|---------|
| Raíz del árbol | `+` | `*` |
| Semántica | `id + (id * id)` | `(id + id) * id` |
| Valor si id=2 | `2 + (2 * 2) = 6` | `(2 + 2) * 2 = 8` |

La misma cadena produce **resultados numéricos distintos** según el árbol.
Esto demuestra que la gramática es ambigua y no puede usarse en un compilador real.
