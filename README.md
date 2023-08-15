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


```python
def main():
    # 1. Get data
    content = """
        Student Marco
        ...
    """
    lines = content.splitlines()

    # 2. Set a global state to persist data
    state = {}

    # 3. Process data
    for line in lines:
        if not line.strip():
            continue
        items = line.strip().split(" ")
        # Do something <- make algorithm this
        print(state, items)

    # 4. Visualize data result
    reporter = ReportFormat(state) # <- Implement solut
    print(reporter)


if __name__ == "__main__":
    main()
```