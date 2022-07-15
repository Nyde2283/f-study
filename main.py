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




def selection():
    system('cls')
    print('\n')
    print('Sélectionnez la forme de la fonction :\n')
    print('1: f(x) = [i green]a[/i green]x+[i green]b[/i green]')
    print('2: f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]   [i #63666A](indidponible pour le moment)[/i #63666A]')
    print('\n')
    select = int(input('Fontion du type : '))
    system('cls')

    if select == 1: selection_affine()
    elif select == 2: selection()
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
        pass
    elif a==1:
        function += 'x'
    elif a==-1:
        function += '-x'
    else:
        function += f'{a}x'
    if b==0:
        pass
    elif b>0:
        function += f'+{b}'
    else:
        function += f'{b}'
    
    derivee = f'f\'(x) = {a}'

    if a>0:
        zero = round(-b/a, 3)
        signe = ('-', '+')
        variation = '⤴️'
    elif a<0:
        zero = round(-b/a, 3)
        signe = ('+', '-')
        variation = '⤵️'
    elif a==0 and b>0:
        zero = None
        signe = ('+')
        variation = '→'
    elif a==0 and b<0:
        zero = None
        signe = ('-')
        variation = '→'
    else:
        zero = None
        signe = ('', '')
        variation = '→'
    
    table = generate_table_affine(zero, signe, variation)
    affichage(table, function, derivee)



selection()




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