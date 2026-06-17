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

## Cadena de prueba

```
id + id * id
```

Esta cadena pertenece a L(G) y puede derivarse de **dos formas distintas**

---

## Por qué es un problema

- El parser no sabe si `+` o `*` tiene mayor precedencia.
- Dos compiladores distintos que usen esta gramática pueden generar
  código diferente para la misma expresión.
- Es imposible construir un parser LL(1) o LALR(1) sobre una gramática ambigua.

---

## Solución: estratificar por precedencia

Se introduce un no terminal por nivel de precedencia:

```
G' = ({E, T, F}, {+, *, (, ), id}, P', E)

P':
    E  →  E + T  |  T        ← precedencia baja  (+)
    T  →  T * F  |  F        ← precedencia media (*)
    F  →  ( E )  |  id       ← átomo
```

G' es **no ambigua**: la cadena `id + id * id` ahora tiene un único árbol,
donde `*` siempre tiene mayor precedencia que `+`.
