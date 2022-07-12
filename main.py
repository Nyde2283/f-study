from rich.console import Console
from rich.table import Table
from rich import box




def affichage(t):
     assert type(t)==list, f't doit être une liste (type(t) = {type(t)})'
     assert len(t)>=2, f'Le tableau est trop petit (nb_lignes = {len(t)} < 2)'
     assert len(t[0])>=4, f'Le tableau est trop petit (nb_colonnes = {len(t[0])} < 4)'
     for i in range(len(t)):
          assert len(t[i])==len(t[0]), f'Les lignes du tableau n\'ont pas la même longueur (len t[0]= {len(t[0])}, len t[{i}]= {len(t[i])}'

     table = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
     for i in range(len(t[0])):
          table.add_column(t[0][i], justify='center')
     for i in range(1, len(t)):
          table.add_row(*t[i])

     console = Console()
     console.print(table)