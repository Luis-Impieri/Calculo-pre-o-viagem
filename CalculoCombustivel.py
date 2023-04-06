preço = float(input('Qual o preço médio do litro de combustível na sua região?'))
quilometragem = float(input('Quantos KM o seu carro consegue fazer com um litro de combustível?'))
distancia = float(input('O quão longe é o seu destino em KM?'))

A = (distancia / quilometragem)
B = (A * preço)

print('O seu gasto de dinheiro com combustível na sua viágem será de: ',B, 'reais')