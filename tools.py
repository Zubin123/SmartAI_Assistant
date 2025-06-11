import wikipedia

import math

def calculator(input: str) -> str:
    try:
        input = input.replace("^", "**").replace("sqrt", "math.sqrt")
        result = eval(input, {"__builtins__": {}}, {"math": math})
        return f"The result of {input} is: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

def wiki_search(input: str) -> str:
    try:
        summary = wikipedia.summary(input, sentences=2)
        return f"Wikipedia summary for '{input}':\n{summary}"
    except Exception as e:
        return f"Could not find Wikipedia info: {str(e)}"
