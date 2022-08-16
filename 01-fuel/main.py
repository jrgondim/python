from time import sleep
from progress.spinner import MoonSpinner

p = 0.7

print("\x1b[2J\x1b[1;1H")
g = float(input("Gasolina R$ : "))
e = float(input("Etanol R$ : "))
r = (e/g)


with MoonSpinner('Processing…') as bar:
    for i in range(100):
        sleep(0.01)
        bar.next()
print("\x1b[2J\x1b[1;1H")

print("Gasolina R$ :", g)
print("Etanol R$ :", e)

if r > p:
    print(format(r*100, '.2f'),"%    |  Abasteca com gasolina")
elif r <= p:
    print(format(r*100,'.2f'),"%     |  Abasteca com etanol")
