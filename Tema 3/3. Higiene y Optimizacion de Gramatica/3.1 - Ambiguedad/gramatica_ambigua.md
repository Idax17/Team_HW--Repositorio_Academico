# 3.1 Ambigüedad — Gramática de ejemplo

## Definición

Una gramática G es **ambigua** si existe al menos una cadena `w ∈ L(G)`
que admite dos o más árboles de derivación distintos.

El compilador no puede determinar cuál estructura sintáctica es la correcta,
lo que produce código objeto incorrecto o con semántica inesperada.

---

## Gramática ambigua

```
G = ({E}, {+, *, id}, P, E)

P:
    E  →  E + E
    E  →  E * E
    E  →  id
```

Esta gramática no define precedencia ni asociatividad entre `+` y `*`.
Cualquier cadena con ambos operadores admite más de un árbol.