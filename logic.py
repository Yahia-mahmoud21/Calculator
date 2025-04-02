import math


class Logic():
    def __init__(self):
        self.str = ""

    def operat(self, x, op, y):
        if op == "÷":
            return x / y
        elif op == "x":
            return x * y
        elif op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "^":
            return x ** y

    def sqrt(self, x):
        try:
            return math.sqrt(x)
        except ValueError:
            print("error")
            quit()

    def factorial(self, x):
        try:
            return math.factorial(x)
        except ValueError:
            print("error")
            quit()

    def is_num(self, x):
        try:
            x = x + 0
            return True
        except Exception as e:
            print(f"{e}")
            return False

    def sin(self, z, l, srr):
        sr = srr
        print(sr)

        s = ""
        for i in range(z + 4, l, 1):
            if sr[i] == ")":
                break
            s += sr[i]

        self.str = s
        c = self.math()
        rad = math.radians(c)
        d = round(math.sin(rad), 10)
        sr = sr.replace(f"Sin({s})", str(d))
        self.str = sr
        self.math()

    def cos(self, z, l, srr):
        sr = srr
        print(sr)

        s = ""
        for i in range(z + 4, l, 1):
            if sr[i] == ")":
                break
            s += sr[i]

        self.str = s
        c = self.math()
        rad = math.radians(c)
        d = round(math.cos(rad), 10)
        sr = sr.replace(f"Cos({s})", str(d))
        self.str = sr
        self.math()

    def tan(self, z, l, srr):
        sr = srr
        print(sr)
        s = ""
        for i in range(z + 4, l, 1):
            if sr[i] == ")":
                break
            s += sr[i]

        self.str = s
        c = self.math()
        rad = math.radians(c)
        d = round(math.tan(rad), 10)
        sr = sr.replace(f"Tan({s})", str(d))
        self.str = sr
        self.math()

    def log(self, z, l, srr):
        sr = srr
        s = ""
        for i in range(z + 4, l, 1):
            if sr[i] == ")":
                break
            s += sr[i]

        self.str = s
        c = self.math()

        d = round(math.log10(c), 10)
        sr = sr.replace(f"log({s})", str(d))
        self.str = sr
        self.math()

    def brac(self, z, l, srr):
        sr = srr
        s = ""
        for i in range(z + 1, l, 1):
            if sr[i] == ")":
                break

            s += sr[i]

        self.str = s
        print(s)
        c = self.math()
        sr = sr.replace(f"({s})", str(c))
        self.str = sr
        print(self.str)
        self.math()

    def math(self):
        self.s = self.str

        if "Sin(" in self.s:
            z = self.s.index("S")
            l = len(self.s)
            self.sin(z, l, self.s)

        elif "Cos(" in self.s:
            z = self.s.index("C")
            l = len(self.s)
            self.cos(z, l, self.s)

        elif "Tan(" in self.s:
            z = self.s.index("T")
            l = len(self.s)
            self.tan(z, l, self.s)

        elif "log(" in self.s:
            z = self.s.index("l")
            l = len(self.s)
            self.log(z, l, self.s)
        if "(" in self.s and (self.s.index("(") == 0 or
                              self.str[self.str.index("(") - 1] in ["+", "-", "x", "÷", "=", "√", "^", "!"]):
            z = self.s.index("(")
            l = len(self.s)
            self.brac(z, l, self.s)

        lis1 = self.math_lis(self.s)
        return self.math1(lis1)

    def math_lis(self, s):
        self.s = s
        lis = []
        num = ""
        for i in range(len(self.s)):
            if self.s[i] in ["+", "-", "x", "÷", "=", "√", "^"]:
                if num:
                    lis.append(float(num))
                    num = ""
                if self.s[i] != "=":
                    lis.append(self.s[i])

            elif self.s[i] == "!":
                if num:
                    lis.append(int(num))
                    num = ""
                if self.s[i] != "=":
                    lis.append(self.s[i])
            else:
                num += self.s[i]

        if num:
            lis.append(float(num))
        return lis

    def math1(self, lis):

        if lis[0] == "+":
            lis.remove(lis[0])

        while len(lis) > 1:

            i = 0
            while i < len(lis):
                if lis[i] in ["√"]:
                    result = self.sqrt(lis[i + 1])  # 5
                    lis[i:i + 2] = [result]
                    i = 0
                else:
                    i += 1

            i = 0
            while i < len(lis):
                if lis[i] in ["!"]:
                    result = self.factorial(lis[i - 1])  # 5
                    lis[i - 1:i + 1] = [result]
                    i = 0
                else:
                    i += 1

            i = 0
            while i < len(lis):
                if (lis[i] == "-" and self.is_num(lis[i + 1]) and
                        (lis[i - 1] in ["+", "-", "x", "÷", "^"] or i == 0)):
                    num = float(lis[i] + str(lis[i + 1]))
                    lis[i:i + 2] = [num]
                    i = 0
                else:
                    i += 1

            i = 0
            while i < len(lis):
                if lis[i] == "^":
                    result = self.operat(lis[i - 1], lis[i], lis[i + 1])
                    lis[i - 1:i + 2] = [result]
                    i = 0
                else:
                    i += 1

            i = 0
            while i < len(lis):
                if lis[i] in ["÷", "x"]:
                    result = self.operat(lis[i - 1], lis[i], lis[i + 1])
                    lis[i - 1:i + 2] = [result]
                    i = 0
                else:
                    i += 1

            i = 0
            while i < len(lis):
                if lis[i] in ["-", "+"]:
                    result = self.operat(lis[i - 1], lis[i], lis[i + 1])
                    lis[i - 1:i + 2] = [result]
                    i = 0
                else:
                    i += 1

        return lis[0]
