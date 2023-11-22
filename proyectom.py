from math import *
from math import sqrt
from sympy import symbols, lambdify, diff, ln

def main():
  #menu de seleccion
  print("Seleccione el metodo")
  print("1 Biseccion")
  print("2 Punto fijo")
  print("3 Newton-Raphson")
  x=input("Metodo a usar: ")
  if x=="1":
      print("-----Metodo de Biseccion-----")
      print("Ingrese una función")
      fx = input("Por ejemplo: 'tan(x) + x**2 - x'. Solo ingrese la expresión, no las comillas: ")

      # lambda toma el argumento de x
      fun = lambda x: eval(fx)

      while True:
          n = input("Ingrese el número máximo de iteraciones que desea: ")
          try:
              n = int(n)
          except ValueError:
              print("¡Error! Ingrese un número entero.")
              continue

          print("Ingrese el intervalo de la forma [a, b]")
          a = input("Ingrese el valor de a: ")
          b = input("Ingrese el valor de b: ")

          try:
              a, b = float(a), float(b)
          except ValueError:
              print("¡Error! Ingrese solo números.")
              continue

          if a >= b:
              print("¡Error! Asegúrese de que a < b.")
              continue

          iteracion, an, bn = 0, a, b
          while iteracion < n:
              fa, fb = fun(an), fun(bn)
              if fa * fb > 0:
                  print("No es posible aplicar el método de la bisección ya que f(a) * f(b) > 0")
                  break
              else:  # en este caso ocurre que f(a) * f(b) < 0
                  cn = (an + bn) / 2.0
                  fc = fun(cn)
                  if fc * fa < 0:
                      bn = cn
                  else:
                      an = cn
              iteracion += 1

          print("Resultado:")
          print("La iteración terminó en n =", iteracion)
          print("La raíz aproximada de la función", fx, "es x =", cn, "en el intervalo [", a, ",", b, "]")
          break

            # punto fijo
  elif x=="2":
      print("-----Metodo de Punto fijo-----")
      def punto_fijo(g, x0, tolerancia, max_iter):
          """
          Encuentra una solución de la ecuación g(x) = x mediante el método del punto fijo.

          :param g: La función g(x)
          :param x0: Aproximación inicial
          :param tolerancia: Tolerancia para la convergencia
          :param max_iter: Número máximo de iteraciones
          :return: La aproximación de la solución y el número de iteraciones realizadas
          """
          iteracion = 0
          x = x0

          while iteracion < max_iter:
              x_anterior = x
              x = g(x_anterior)

              # Verifica la convergencia
              if abs(x - x_anterior) < tolerancia:
                  return x, iteracion + 1

              iteracion += 1

          # Si no converge en el número máximo de iteraciones
          raise Exception("El método del punto fijo no converge después de {} iteraciones.".format(max_iter))


      # Solicitar datos al usuario
      def obtener_datos_usuario():
          g_expresion = input("Ingrese la expresión de la función g(x): ")
          g = lambda x: eval(g_expresion)  # Convierte la expresión a una función lambda

          x0 = float(input("Ingrese la aproximación inicial (x0): "))
          tolerancia = float(input("Ingrese la tolerancia: "))
          max_iter = int(input("Ingrese el número máximo de iteraciones: "))

          return g, x0, tolerancia, max_iter


      if __name__ == "__main__":
          # Obtener datos del usuario
          g, x0, tolerancia, max_iter = obtener_datos_usuario()

          # Aplica el método del punto fijo
          try:
              solucion, num_iteraciones = punto_fijo(g, x0, tolerancia, max_iter)
              print("\nSolución encontrada:", solucion)
              print("Número de iteraciones:", num_iteraciones)
          except Exception as e:
              print("\nError:", e)


  elif x=="3":


    def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
        iteracion = 0
        x = x0

        while abs(f(x)) > tol and iteracion < max_iter:
            x = x - f(x) / f_prime(x)
            iteracion += 1

        return x, iteracion

    if __name__ == "__main__":
        # Solicitar la función al usuario
        x = symbols('x')
        fx = input("Ingrese la función f(x) en términos de x (puedes usar sin, cos, log, etc.): ")

        # Convertir la expresión a una función simbólica
        f = lambdify(x, fx, 'numpy')

        # Calcular la derivada de la función
        f_prime = lambdify(x, diff(fx, x), 'numpy')

        # Solicitar la aproximación inicial al usuario
        x0 = float(input("Ingrese la aproximación inicial x0: "))

        # Llamar a la función Newton-Raphson
        raiz_aprox, num_iteraciones = newton_raphson(f, f_prime, x0)

        # Mostrar resultados
        print("Resultado:")
        print(f"Raíz aproximada: {raiz_aprox}")
        print(f"Número de iteraciones: {num_iteraciones}")


  else:
      print("Error en la eleccion")

while True:
    main()
    reiniciar = input("¿Quieres reiniciar el programa? (s/n): ")
    if reiniciar.lower() != 's':
        break