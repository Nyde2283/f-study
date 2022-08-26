from rich.table import Table
from rich.console import Console
from rich import box
from os import system


console = Console(highlight=False)




def affichage(tableaux, function, derivee):
    system('cls')
    console.print('\n')
    for t in tableaux:
        table = Table(box=box.SIMPLE, padding=(0,2,0,2), leading=1)
        for i in range(len(t[0])):
            table.add_column(t[0][i], justify='center') #ajout des en-têtes de colonnes un par un (première ligne de t)
        for i in range(1, len(t)):
            table.add_row(*t[i]) #ajout des lignes une par une
        console.print(table) # affichage de la table
    console.print('\n')
    console.print(function, derivee, sep='\n')
    console.print('\n')
    console.print('[#818488]Certaines valeurs peuvent être arrondies.[/#818488]')
    console.print('\n\n[#818488]Pour faire une demande de nouvelle fonctionnalité \nou pour signaler un bug : [/#818488]https://github.com/Nyde2283/f-study/issues   [#63666A](Ctrl+Click)[/#63666A]', highlight=False)
    console.input('\n\n[black on white]Appuyer sur Entrée pour quitter...[/black on white]')




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