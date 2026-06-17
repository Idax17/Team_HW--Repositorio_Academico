# 3.2 Recursividad por la Izquierda — Gramática problemática

## Definición

Una gramática tiene **recursividad por la izquierda** cuando existe un
no terminal A tal que:

```
A ⇒⁺ A α
```

para alguna cadena α. Es decir, A puede derivar en una cadena que comienza
por el propio A.

Hay dos tipos:

| Tipo | Definición | Ejemplo |
|------|-----------|---------|
| Directa | A aparece inmediatamente en su propia producción | `E → E + T` |
| Indirecta | A aparece tras varios pasos de derivación | `A → B α`, `B → A β` |

---

## Gramática con recursión izquierda directa

```
G = ({E, T}, {+, id}, P, E)

P:
    E  →  E + T       ← recursión izquierda: E es el primer símbolo
    E  →  T
    T  →  id
```

---
## Por qué es un problema para parsers LL

Un parser de descenso recursivo implementa cada no terminal como una función:

```python
def E():
    E()       # ← llama a E() antes de consumir ningún token
    match('+')
    T()
```

Al llamar a `E()`, lo primero que hace es llamar a `E()` de nuevo,
que a su vez llama a `E()`, y así hasta agotar la pila → **bucle infinito**.

Los parsers **LL(k)** no pueden manejar gramáticas con recursión izquierda.
Es obligatorio eliminarla antes de construir el analizador.

---

## Identificación del patrón

Para la producción `E → E + T | T` se identifican:

- **Producción recursiva**: `E → E + T`  → extrae `α = + T`
- **Producción base** (no recursiva): `E → T`  → extrae `β = T`
