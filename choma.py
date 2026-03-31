class Choma:
    def euklides(self, a, b):
        while a != b:
            if a > b:
                a = a - b
            elif b > a:
                b = b - a
        return a

choma = Choma()

