menu = [
    {
        'nombre':'Cazuela',
        'precio':3000,
        'kcal':800,
        'ingredientes':['agua','zanahoria','zapallo','choclo','carne','ajito','PAPA'],
    },
    {
        'nombre':'Completo',
        'precio':1500
    },
    {
        'nombre':'Churrasco',
        'precio':2000
    }
]

#agregar a lista de diccionarios
menu.append(
    {
        'nombre':'Sopaipilla Calle',
        'precio':200,
        'ingredientes':['zapallo','harina','aceite','aceite motor']
    }
)

menu[2]['precio'] = 1200

for item in menu:
    print (item['nombre'], ' $', item['precio'])
