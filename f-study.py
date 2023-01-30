from platform import system as platform
from sys import version_info

from decorators import *
from error import *

prog_info = {
	'version': 'v0.2.2',
	'release_link': 'https://github.com/Nyde2283/f-study/releases/tag/v0.2.2',
	'py_version': f'{version_info.major}.{version_info.minor}.{version_info.micro}',
	'plateforme': platform()
}
def_debug_info(prog_info)

if version_info<(3, 10): BadPythonVersion.raise_and_exit()

try:
	from rich.console import Console
except Exception as e:
	RichNotFound.raise_and_exit(e)
from fonction import Fonction, def_affine, def_second_degre
from display import Selecteur, cls

console = Console(highlight=False) #désactive le formatage auto pour éviter des incohérences dans la coloration




def prog_exit() -> None:
	"""Change la valeur d'exécution sur Flase"""
	global execute
	execute = False

options_selecteur_1er = [
	{
		'forme': 'affine',
		'content': 'f(x) = [i green]a[/i green]x+[i green]b[/i green]',
		'fonction associee': def_affine
	},
	{
		'forme': 'second_degre',
		'content': 'f(x) = [i green]a[/i green]x²+[i green]b[/i green]x+[i green]c[/i green]	[#818488](a ∈ ℝ\\0)[/#818488]',
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




#	f-study
#	Copyright (C) CHEVEREAU Edwyn
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	GNU GPLv3: https://www.gnu.org/licenses/gpl-3.0.html