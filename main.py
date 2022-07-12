from rich.console import Console
from rich.table import Table
from rich import box




def affichage(t):
     table = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
     for i in range(len(t[0])):
          table.add_column(t[0][i], justify='center')
     for i in range(1, len(t)):
          table.add_row(*t[i])

     console = Console()
     console.print(table)