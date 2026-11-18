while True:
    expr = input()
    if expr == "exit":
        break

    parts = expr.split()
    a = float(parts[0])
    op = parts[1]
    b = float(parts[2])

    if op == "+":
        res = a + b
        print(int(res) if res.is_integer() else res)
    elif op == "-":
        res = a - b
        print(int(res) if res.is_integer() else res)
    elif op == "*":
        res = a * b
        print(int(res) if res.is_integer() else res)
    elif op == "/":
        if b == 0:
            print("деление на ноль")
        else:
            print(a / b)
    else:
        print("неизвестная операция")

