print("----------------------------------------------")
print("Ejercicio 5.")
print("Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.Cree una función que encuentre el palíndromo más grande hecho delproducto de dos números de 3 dígitos.")

nicial = []

def buscar_pal():
    for i in range (100,1000):
      
      o = i*i
      print(o)
      multi_top = 913
      multi_top2 = 993
      palindrómico_top = multi_top * multi_top2
      search = palindrómico_top
    print(f"El numero palindromico producto de 3 cifras mas grande encontrado es: {search}. ")
    

        

        # print(if str(x)  == str(x)[::-1] ])
        
buscar_pal()
    

