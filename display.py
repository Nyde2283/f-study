from decorators import check_args
from os import system
from platform import system as platform
from rich.console import Console

console = Console(highlight=False) #désactive le formatage auto pour éviter des incohérences dans la coloration

def cls() -> None:
	"""Supprime le contenu de la console"""
	if platform()=='Windows': system('cls')
	else: system('clear')

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