class EjerciciosCiclicosPY:
  def CalcularFactorialNum(self):
    contador=1
    resultado=1
    numero=int(input("Ingrese el numero a calcular el Factorial:"))
    if(numero>0):
      while(contador<numero):
        contador=contador+1
        resultado=resultado*contador
    print(f"El factorial de{numero} Es: {resultado}")

obj=EjerciciosCiclicosPY()
obj.CalcularFactorialNum()