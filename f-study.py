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




class Fonction:
    def __init__(self, name='f'):
        self.name = name

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
        for i in range(len(self.f_signe)):
            if i%2==0:
                if self.f_signe[i] in ('-∞', '+∞'):
                    t_signe[0].append(self.f_signe[i])
                    t_signe[1].append('')
                else:
                    t_signe[0].append(self.f_signe[i])
                    t_signe[1].append('0')
            elif i%2==1:
                t_signe[0].append('')
                t_signe[1].append(self.f_signe[i])
        for i in range(len(self.f_varia)):
            if i%2==0:
                if self.f_varia[i] in ('-∞', '+∞'):
                    t_varia[0].append(self.f_varia[i])
                    t_varia[1].append('')
                    t_varia[2].append('')
                else:
                    t_varia[0].append(self.f_varia[i]["x"])
                    t_varia[1].append('0')
                    t_varia[2].append(self.f_varia[i]["y"])
            else:
                match self.f_varia[i]:
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
        console.print('\n')
        console.print('[#818488]Certaines valeurs peuvent être arrondies.[/#818488]')




