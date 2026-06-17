# 3.2 Recursividad por la Izquierda — Algoritmo de eliminación

## Fórmula general

Para una producción de la forma:

```
A  →  A α₁ | A α₂ | ... | β₁ | β₂ | ...
```

donde los `βᵢ` no comienzan por A, se reescribe como:

```
A   →  β₁ A' | β₂ A' | ...
A'  →  α₁ A' | α₂ A' | ... | ε
```

---

## Aplicación paso a paso

### Gramática original

```
E  →  E + T
E  →  T
T  →  id
```

---

### Paso 1 — Identificar la producción recursiva

```
E → E + T
```

Se extrae: `α = "+ T"`

---

### Paso 2 — Identificar la producción base

```
E → T
```

Se extrae: `β = "T"`

---

### Paso 3 — Crear el nuevo no terminal E'

Se introduce `E'` (E primo) para acumular las repeticiones.

---

### Paso 4 — Reescribir las producciones

```
E   →  T E'
E'  →  + T E'  |  ε
T   →  id
```

`E'` maneja todos los `+ T` adicionales de forma iterativa,
sin llamarse a sí misma al inicio → apto para LL(1).

---

## Verificación: derivar `id + id + id`

```
E
⇒  T E'                (E  → T E')
⇒  id E'               (T  → id)
⇒  id + T E'           (E' → + T E')
⇒  id + id E'          (T  → id)
⇒  id + id + T E'      (E' → + T E')
⇒  id + id + id E'     (T  → id)
⇒  id + id + id ε      (E' → ε)
=  id + id + id   ✓
```

---

## Comparación antes / después

| | Gramática original | Gramática corregida |
|-|--------------------|---------------------|
| Recursión izquierda | Sí (`E → E + T`) | No |
| Apta para LL(1) | No | Sí |
| Lenguaje generado | `{id (+ id)*}` | `{id (+ id)*}` (igual) |

La gramática resultante es **equivalente** (genera el mismo lenguaje)
pero sin la patología que impedía construir el parser.
