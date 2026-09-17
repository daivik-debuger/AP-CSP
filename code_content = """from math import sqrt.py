code_content = """from math import sqrt

def clean(s):
    s = s.replace(" ", "").replace("*", "").replace("−", "-").lower()
    return s

def gcd2(a, b):
    a, b = abs(int(a)), abs(int(b))
    while b != 0:
        a, b = b, a % b
    return a

def gcd_list(values):
    g = 0
    for v in values:
        g = gcd2(g, v)
    return g

def get_number(s):
    if s == "" or s == "+": return 1
    if s == "-": return -1
    return int(s)

def parse_term(t):
    c, xe, ye = 1, 0, 0
    if "x" in t:
        p = t.find("x")
        c = get_number(t[:p])
        rest = t[p + 1:]
        if rest.startswith("^"):
            rest = rest[1:]
            if "y" in rest:
                q = rest.find("y")
                xe = int(rest[:q])
                ypart = rest[q + 1:]
                ye = int(ypart[1:]) if ypart.startswith("^") else (1 if ypart == "" else 0)
            else: xe = int(rest)
        else:
            xe = 1
            if "y" in rest:
                q = rest.find("y")
                ypart = rest[q + 1:]
                ye = int(ypart[1:]) if ypart.startswith("^") else (1 if ypart == "" else 0)
    elif "y" in t:
        p = t.find("y")
        c = get_number(t[:p])
        rest = t[p + 1:]
        ye = int(rest[1:]) if rest.startswith("^") else (1 if rest == "" else 0)
    else: c = int(t)
    return c, xe, ye

def split_terms(s):
    terms, start = [], 0
    for i in range(1, len(s)):
        if s[i] in ["+", "-"]:
            terms.append(s[start:i])
            start = i
    terms.append(s[start:])
    return terms

def polynomial(s):
    if "=" in s: s = s.split("=")[0]
    if s.startswith("+"): s = s[1:]
    return [parse_term(p) for p in split_terms(s) if p != ""]

def monomial(c, x, y):
    if c == 0: return "0"
    out = "-" if c == -1 else (str(c) if c != 1 or (x == 0 and y == 0) else "")
    if x > 0: out += "x" + ("^" + str(x) if x != 1 else "")
    if y > 0: out += "y" + ("^" + str(y) if y != 1 else "")
    return out

def polynomial_text(terms):
    out, first = "", True
    for c, x, y in terms:
        if c == 0: continue
        term = monomial(abs(c), x, y)
        if first:
            if c < 0: out += "-"
            out += term
            first = False
        else:
            out += ("-" if c < 0 else "+") + term
    return "0" if out == "" else out

def find_gcf(terms):
    g = gcd_list([t[0] for t in terms])
    minx, miny = terms[0][1], terms[0][2]
    for t in terms:
        if t[1] < minx: minx = t[1]
        if t[2] < miny: miny = t[2]
    return g, minx, miny

def remove_gcf(terms, g, xg, yg):
    return [(c // g, x - xg, y - yg) for c, x, y in terms]

def fraction(n, d):
    n, d = int(n), int(d)
    if d < 0: n, d = -n, -d
    g = gcd2(n, d)
    n, d = n // g, d // g
    return str(n) if d == 1 else str(n) + "/" + str(d)

def perfect_square(n):
    if n < 0: return None
    r = int(sqrt(n))
    return r if r * r == n else None

def factor_text(p, q):
    s = "x" if p == 1 else ("-x" if p == -1 else str(p) + "x")
    if q > 0: s += "+" + str(q)
    elif q < 0: s += str(q)
    return "(" + s + ")"

def find_quadratic_factors(a, b, c):
    for p in range(-abs(a), abs(a) + 1):
        if p == 0 or a % p != 0: continue
        r = a // p
        for q in range(-abs(c), abs(c) + 1):
            if q == 0 or c % q != 0: continue
            s = c // q
            if p * s + q * r == b:
                if p < 0: p, q, r, s = -p, -q, -r, -s
                if r < 0: r, s = -r, -s
                return p, q, r, s
    return None

def quadratic_formula(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        print("No real solutions.")
        return
    root = perfect_square(d)
    if root != None:
        n1, n2, den = -b + root, -b - root, 2 * a
        print("x =", fraction(n1, den))
        if n1 != n2: print("x =", fraction(n2, den))
    else:
        print("x=(-b +/- sqrt(" + str(d) + "))/(" + str(2 * a) + ")")

def solve_factored(s):
    factors, i = [], 0
    while i < len(s):
        if s[i] == "(":
            j = s.find(")", i)
            if j == -1: return False
            factors.append(polynomial(s[i + 1:j]))
            i = j + 1
        else: i += 1
    if len(factors) == 0: return False
    
    print("\\nZERO PRODUCT PROP")
    for t in factors: print(polynomial_text(t) + "=0")
    print("\\nSOLUTIONS")
    for t in factors:
        a, b = 0, 0
        for c, x, y in t:
            if x == 1 and y == 0: a += c
            elif x == 0 and y == 0: b += c
        if a != 0: print("x = " + fraction(-b, a))
    return True

def solve_quadratic(terms, equation, gcf_text):
    a, b, c = 0, 0, 0
    for co, x, y in terms:
        if y != 0: return False
        if x == 2: a += co
        elif x == 1: b += co
        elif x == 0: c += co
        else: return False
    if a == 0: return False
    
    print("\\nQUADRATIC")
    print("a=", a, " b=", b, " c=", c)
    print("b^2-4ac =", b * b - 4 * a * c)
    
    f = find_quadratic_factors(a, b, c)
    if f != None:
        p, q, r, s = f
        f1, f2 = factor_text(p, q), factor_text(r, s)
        print("\\nFACTORING\\nac =", a * c)
        print("FACTORED:\\n" + gcf_text + f1 + f2)
        if equation:
            print("\\nSOLUTIONS:")
            print("x = " + fraction(-q, p))
            print("x = " + fraction(-s, r))
        return True
    
    print("\\nQUAD FORMULA")
    if equation:
        print("SOLUTIONS:")
        quadratic_formula(a, b, c)
    else:
        print("Does not factor.")
    return True

def main():
    print("=== FACTOR_M ===")
    s = input("Problem: ")
    s = clean(s)
    if s == "": return
    equation = "=" in s
    
    if "(" in s and ")" in s and equation:
        if solve_factored(s): return
        
    try: terms = polynomial(s)
    except:
        print("ERROR: format x^2")
        return

    if len(terms) == 0: return

    print("\\nORIGINAL:\\n" + polynomial_text(terms))

    g, xg, yg = find_gcf(terms)
    gcf_text = ""
    if g != 1 or xg != 0 or yg != 0:
        gcf_text = monomial(g, xg, yg)
        print("\\nGCF =", gcf_text)
        terms = remove_gcf(terms, g, xg, yg)
        print("FACTORED:\\n" + gcf_text + "(" + polynomial_text(terms) + ")")

    if len(terms) == 2:
        t1, t2 = terms[0], terms[1]
        if t1[2] == 0 and t2[2] == 0 and t1[1] == 2 and t2[1] == 0:
            a, b = t1[0], t2[0]
            sa, sb = perfect_square(abs(a)), perfect_square(abs(b))
            if sa != None and sb != None and a > 0 and b < 0 and a == 1:
                ans = "(x-" + str(sb) + ")(x+" + str(sb) + ")"
                print("\\nDIFF OF SQUARES\\n" + gcf_text + ans)
                if equation: print("\\nx =", sb, "\\nx =", -sb)
                return

    if len(terms) >= 2:
        if solve_quadratic(terms, equation, gcf_text): return

    print("\\nFINAL FORM:")
    if gcf_text != "": print(gcf_text + "(" + polynomial_text(terms) + ")")
    else: print(polynomial_text(terms))

if __name__ == "__main__":
    main()
"""

with open('factorti.py', 'w', encoding='utf-8') as f:
    f.write(code_content)

print("File created successfully: factorti.py")