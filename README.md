# python-rules-engine
## Setup
```
pip install flask
pip install libcst

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
    "formula": "s_result = a * b * c \nif s_result > 10:\n    s_result_2 = 2222"
}
```


## Output
```
{
    "tracking": {
        "if_s_result_GreaterThan_10": true
    },
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
