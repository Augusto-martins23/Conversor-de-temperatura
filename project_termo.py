def celsius_to_fahrenheit(c):
    fahrenheit = (c*1.8) + 32
    return (fahrenheit)
def fahrenheit_to_celsius(f):
    celsius = (f-32)/1.8
    return (celsius)
def celsius_to_kelvin(c):
    kelvin = c + 273.15
    return (kelvin)
def kelvin_to_celsius(k):
    celsius = k - 273.15
    return (celsius)
def fahrenheit_to_kelvin(f):
    kelvin = ((f-32)*1.8)+ 32
    return (kelvin)
def kelvin_to_fahrenheit(k):
    fahrenheit = ((k - 273.15)*1.8)+32
    return (fahrenheit)
while True:
    print('1.Celsius')
    print('2.Fahrenheit')
    print('3.Kelvin')
    choice = int(input('Opção: '))
    if choice == 1:
        print('1.Celsius para Fahrenheit')
        print('2. Celsius para Kelvin')
        escolha = int(input('\nOpção: '))
        if escolha == 1:
            temperatura = float(input('\nTemperatura em °C: '))
            resultado = celsius_to_fahrenheit(temperatura)
            print(f'{resultado:.4f}= ºF')
            break
        elif escolha == 2:
            temperatura = float(input('\nTemperatura em °C: '))
            resultado = celsius_to_kelvin(temperatura)
            print(f'{resultado:.4f}= °K')
            break
    elif choice == 2:
        print('1.Fahrenheit para celsius')
        print('2. Fahrenheit para Kelvin')
        escolha = int(input('\nOpção: '))
        if escolha == 1:
            temperatura = float(input('\nTemperatura em °F: '))
            resultado = fahrenheit_to_celsius(temperatura)
            print(f'{resultado:.4f}= ºC')
            break
        elif escolha == 2:
            temperatura = float(input('\nTemperatura em °F: '))
            resultado = fahrenheit_to_kelvin(temperatura)
            print(f'{resultado}= K')
            break
    elif choice == 3:
        print('1.Kelvin para Celsius')
        print('2.Kelvin para Fahrenheit')
        escolha = int(input('\nOpção: '))
        if escolha == 1:
            temperatura = float(input('\nTemperatura em Kelvin: '))
            resultado = kelvin_to_celsius(temperatura)
            print(f'{resultado:.4f} °C')
            break
        elif escolha == 2:
            temperatura = float(input('\nTemperatura em Kelvin'))
            resultado = kelvin_to_fahrenheit(temperatura)
            print(f'{resultado:.4f} °F')
            break
    else:
        print('invalido!\n')