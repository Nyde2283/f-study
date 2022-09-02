from sys import version_info
from os import system
from platform import system as platform
from math import sqrt
from error import def_debug_info, display_error, exit_on_error

prog_info = {
    'version': 'v0.1.1-dev',
    'release_link': 'https://github.com/Nyde2283/f-study/releases/tag/v0.1.0',
    'py_version': f'{version_info.major}.{version_info.minor}.{version_info.micro}',
    'platforme': platform()
}
def_debug_info(prog_info)

if version_info<(3, 10): exit_on_error('Bad Python version')

try:
    from rich.console import Console
except:
    exit_on_error('Rich not found')
from rich.table import Table
from rich import box


console = Console(highlight=False)




def get_number(msg, var):
    response = None
    while response==None:
        system('cls')
        console.print(msg)
        response = console.input(f'{var} = ')
        try:
            response = float(response)
        except:
            try:
                i = response.index('/')
                numerateur = float(response[:i])
                denominateur = float(response[i+1:])
                response = numerateur/denominateur
            except:
                response = None
    if response.is_integer(): response = int(response)
    return response

def def_affine():
    msg = '\nf(x) = [i green blink]a[/i green blink]x+[i green]b[/i green]\n'
    a = get_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x+[i green blink]b[/i green blink]\n'
    b = get_number(msg, 'b')

    f = Fonction('affine', [a, b])

def def_second_degre():
    a = 0
    msg = '\nf(x) = [i green blink]a[/i green blink]x²+[i green]b[/i green]x+[i green]c[/i green]\n'
    while a==0:
        a = get_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[i green blink]b[/i green blink]x+[i green]c[/i green]\n'
    b = get_number(msg, 'b')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[green]{round(b, 3)}[/green]x+[i green]c[/i green]\n'
    c = get_number(msg, 'c')

    f = Fonction('second_degre', [a, b, c])

def anal_affine(name, facteurs):
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

    if a>0:
        x0 = round(-b/a, 3)
        if x0.is_integer(): x0 = int(x0)
        signe = ['-∞', '-', f'{x0}', '+', '+∞']
        varia = ['-∞', '+', '+∞']
    elif a<0:
        x0 = round(-b/a, 3)
        if x0.is_integer(): x0 = int(x0)
        signe = ['-∞', '+', f'{x0}', '-', '+∞']
        varia = ['-∞', '-', '+∞']
    else:
        if b>0: signe = ['-∞', '+', '+∞']
        elif b<0: signe = ['-∞', '-', '+∞']
        else: signe = ['-∞', '0', '+∞']
        varia = ['-∞', '0', '+∞']

    return fonction, derivee, signe, varia

def anal_second_degre(name, facteurs):
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
    if type(temp)==float and temp.is_integer(): temp = int(temp)
    derivee = f'{name}\'(x) = {temp}x'
    if b>0: derivee += f'+{round(b, 3)}'
    elif b<0: derivee += f'{round(b, 3)}'

    f = lambda x: a*x**2+b*x+c
    Sx = -b/(2*a)
    Sy = f(Sx)
    if Sx.is_integer(): Sx = int(Sx)
    if Sy.is_integer(): Sy = int(Sy)
    S = {'x': f'{round(Sx, 3)}', 'y': f'{round(Sy, 3)}'}

    delta = b**2-4*a*c
    if delta>0:
        x1 = round((-b-sqrt(delta))/(2*a), 3)
        x2 = round((-b+sqrt(delta))/(2*a), 3)
        if x1.is_integer(): x1 = int(x1)
        if x2.is_integer(): x2 = int(x2)
        if x1>x2:
            x1, x2 = x2, x1
        if a>0:
            signe = ['-∞', '+', f'{x1}', '-', f'{x2}', '+', '+∞']
        else:
            signe = ['-∞', '-', f'{x1}', '+', f'{x2}', '-', '+∞']
    elif delta==0:
        x0 = round(-b/(2*a), 3)
        if x0.is_integer(): x0 = int(x0)
        if a>0:
            signe = ['-∞', '+', f'{x0}', '+', '+∞']
        else:
            signe = ['-∞', '-', f'{x0}', '-' '+∞']
    else:
        if a>0:
            signe = ['-∞', '+', '+∞']
        else:
            signe = ['-∞', '-', '+∞']

    if a>0:
        varia = ['-∞', '-', S, '+', '+∞']
    else:
        varia = ['-∞', '+', S, '-', '+∞']
    
    return fonction, derivee, signe, varia


class Fonction:
    def __init__(self, forme: str, facteurs: list, name='f'):
        self.name = name
        match forme:
            case 'affine':
                self.fonction, self.derivee, self.signe, self.varia = anal_affine(name, facteurs)
            case 'second_degre':
                self.fonction, self.derivee, self.signe, self.varia = anal_second_degre(name, facteurs)
        Fonction.fonction = self

    def display(self):
        t_signe = [
            ['', 'x='],
            ['signe', f'{self.name}(x)']
        ]
        t_varia = [
            ['', 'x='],
            ['signe', f'{self.name}\'(x)'],
            ['varia', f'{self.name}(x)']
        ]
        for i in range(len(self.signe)):
            if i%2==0:
                if self.signe[i] in ('-∞', '+∞'):
                    t_signe[0].append(self.signe[i])
                    t_signe[1].append('')
                else:
                    t_signe[0].append(self.signe[i])
                    t_signe[1].append('0')
            elif i%2==1:
                t_signe[0].append('')
                t_signe[1].append(self.signe[i])
        for i in range(len(self.varia)):
            if i%2==0:
                if self.varia[i] in ('-∞', '+∞'):
                    t_varia[0].append(self.varia[i])
                    t_varia[1].append('')
                    t_varia[2].append('')
                else:
                    t_varia[0].append(self.varia[i]["x"])
                    t_varia[1].append('0')
                    t_varia[2].append(self.varia[i]["y"])
            else:
                match self.varia[i]:
                    case '+':
                        varia = ('+', '↗')
                    case '-':
                        varia = ('-', '↘')
                    case '0':
                        varia = ('0', '→')
                t_varia[0].append('')
                t_varia[1].append(varia[0])
                t_varia[2].append(varia[1])

        for t in (t_signe, t_varia):
            tableau = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
            for i in range(len(t[0])):
                tableau.add_column(t[0][i], justify='center') #ajout des en-têtes de colonnes un par un (première ligne de t)
            for i in range(1, len(t)):
                tableau.add_row(*t[i]) #ajout des lignes une par une
            console.print(tableau) # affichage de la table
        console.print('\n')
        console.print(self.fonction, self.derivee, sep='\n')
        console.print('\n\n[#818488]Certaines valeurs peuvent être arrondies.[/#818488]')

class Selecteur:
    def __init__(self, prompt_msg, options, prompt_title=None):
        self.prompt_title = prompt_title
        self.options = options
        self.prompt_msg = prompt_msg

    def prompt(self):
        select = None
        options_list = '[1'
        for i in range(1, len(self.options)):
            options_list += f'/{i+1}'
        options_list += ']'

        while type(select)!=int:
            system('cls')
            if self.prompt_title != None:
                console.print(f'\n\n{self.prompt_title}\n')
            else:
                console.print('\n\n')
            for i in range(len(self.options)):
                console.print(f'[#61d6d6][{i+1}][/#61d6d6] : {self.options[i]["content"]}')
            select = console.input(f'\n\n{self.prompt_msg} [#61d6d6]{options_list}[/#61d6d6] : ')
            try:
                select = int(select)
                if select not in range(1, len(self.options)+1):
                    select = None
            except:
                pass
        return_value = self.options[i]["fonction associee"]()

        return return_value





options_selecteur_1er = [
    {
        'forme': 'affine',
        'content': 'f(x) = [i green]a[/i green]x+[i green]b[/i green]',
        'fonction associee': def_affine
    },
    {
        'forme': 'second_degre',
        'content': 'f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]',
        'fonction associee': def_second_degre
    }
]
selecteur_1er = Selecteur('Fonction du type', options_selecteur_1er, 'Sélectionnez la forme de la fonction')

options_main_menu = [
    {
        'content': 'Ajouter une fonction à étudier',
        'fonction associee': selecteur_1er.prompt
    }
]
main_menu = Selecteur('Choisissez une action', options_main_menu)

while True:
    try:
        main_menu.prompt()
        system('cls')
        console.print('\n')
        Fonction.fonction.display()
        console.print('\n\n[#818488]Pour faire une demande de nouvelle fonctionnalité \nou pour signaler un bug : [/#818488]https://github.com/Nyde2283/f-study/issues   [#63666A](Ctrl+Click)[/#63666A]', highlight=False)
        console.input('\n\n[black on white]Appuyer sur Entrée pour continuer...[/black on white]')
    except:
        display_error('Something went wrong')
        pass
