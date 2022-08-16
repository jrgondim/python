#define indice
v = 0.7

#define consumo do veiculo
gk = float(input('Quantos km/l seu veiculo faz na GASOLINA? :'))
ek = float(input('Quantos km/l seu veiculo faz na ETANOL? :'))

# define periodos de utilizacao e km
w = float(input('Quantos dias na semana usa o carro? :'))

k = float(input('Quantos km percorre por dia com o carro? :'))

d = float(input('Quantos dias no mes faz esse percurso? :'))

#recebe os valores dos combustiveis
g = float(input('preco da gasolina :'))
e = float(input('preco da etanol :'))
#calcula percental
p = (e/g)
#mostra comparativo
print(round(p, 2), '%')
#exibe mensagem de sugestao de uso de combustivel mais indicado

if(p>=v):
    r1 = (k/gk)*g
    r2 = ((k/gk)*g) * w
    r3 = ((k/gk)*g) * d
    print('Use gasolina!')
    print('Reais por dia :', round(r1, 2) )
    print('Reais por semana :', round(r2, 2))    
    print('Reais por mês :', round(r3, 2))
else:
    r4 = (k/ek)*e
    r5 = ((k/ek)*e) * w
    r6 = ((k/ek)*e) * d
    print('Use etanol')
    print('Reais por dia :', round(r4, 2) )
    print('Reais por semana :', round(r5, 2))    
    print('Reais por mês :', round(r6, 2))
