def leitura_celcius():
    temperatura = float(input("Qual é o valor da temperatura em celsius? "))
    fahrenheit = (temperatura * 1.8) + 32
    return fahrenheit, temperatura


resultado, temp = leitura_celcius()
print(f"{temp} em Fahrenheit é {resultado}!")