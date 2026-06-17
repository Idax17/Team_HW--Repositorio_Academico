# 3.3 Factorización por la Izquierda — El problema del dangling else

## Definición

Una gramática requiere **factorización por la izquierda** cuando dos o más
producciones para el mismo no terminal comparten un prefijo común.

Un parser LL(1) no puede decidir cuál producción aplicar con un solo símbolo
de anticipación (lookahead), porque el prefijo no permite distinguir entre
las alternativas.

---

## Caso de estudio: dangling else

El ejemplo canónico es la sentencia `if-then-else` en lenguajes de programación.

### Gramática original

```
G:
    S  →  if E then S else S     ← producción 1
    S  →  if E then S            ← producción 2
```
