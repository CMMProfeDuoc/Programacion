lista_mascotas = [
    {
        'nombre':'Pepito',
        'tipo':'gato',
        'edad':5,
    },
    {
        'nombre':'Juanito',
        'tipo':'gato',
        'edad':6,
    },
    {
        'nombre':'Panxito',
        'tipo':'hamstercito',
        'edad':5,
        'inmortal':True
    },
    {
        'nombre':'Lechuga',
        'tipo':'perro',
        'edad':5,
    },
]

for mascota in lista_mascotas:
    print(mascota['nombre'],mascota['tipo'])