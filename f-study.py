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
from rich.table import Table
from rich import box
from math import sqrt
from os import system


console = Console(highlight=False)




def selection(options: list[dict]):
    select=None
    while type(select)!=int:
        system('cls')
        console.print('\n\nSélectionnez la forme de la fonction :\n')
        for i in range(len(options)):
            console.print(f'[#61d6d6]{i+1}[/#61d6d6]: {options[i]["content"]}')
        select = console.input('\n\nFonction du type : ')
        try:
            select = int(select)
            if select not in range(1, len(options)+1):
                select = None
        except:
            pass
    return select-1

def def_number(msg, var):
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

def selection_affine():
    msg = '\nf(x) = [i green blink]a[/i green blink]x+[i green]b[/i green]\n'
    a = def_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x+[i green blink]b[/i green blink]\n'
    b = def_number(msg, 'b')

    return [a, b]

def selection_second_degre():
    a = 0
    msg = '\nf(x) = [i green blink]a[/i green blink]x²+[i green]b[/i green]x+[i green]c[/i green]\n'
    while a==0:
        a = def_number(msg, 'a')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[i green blink]b[/i green blink]x+[i green]c[/i green]\n'
    b = def_number(msg, 'b')

    msg = f'\nf(x) = [green]{round(a, 3)}[/green]x²+[green]{round(b, 3)}[/green]x+[i green]c[/i green]\n'
    c = def_number(msg, 'c')

    return [a, b, c]

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
        signe = ['-∞', '+', f'{round(-b/a, 3)}', '-', '+∞']
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

    derivee = f'{name}\'(x) = {round(a*2, 3)}x'
    if b>0: derivee += f'+{round(b, 3)}'
    elif b<0: derivee += f'{round(b, 3)}'

    f = lambda x: a*x**2+b*x+c
    Sx = -b/(2*a)
    S = {'x': f'{round(Sx, 3)}', 'y': f'{round(f(Sx), 3)}'}

    delta = b**2-4*a*c
    if delta>0:
        x1 = round((-b-sqrt(delta))/(2*a), 3)
        x2 = round((-b+sqrt(delta))/(2*a), 3)
        if x1>x2:
            x1, x2 = x2, x1
        if a>0:
            signe = ['-∞', '+', f'{x1}', '-', f'{x2}', '+', '+∞']
        else:
            signe = ['-∞', '-', f'{x1}', '+', f'{x2}', '-', '+∞']
    elif delta==0:
        x0 = round(-b/(2*a), 3)
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




options = [
    {
        'forme': 'affine',
        'content': 'f(x) = [i green]a[/i green]x+[i green]b[/i green]',
        'fonction_selection': selection_affine
    },
    {
        'forme': 'second_degre',
        'content': 'f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]',
        'fonction_selection': selection_second_degre
    }
]

while True:
    select_i = selection(options)
    select = options[select_i]
    facteurs = select["fonction_selection"]()
    f = Fonction(select["forme"], facteurs)

    system('cls')
    console.print('\n')
    f.display()
    console.print('\n\n[#818488]Pour faire une demande de nouvelle fonctionnalité \nou pour signaler un bug : [/#818488]https://github.com/Nyde2283/f-study/issues   [#63666A](Ctrl+Click)[/#63666A]', highlight=False)
    console.input('\n\n[black on white]Appuyer sur Entrée pour continuer...[/black on white]')





