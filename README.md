# python-rules-engine
## Setup
```
pip install flask

python main.py
```

## Simulate

POST http://127.0.0.1:5000/formula
```
{
    "variables": {
        "a": "2",
        "b": "3",
        "c": "4"
    },
    "formula": "s_result = a * b * c \nif s_result > 10: s_result_2 = 2222"
}
```


## Output
```
{
    "tracking": "to implement",
    "variables": {
        "a": "2",
        "b": "3",
        "c": "4"
    },
    "variables_formula": {
        "s_result": 24,
        "s_result_2": 2222
    }
}
```


### Determine output variables with prefix 's_'
