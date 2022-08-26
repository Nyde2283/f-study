from sys import version_info
assert version_info >= (3, 10), 'f-study nécessite Python 3.10 ou supérieur'

try:
    from rich.console import Console
except:
    print('\nLa bibliothèque Rich n\'est pas installé sur votre ordinateur. Elle est indispensable pour afficher les tableaux.')
    print('Pour plus d\'informations consultez la page PyPi ( https://pypi.org/project/rich/ ) \nou la page GitHub ( https://github.com/Textualize/rich ) du projet.')
    print('\nPour installer Rich :')
    print('- Ouvrez un terminal en administrateur')
    print('- Tapez la commande: python -m pip install rich')
    input('\n Appuyez sur Enter pour quitter...')
from os import system
from traitement_fonctions import affine, second_degre


console = Console(highlight=False)




#############
# selection #
#############

def selection(options: list[str]):
    system('cls')
    console.print('\n\nSélectionnez la forme de la fonction :\n')
    for i in range(len(options)):
        console.print(f'[#61d6d6]{i+1}[/#61d6d6]: {options[i]}')
    select = console.input('\n\nFonction du type : ')
    system('cls')

    if select == '1': selection_affine()
    elif select == '2': selection_second_degre()
    else: selection(options)

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

    affine(a, b)

def selection_second_degre():
    msg = '\nf(x) = [i green blink]a[/i green blink]x²+[i green]b[/i green]x+[i green]c[/i green]\n'
    a = def_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[i green blink]b[/i green blink]x+[i green]c[/i green]\n'
    b = def_number(msg, 'b')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[green]{round(b, 3)}[/green]x+[i green]c[/i green]\n'
    c = def_number(msg, 'c')

    if a!=0: second_degre(a, b, c)
    else: affine(b, c)


#############
# programme #
#############

options = [
    'f(x) = [i green]a[/i green]x+[i green]b[/i green]',
    'f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]'
]
while True:
    try:
        selection(options)
    except:
        pass
# utiliser match pour select



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