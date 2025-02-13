print("===================================")
print("=======verificar triandulos========")
print("===================================")

a=input("dijite el primer numero: ")

b=input("dijite el segundo numer: ")

c=input("dijite el tercer numero: ")

# proseccing

if a+b >= c:
    r="es posible hacer un triangulo"
elif b+c >= a:
    r="es posible hacer un triangulo"
elif c+a >= b:
    r="es posible hacer un triangulo"
else:
    r="el triangulo no es posible"
pass

#Output
print(r)