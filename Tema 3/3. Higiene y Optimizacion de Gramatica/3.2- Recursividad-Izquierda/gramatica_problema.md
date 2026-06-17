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