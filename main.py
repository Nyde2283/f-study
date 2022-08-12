from os import system
try:
    from rich.table import Table
except:
    print('\nLe bibliothèque Rich n\'est pas installé sur votre ordinateur. Elle est indispensable pour afficher les tableaux.')
    print('Pour plus d\'informations consultez la page PyPi ( https://pypi.org/project/rich/ ) \nou la page GitHub ( https://github.com/Textualize/rich ) du projet.')
    print('\nPour installer Rich :')
    print('- Ouvrez un terminal en administrateur')
    print('- Tapez la commande: pip install rich')
    input('\n Appuyez sur Enter pour quitter...')
from rich import print, box
from math import sqrt




def selection():
    system('cls')
    print('\n')
    print('Sélectionnez la forme de la fonction :\n')
    print('1: f(x) = [i green]a[/i green]x+[i green]b[/i green]')
    print('2: f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]   [i #63666A](indidponible pour le moment)[/i #63666A]')
    print('\n')
    select = input('Fontion du type : ')
    system('cls')

    if select == '1': selection_affine()
    elif select == '2': selection_2nd_degre()
    else: selection()

def selection_affine():
    print()
    print('f(x) = [i green blink]a[/i green blink]x+[i green]b[/i green]\n')
    a = float(input('a = '))
    if a.is_integer(): a = int(a)

    system('cls')
    print()
    print(f'f(x) = [green]{a}[/green]x+[i green blink]b[/i green blink]\n')
    b = float(input('b = '))
    if b.is_integer(): b = int(b)

    anal_affine(a, b)

def selection_2nd_degre():
    print()
    print('f(x) = [i green blink]a[/i green blink]x²+[i green]b[/i green]x+[i green]c[/i green]\n')
    a = float(input('a = '))
    if a.is_integer(): a = int(a)

    system('cls')
    print()
    print(f'f(x) = [green]{a}[/green]x²+[i green blink]b[/i green blink]x+[i green]c[/i green]\n')
    b = float(input('b = '))
    if b.is_integer(): b = int(b)

    system('cls')
    print()
    print(f'f(x) = [green]{a}[/green]x²+[green]{b}[/green]x+[i green blink]c[/i green blink]\n')
    c = float(input('c = '))
    if c.is_integer(): c = int(c)

    if a!=0: anal_2nd_degre(a, b, c)
    else: anal_affine(b, c)

def generate_table_affine(zero, signe, varia):
    '''Génère un tableau de signe et de variation pour une fonction affine'''
    if zero!=None:
        t = [['', 'x=', '-∞', '', f'{zero}', '', '+∞'],
             ['signe', 'f(x)', '', signe[0], '0', signe[1], ''],
             ['varia', 'f(x)', '', varia, '', varia, '']]
    else:
        t = [['', 'x=', '-∞', '', '+∞'],
             ['signe', 'f(x)', '', signe[0], ''],
             ['varia', 'f(x)', '', varia, '']]
    return t

def anal_affine(a, b):
    '''Analyse une fonction de la forme f(x) = ax+b'''
    assert type(a) in (int, float), f'a doit être de type int ou float (type(a) = {type(a)})'
    assert type(b) in (int, float), f'b doit être de type int ou float (type(b) = {type(b)})'

    function = 'f(x) = '
    if a==0:
        if b==0: function += '0' #0x+0 = x
    else:
        if a==1: function += 'x' #1x = x
        elif a==-1: function += '-x' #-1x = -x
        else: function += f'{a}x'
        if b>0: function += f'+{b}' #pour éviter d'afficher 5x+-8 (à la place de 5x-8) par exemple
        else: function += f'{b}'

    derivee = f'[#B4009E]f\'[/#B4009E](x) = {a}'

    if a>0: #courbe croissante
        zero = round(-b/a, 3)
        signe = ('-', '+')
        variation = '⤴️'
    elif a<0: #courbe décroissante
        zero = round(-b/a, 3)
        signe = ('+', '-')
        variation = '⤵️'
    elif a==0 and b>0: #courbe constante et f(x)>0
        zero = None
        signe = ('+')
        variation = '→'
    elif a==0 and b<0: #courbe constante et f(x)<0
        zero = None
        signe = ('-')
        variation = '→'
    else: #courbe constante et f(x)=0
        zero = None
        signe = ('0')
        variation = '→'
    
    table = generate_table_affine(zero, signe, variation)
    affichage(table, function, derivee)


def anal_2nd_degre(a, b, c):
    '''Analyse une fonction de la forme f(x) = ax²+bx+c'''

    def f(x):
        return a*x**2+b*x+c

    #Convertie la fonction en string
    function = 'f(x) = '
    if a==1: function += 'x²'
    elif a==-1: function += '-x²'
    else: function += f'{a}x²'
    if b==1: function += '+x'
    elif b==-1: function += '-x'
    elif b>0: function += f'+{b}x'
    elif b<0: function += f'{b}x'
    if c>0: function += f'+{c}'
    elif c<0: function += f'{c}'

    derivee = f'f\'(x) = {a*2}x'
    if b>0: derivee += f'+{b}'
    elif b<0: derivee += f'{b}'

    Sx = -b/(2*a)
    S = (round(Sx, 3), f(Sx, 3))

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

    [t_signe, t_varia] = generate_table_2nd_degre(a, racines, S)

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

def affichage(t, function, derivee):
    assert type(t)==list, f't doit être une liste (type(t) = {type(t)})'
    assert len(t)>=2, f'Le tableau est trop petit (nb_lignes = {len(t)} < 2)'
    assert len(t[0])>=5, f'Le tableau est trop petit (nb_colonnes = {len(t[0])} < 4)'
    for i in range(len(t)):
        assert len(t[i])==len(t[0]), f'Les lignes du tableau n\'ont pas la même longueur (len t[0]= {len(t[0])}, len t[{i}]= {len(t[i])}'

    table = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
    for i in range(len(t[0])):
        table.add_column(t[0][i], justify='center') #ajout des en-têtes de colonnes un par un (première ligne de t)
    for i in range(1, len(t)):
        table.add_row(*t[i]) #ajout des lignes une par une

    system('cls')
    print('\n')
    print(table) # affichage de la table
    print()
    print(function, derivee, sep='\n')
    print('\n')
    print('[#63666A]Certaines valeurs peuvent être arrondies.[/#63666A]')
    input('\nAppuyer sur Enter pour quitter...')



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