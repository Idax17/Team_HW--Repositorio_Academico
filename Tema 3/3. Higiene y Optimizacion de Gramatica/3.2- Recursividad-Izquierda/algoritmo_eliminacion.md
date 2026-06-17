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
