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
