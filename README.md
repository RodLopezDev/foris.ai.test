# General

Version de Python

```
Python 3.11.4
```

# Run

Archivo como input de ejecución

```
cat data.txt | python main.py
```

Cargar el nombre del archivo como parámetro

```
python main.py data.txt
```

# Tests

Instalar pytest

```
pip install pytest pytest-cov coverage
```

Correr tester

```
pytest
```

Correr test con coverage

```
coverage run -m pytest
```

Visualize HTML Coverage

```
coverage html
```

# Documentación

- [Esqueleto solución](./development/1.primeros-pasos.md)
- [Primera versión](./development/2.primer-iteracion.md)
- [Mejorando solución, event map](./development/3.refactor.md)
- [Desacoplando reporteador e input de datos](./development/4.refactor-v2.md)
- [Strategy para input de datos](./development/5.input-data.md)
