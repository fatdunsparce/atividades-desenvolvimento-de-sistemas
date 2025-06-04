class conversortemperatura:
    def celsius_para_fahrenheit(Celcius):
        if not conversortemperatura.__validar(Celcius):
            raise ValueError("Valor Inválido")
        else:
            return (Celcius * 9/5) + 32
        
    def fahrenheit_para_celcius(Fahrenheit):
        if not conversortemperatura.__validar(Fahrenheit):
            raise ValueError("Valor Inválido")
        else:
            return (Fahrenheit - 32) * 5/9
        
    def __validar(Valor):
        try:
            float(Valor)
            return True
        except(ValueError, TypeError):
            return False
        
print(conversortemperatura.celsius_para_fahrenheit(0))
print(conversortemperatura.fahrenheit_para_celcius(0))
print(conversortemperatura.celsius_para_fahrenheit("ABC"))