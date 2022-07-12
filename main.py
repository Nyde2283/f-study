from rich.console import Console
from rich.table import Table
from rich import box




def affichage(t):
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

     console = Console()
     console.print(table) # affichage de la table


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

    function = f'f(x) = '
    if a==0:
        pass
    elif a==1:
        function += 'x'
    else:
        function += f'{a}x'
    if b==0:
        pass
    elif b>0:
        function += f'+{b}'
    else:
        function += f'{b}'

    if a>0:
        zero = -b/a
        signe = ('-', '+')
        variation = '⤴️'
    elif a<0:
        zero = -b/a
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
    affichage(table)