from math import sqrt
from os import system
from platform import system as platform
from sys import version_info

from decorators import *
from error import *

prog_info = {
    'version': 'v0.2.2',
    'release_link': 'https://github.com/Nyde2283/f-study/releases/tag/v0.2.2',
    'py_version': f'{version_info.major}.{version_info.minor}.{version_info.micro}',
    'platforme': platform()
}
def_debug_info(prog_info)

if version_info<(3, 10): BadPythonVersion.raise_and_exit()

try:
    from rich.console import Console
except Exception as e:
    RichNotFound.raise_and_exit(e)
from rich import box
from rich.table import Table


console = Console(highlight=False) #désactive le formatage auto pour éviter des incohérences dans la coloration




def cls() -> None:
    """Supprime le contenu de la console"""
    if platform()=='Windows': system('cls')
    else: system('clear')

@check_args
def get_number(msg: str, var: str) -> (float | int):
    """Demande un nombre en input puis le return

    Args:
        msg (str): message à afficher avant l'input
        var (str): nom correspondant à la variable demandé à l'utilisateur

    Returns:
        float | int: nombre donné par l'utilisateur
    """
    response = None
    while response==None:
        cls()
        console.print(msg)
        response = console.input(f'{var} = ')
        try:
            response = float(response) #test si l'input est un nombre
        except:
            try:
                i = response.index('/') #test si le nombre peut être une fraction
                numerateur = float(response[:i])
                denominateur = float(response[i+1:])
                response = numerateur/denominateur
            except:
                response = None #permet de relancer la boucle while
    if response.is_integer(): response = int(response)
    return response

@check_args
def str_puissance(x: int) -> str:
    puissance_str = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    x = str(x)
    temp = ''
    for carac in x:
        temp += puissance_str[int(carac)]
    return temp

def prog_exit() -> None:
    """Change la valeur d'exécution sur Flase"""
    global execute
    execute = False

def def_affine() -> None:
    """génère une fonction affine"""
    msg = '\nf(x) = [i green blink]a[/i green blink]x+[i green]b[/i green]\n'
    a = get_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x+[i green blink]b[/i green blink]\n'
    b = get_number(msg, 'b')

    f = Fonction('affine', [a, b])

def def_second_degre() -> None:
    """génère une fonction du second degré"""
    a = 0
    msg = '\nf(x) = [i green blink]a[/i green blink]x²+[i green]b[/i green]x+[i green]c[/i green]\n'
    while a==0:
        a = get_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[i green blink]b[/i green blink]x+[i green]c[/i green]\n'
    b = get_number(msg, 'b')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[green]{round(b, 3)}[/green]x+[i green]c[/i green]\n'
    c = get_number(msg, 'c')

    f = Fonction('second_degre', [a, b, c])

@check_args
def anal_affine(name: str, facteurs: list) -> tuple[str, str, list[str], list[str]]:
    """Analyse une fonction affine

    Args:
        name (str): nom de la fonction
        facteurs (list[float | int]): liste des facteurs [a, b]

    Returns:
        tuple[str, str, list[str], list[str]]: tuple contenant la fonction et sa dérivée sous forme de texte et son signe et sa variation sous forme de liste
    """
    a, b = facteurs

    fonction = f'{name}(x) = '
    if a==0:
        if b==0: fonction += '0'
        else: fonction += f'{b}'
    else:
        if a==1: fonction += 'x'
        elif a==-1: fonction += '-x'
        else: fonction += f'{a}x'

        if b>0: fonction += f'+{b}'
        elif b<0: fonction += f'{b}'
        #sous entendu if b==0: pass

    derivee = f'{name}\'(x) = {round(a, 3)}'

    if a>0: #f(x) croissant
        x0 = round(-b/a, 3) #x tel que ax+b = 0
        if x0.is_integer(): x0 = int(x0)
        signe = ['-∞', '-', f'{x0}', '+', '+∞']
        varia = ['-∞', '+', '+∞'] #+ pour croissant
    elif a<0: #f(x) décroissant
        x0 = round(-b/a, 3) #x tel que ax+b = 0
        if x0.is_integer(): x0 = int(x0)
        signe = ['-∞', '+', f'{x0}', '-', '+∞']
        varia = ['-∞', '-', '+∞'] #- pour décroissant
    else: #fonction constante qui ne passe pas par 0
        if b>0: signe = ['-∞', '+', '+∞']
        elif b<0: signe = ['-∞', '-', '+∞']
        else: signe = ['-∞', '0', '+∞']
        varia = ['-∞', '0', '+∞'] #0 pour constant

    return fonction, derivee, signe, varia

@check_args
def anal_second_degre(name: str, facteurs: list) -> tuple[str, str, list[str], list[str]]:
    """Analyse une fonction du second degré

    Args:
        name (str): nom de la fonction
        facteurs (list[float  |  int]): liste des facteurs [a, b, c]

    Returns:
        tuple[str, str, list[str], list[str]]: tuple contenant la fonction et sa dérivée sous forme de texte et son signe et sa variation sous forme de liste
    """
    a, b, c = facteurs

    fonction = f'{name}(x) = '
    if a==1: fonction += 'x²'
    elif a==-1: fonction += '-x²'
    else: fonction += f'{a}x²'

    if b==1: fonction += '+x'
    elif b==-1: fonction += '-x'
    elif b>0: fonction += f'+{b}x'
    elif b<0: fonction += f'{b}x'
    #sous entendu if b==0: pass

    if c>0: fonction += f'+{c}'
    elif c<0: fonction += f'{c}'
    #sous entendu if c==0: pass

    temp = round(a*2, 3)
    if type(temp)==float and temp.is_integer(): temp = int(temp) #besoin de vérif que temp est un float parce qu'il peut être un int si a est un int
    derivee = f'{name}\'(x) = {temp}x'
    if b>0: derivee += f'+{round(b, 3)}'
    elif b<0: derivee += f'{round(b, 3)}'

    f = lambda x: a*x**2+b*x+c
    Sx = -b/(2*a)
    Sy = f(Sx)
    if Sx.is_integer(): Sx = int(Sx)
    if Sy.is_integer(): Sy = int(Sy)
    S = {'x': f'{round(Sx, 3)}', 'y': f'{round(Sy, 3)}'} #S pour Sommet de la courbe

    delta = b**2-4*a*c
    if delta>0: #2 racines
        x1 = round((-b-sqrt(delta))/(2*a), 3)
        x2 = round((-b+sqrt(delta))/(2*a), 3)
        if x1.is_integer(): x1 = int(x1)
        if x2.is_integer(): x2 = int(x2)
        if x1>x2:
            x1, x2 = x2, x1
        if a>0: #la courbe a un minimum en dessous de l'axe des abscisses
            signe = ['-∞', '+', f'{x1}', '-', f'{x2}', '+', '+∞']
        else: #la courbe a un maximum au dessus de l'axe des abscisses
            signe = ['-∞', '-', f'{x1}', '+', f'{x2}', '-', '+∞']
    elif delta==0: #1 racine
        x0 = round(-b/(2*a), 3)
        if x0.is_integer(): x0 = int(x0)
        if a>0: #la courbe a un minimum sur l'axe des abscisses
            signe = ['-∞', '+', f'{x0}', '+', '+∞']
        else: #la courbe a un maximum sur l'axe des abscisses
            signe = ['-∞', '-', f'{x0}', '-' '+∞']
    else: #aucune racine
        if a>0: #la courbe a un minimum au dessus de l'axe des abscisses
            signe = ['-∞', '+', '+∞']
        else: #la courbe a un maximum en dessous de l'axe des abscisses
            signe = ['-∞', '-', '+∞']

    if a>0:
        varia = ['-∞', '-', S, '+', '+∞'] #- pour décroissant
    else:
        varia = ['-∞', '+', S, '-', '+∞'] #+ pour croissant

    return fonction, derivee, signe, varia


class Fonction:
    @check_args
    def __init__(self, forme: str, facteurs: list, name: str = 'f') -> None:
        """Créer une fonction

        Args:
            forme (str): nom de la forme de la fonction
            facteurs (list[float  |  int]): liste des facteurs
            name (str, optional): nom de la fonction. Defaults to 'f'.
        """
        self.name = name
        for i in range(len(facteurs)):
            if facteurs[i] != 0: break
            facteurs.pop(i)
        self.facteurs = facteurs
        match forme:
            case 'affine':
                self.fonction, self.derivee, self.signe, self.varia = anal_affine(name, facteurs)
            case 'second_degre':
                self.fonction, self.derivee, self.signe, self.varia = anal_second_degre(name, facteurs)
        Fonction.fonction = self #permet d'utiliser la fonction sans connaître sons nom

    def __str__(self) -> str:
        result = f'{self.name}(x) = '
        for i in range(len(self.facteurs)):
            facteur = self.facteurs[i]
            puissance = len(self.facteurs)-1-i
            if facteur == 1:
                result += '[#34ADFE]+[/#34ADFE]'
            elif facteur == -1:
                result += '[purple]-[/purple]'
            elif facteur > 0:
                if result[len(result)-1] == ' ':
                    result += '[#34ADFE]' + str(facteur) + '[/#34ADFE]'
                else:
                    result += '+' + '[#34ADFE]' + str(facteur) + '[/#34ADFE]'
            elif facteur < 0:
                result += '[purple]' + str(facteur) + '[/purple]'
            
            if facteur!=0 and puissance>0:
                result += '[green]x[/green]'
                if puissance > 1:
                    result += '[green]' + str_puissance(puissance) + '[/green]'

        if len(result)==7:
            result += '0'

        return result        

    def display(self):
        """Affiche l'étude de la fonction (son tableau de signe, de variation, la fonction et sa dérivée)"""
        t_signe = [
            ['', 'x='],
            ['signe', f'{self.name}(x)']
        ]
        t_varia = [
            ['', 'x='],
            ['signe', f'{self.name}\'(x)'],
            ['varia', f'{self.name}(x)']
        ]
        for i in range(len(self.signe)): #construit le tableau de signe
            if i%2==0: #si i est paire
                if self.signe[i] in ('-∞', '+∞'): #si l'on est à la fin ou au début du tableau
                    t_signe[0].append(self.signe[i])
                    t_signe[1].append('')
                else:
                    t_signe[0].append(self.signe[i]) #correspond à une racine
                    t_signe[1].append('0')
            elif i%2==1: #si i est impaire
                t_signe[0].append('')
                t_signe[1].append(self.signe[i])
        for i in range(len(self.varia)): #construit le tableau de variation
            if i%2==0: #si i est paire
                if self.varia[i] in ('-∞', '+∞'): #si l'on est à la fin ou au début du tableau
                    t_varia[0].append(self.varia[i])
                    t_varia[1].append('')
                    t_varia[2].append('')
                else:
                    t_varia[0].append(self.varia[i]["x"]) #correspond à un changement de variation
                    t_varia[1].append('0')
                    t_varia[2].append(self.varia[i]["y"])
            else: #si i est impaire
                match self.varia[i]: #attribut les bons symboles en fonction de la variation
                    case '+':
                        varia = ('+', '↗')
                    case '-':
                        varia = ('-', '↘')
                    case '0':
                        varia = ('0', '→')
                t_varia[0].append('')
                t_varia[1].append(varia[0])
                t_varia[2].append(varia[1])

        for t in (t_signe, t_varia): #boucle sur chaque tableau
            tableau = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
            for i in range(len(t[0])):
                tableau.add_column(t[0][i], justify='center') #ajout des en-têtes de colonnes une par une (première ligne de t)
            for i in range(1, len(t)):
                tableau.add_row(*t[i]) #ajout des lignes une par une
            console.print(tableau) # affichage du tableau
        console.print('\n')
        console.print(self.fonction, self.derivee, sep='\n')
        console.print('\n\n[#818488]Certaines valeurs peuvent être arrondies.[/#818488]')

class Selecteur:
    @check_args
    def __init__(self, prompt_msg: str, options: list, prompt_title: str = ''):
        """Créer un menu de sélection

        Args:
            prompt_msg (str): instruction donnée à la fin du menu (après le options)
            options (list[dict]): liste des options à afficher
            prompt_title (str, optional): message à afficher au début du menu (avant les options). Defaults to None.
        """
        self.prompt_title = prompt_title
        self.options = options
        self.prompt_msg = prompt_msg

    def prompt(self):
        select = None
        options_list = '[1' #liste des valeurs fonctionnelles pour l'input
        for i in range(1, len(self.options)):
            options_list += f'/{i+1}'
        options_list += ']'

        while type(select)!=int:
            cls()
            if self.prompt_title != '':
                console.print(f'\n\n{self.prompt_title}\n')
            else:
                console.print('\n\n')
            for i in range(len(self.options)):
                console.print(f'[#61d6d6][{i+1}][/#61d6d6] : {self.options[i]["content"]}')
            select = console.input(f'\n\n{self.prompt_msg} [#61d6d6]{options_list}[/#61d6d6] : ')
            try:
                select = int(select) - 1 #vérifie que l'input est un nombre (entier)
                if select not in range(len(self.options)): #vérifie que l'input ne fait pas parti des options
                    select = None #permet de rester dans la boucle while
            except:
                pass
        self.options[select]["fonction associee"]() #exécute la fonction associée à l'option et récupère son return (même si elle ne return pas)




options_selecteur_1er = [
    {
        'forme': 'affine',
        'content': 'f(x) = [i green]a[/i green]x+[i green]b[/i green]',
        'fonction associee': def_affine
    },
    {
        'forme': 'second_degre',
        'content': 'f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]    [#818488](a ∈ ℝ\\0)[/#818488]',
        'fonction associee': def_second_degre
    }
]
selecteur_1er = Selecteur('Fonction du type', options_selecteur_1er, 'Sélectionnez la forme de la fonction')

options_main_menu = [
    {
        'content': 'Ajouter une fonction à étudier',
        'fonction associee': selecteur_1er.prompt
    },
    {
        'content': 'Quitter',
        'fonction associee': prog_exit
    }
]
main_menu = Selecteur('Choisissez une action', options_main_menu)

execute = True #valeur d'exécution




cls()
console.print(f"""\nBienvenu sur [link={prog_info['release_link']}]f-study {prog_info['version']}[/link]

Pour signaler un bug ou suggérer une nouvelle fonctionnalité créez une issue [link=https://github.com/Nyde2283/f-study/issues/new/choose]ici[/link].   [#63666A](Ctrl+Click)[/#63666A]""")
input('\nAppuyez sur Entrée pour continuer...')

while execute:
    try:
        main_menu.prompt()
        cls()
        if execute: #empêche d'exécuter si l'option quitté est choisie
            console.print('\n')
            Fonction.fonction.display()
            console.input('\n\n[black on white]Appuyer sur Entrée pour continuer...[/black on white]')
    except KeyboardInterrupt:
        exit()
    except:
        SomethinWentWrong.raise_and_continu()
        pass




#    f-study
#    Copyright (C) CHEVEREAU Edwyn
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    GNU GPLv3: https://www.gnu.org/licenses/gpl-3.0.html