import math

allowed_names = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
allowed_names.update({"abs": abs, "round": round})

def safe_eval(expr):
    return eval(expr, {"__builtins__": {}}, allowed_names)

history = []

while True:
    user_input = input("Enter expression ('history' to view, 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    if user_input.lower() == 'history':
        for expr, res in history:
            print(f"{expr} = {res}")
        continue

    try:
        result = safe_eval(user_input)
        history.append((user_input, result))
        print("Result:", result)
    except Exception as e:
        print("Invalid expression:", e)
