from os import system
try:
    from rich.table import Table
except:
    print('\nLa bibliothèque Rich n\'est pas installé sur votre ordinateur. Elle est indispensable pour afficher les tableaux.')
    print('Pour plus d\'informations consultez la page PyPi ( https://pypi.org/project/rich/ ) \nou la page GitHub ( https://github.com/Textualize/rich ) du projet.')
    print('\nPour installer Rich :')
    print('- Ouvrez un terminal en administrateur')
    print('- Tapez la commande: python -m pip install rich')
    input('\n Appuyez sur Enter pour quitter...')
from rich.console import Console
from rich import print, box
from math import sqrt
from sys import version_info

assert version_info >= (3, 10), 'f-study nécessite Python 3.10 ou supérieur'


console = Console(highlight=False)




def selection():
    system('cls')
    console.print('\n')
    console.print('Sélectionnez la forme de la fonction :\n')
    console.print('[#61d6d6]1[/#61d6d6]: f(x) = [i green]a[/i green]x+[i green]b[/i green]')
    console.print('[#61d6d6]2[/#61d6d6]: f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]')
    console.print('\n')
    select = input('Fontion du type : ')
    system('cls')

    if select == '1': selection_affine()
    elif select == '2': selection_2nd_degre()
    else: selection()

def def_number(msg, var):
    system('cls')
    console.print(msg)
    response = console.input(f'{var} = ')
    try:
        response = float(response)
    except:
        i = response.index('/')
        numerateur = float(response[:i])
        denominateur = float(response[i+1:])
        response = numerateur/denominateur
    if response.is_integer(): response = int(response)
    return response

def selection_affine():
    msg = '\nf(x) = [i green blink]a[/i green blink]x+[i green]b[/i green]\n'
    a = def_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x+[i green blink]b[/i green blink]\n'
    b = def_number(msg, 'b')

    anal_affine(a, b)

def selection_2nd_degre():
    msg = '\nf(x) = [i green blink]a[/i green blink]x²+[i green]b[/i green]x+[i green]c[/i green]\n'
    a = def_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[i green blink]b[/i green blink]x+[i green]c[/i green]\n'
    b = def_number(msg, 'b')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[green]{round(b, 3)}[/green]x+[i green]c[/i green]\n'
    c = def_number(msg, 'c')

    if a!=0: anal_2nd_degre(a, b, c)
    else: anal_affine(b, c)


def function_to_string(facteurs: list):
    function = 'f(x) = '

    for i in range(len(facteurs)):
        facteurs[i] = round(facteurs[i], 3)

    match facteurs:
        case [a, b]:
                if a==1: function += 'x'
                elif a==-1: function += '-x'
                elif a!=0: function += f'{a}x'
                else:
                    if b!=0: function += f'{b}'
                    else: function += '0'
                    return function
                
                if b>0: function += f'+{b}'
                elif b<0: function += f'{b}'

        case [a, b, c]:
                if a==1: function += 'x²'
                elif a==-1: function += '-x²'
                else: function += f'{a}x²'

                if b==1: function += '+x'
                elif b==-1: function += '-x'
                elif b>0: function += f'+{b}x'
                elif b<0: function += f'{b}x'
                
                if c>0: function += f'+{c}'
                elif c<0: function += f'{c}'
    return function


def anal_affine(a, b):
    '''Analyse une fonction de la forme f(x) = ax+b'''

    function = function_to_string([a, b])

    derivee = f'f\'(x) = {round(a, 3)}'

    if a!=0: x0 = round(-b/a, 3)
    else: x0 = None
    
    tableaux = generate_table_affine(x0, a, b)
    affichage(tableaux, function, derivee)

def generate_table_affine(x0, a, b):
    '''Génère un tableau de signe et de variation pour une fonction affine'''
    match x0:
        case None:
            t_signe = [['', 'x=', '-∞', '', '+∞']]
            if b>0:
                t_signe.append(['signe', 'f(x)', '', '+', ''])
            elif b<0:
                t_signe.append(['signe', 'f(x)', '', '-', ''])
            else:
                t_signe.append(['signe', 'f(x)', '', '0', ''])
            t_signe.append(['varia', 'f(x)', '', '→', ''])
            return [t_signe]
        case _:
            t_signe = [['', 'x=', '-∞', '', f'{x0}', '', '+∞']]
            if a>0:
                t_signe.append(['signe', 'f(x)', '', '-', '0', '+', ''])
            else:
                t_signe.append(['signe', 'f(x)', '', '+', '0', '-', ''])

    t_varia = [['', 'x=', '-∞', '', '+∞']]
    if a>0:
        t_varia.append(['signe', 'f\'(x)', '', '+', ''])
        t_varia.append(['varia', 'f(x)', '', '↗', ''])
    elif a<0:
        t_varia.append(['signe', 'f\'(x)', '', '-', ''])
        t_varia.append(['varia', 'f(x)', '', '↘', ''])

    return [t_signe, t_varia]

def anal_2nd_degre(a, b, c):
    '''Analyse une fonction de la forme f(x) = ax²+bx+c'''

    def f(x):
        return a*x**2+b*x+c

    #Convertie la fonction en string
    function = function_to_string([a, b, c])

    derivee = f'f\'(x) = {round(a*2, 3)}x'
    if b>0: derivee += f'+{round(b, 3)}'
    elif b<0: derivee += f'{round(b, 3)}'

    Sx = -b/(2*a)
    S = (round(Sx, 3), round(f(Sx), 3))

    delta = b**2-4*a*c
    if delta>0:
        x1 = round((-b-sqrt(delta))/(2*a), 3)
        x2 = round((-b+sqrt(delta))/(2*a), 3)
        if x1<x2:
            racines = (x1, x2)
        else:
            racines = (x2, x1)
    elif delta==0:
        x0 = round(-b/(2*a), 3)
        racines = (x0)
    else:
        racines = None

    tableaux = generate_table_2nd_degre(a, racines, S)
    affichage(tableaux, function, derivee)

def generate_table_2nd_degre(a, racines, S):
    match racines:
        case [x1, x2]:
            t_signe = [['', 'x=', '-∞', '', f'{racines[0]}', '', f'{racines[1]}', '', '+∞']]
            if a>0:
                t_signe.append(['signe', 'f(x)', '', '+', '0', '-', '0', '+', ''])
            else:
                t_signe.append(['signe', 'f(x)', '', '-', '0', '+', '0', '-', ''])
        case [x0]:
            t_signe = [['', 'x=', '-∞', '', f'{racines[0]}', '', '+∞']]
            if a>0:
                t_signe.append(['signe', 'f(x)', '', '+', '0', '+', ''])
            else:
                t_signe.append(['signe', 'f(x)', '', '-', '0', '-', ''])
        case _:
            t_signe = [['', 'x=', '-∞', '', '+∞']]
            if a>0:
                t_signe.append(['signe', 'f(x)', '', '+', ''])
            else:
                t_signe.append(['signe', 'f(x)', '', '-', ''])
    
    t_varia = [['', 'x=', '-∞', '', f'{S[0]}', '', '+∞']]
    if a>0:
        t_varia.append(['signe', 'f\'(x)', '', '-', '0', '+', ''])
        t_varia.append(['varia', 'f(x)', '', '↘', f'{S[1]}', '↗', ''])
    else:
        t_varia.append(['signe', 'f\'(x)', '', '+', '0', '-', ''])
        t_varia.append(['varia', 'f(x)', '', '↗', f'{S[1]}', '↘', ''])

    return [t_signe, t_varia]

def affichage(tableaux, function, derivee):
    system('cls')
    console.print('\n')
    for t in tableaux:
        table = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
        for i in range(len(t[0])):
            table.add_column(t[0][i], justify='center') #ajout des en-têtes de colonnes un par un (première ligne de t)
        for i in range(1, len(t)):
            table.add_row(*t[i]) #ajout des lignes une par une
        console.print(table) # affichage de la table
    console.print('\n')
    console.print(function, derivee, sep='\n')
    console.print('\n')
    console.print('[#818488]Certaines valeurs peuvent être arrondies.[/#818488]')
    print('\n\n[#818488]Pour faire une demande de nouvelle fonctionnalité \nou pour signaler un bug : [/#818488]https://github.com/Nyde2283/f-study/issues   [#63666A](Ctrl+Click)[/#63666A]')
    console.input('\n\n[black on white]Appuyer sur Entrée pour quitter...[/black on white]')


while True:
    selection()




# Find GitHub repo here : https://github.com/Nyde2283/f-study


#    Copyright 2022 CHEVEREAU Edwyn

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.