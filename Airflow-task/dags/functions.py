from airflow.models import Variable
# 2.py
# Task 1: Get Input
def get_input():
    input= Variable.set(key="input" , value=["DAG", "variable", "preset"] , serialize_json=True)
    input_data = Variable.get("input", deserialize_json=True)
    return input_data

# Task 2: Get Word Counts and Store in Dictionary
def get_word_counts(input_data):
    word_lengths = {word: len(word) for word in input_data}
    print(word_lengths)
    
# 3.py
# Task 1: Add values a and b
def add_values(**kwargs):
    a = int(Variable.get("a"))
    b = int(Variable.get("b"))
    print(f'value for a: {a}')
    print('value for a:', a)
    print(f'value for b: {b}')
    result = a + b
    print(f"Addition Result: {result}")
    
# Task 2: Subtract values c and d
def subtract_values(**kwargs):
    c = int(Variable.get("c"))
    d = int(Variable.get("d"))
    print(f'value for c: {c}')
    print(f'value for d: {d}')
    result = c - d
    print(f"Subtraction Result: {result}")
    
# Task 3: Multiply values e and f
def multiply_values(**kwargs):
    e = int(Variable.get("e"))
    f = int(Variable.get("f"))
    print(f'value for e: {e}')
    print(f'value for f: {f}')
    result = e * f
    print(f"Multiplication Result: {result}")