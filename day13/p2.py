with open("./day13/data1.txt", "r") as f:
    data = f.read()
    blocks = data.split("\n\n")

PRICE_A = 3
PRICE_B = 1


def parse_block(block):
    button_a, button_b, prize = block.split("\n")
    button_a = button_a.split(": ")[1]
    button_b = button_b.split(": ")[1]
    prize = prize.split(": ")[1]

    xa, ya = button_a.split(", ")
    xa = xa.replace("X", "")
    ya = ya.replace("Y", "")

    xb, yb = button_b.split(", ")
    xb = xb.replace("X", "")
    yb = yb.replace("Y", "")

    xt, yt = prize.split(", ")
    xt = xt.replace("X=", "")
    yt = yt.replace("Y=", "")
    return {
        "xa": int(xa),
        "ya": int(ya),
        "xb": int(xb),
        "yb": int(yb),
        "xt": int(xt) + 10000000000000,
        "yt": int(yt) + 10000000000000,
    }


def compute_b(xa, ya, xb, yb, xt, yt):
    return ((xa * yt) - (ya * xt)) / ((xa * yb) - (ya * xb))


total = 0
for i in blocks:
    v = parse_block(i)
    b = compute_b(v["xa"], v["ya"], v["xb"], v["yb"], v["xt"], v["yt"])
    a = (v["xt"] - (v["xb"] * b)) / v["xa"]
    price = a * PRICE_A + b * PRICE_B
    if price % 1 == 0:
        total += price

print(total)
