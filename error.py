from decorators import *




def def_debug_info(prog_info):
    """Définie les information de débogage

    Args:
        prog_info (dict): dictionnaire avec les clefs 'version', 'py_version' et 'platforme'
    """
    global debug_info
    debug_info = prog_info

class Error:
    @check_args
    def __init__(self, code: str, msg: str, todo: str = '') -> None:
        """Créer une erreur

        Args:
            code (str): nom de l'erreur
            msg (str): message à afficher
            todo (str, optional): marche à suivre pour résoudre l'erreur. Defaults to ''.
        """
        self.code = code
        self.msg = msg
        if todo == '': self.todo = None
        else: self.todo = todo
    
    @check_args
    def raise_and_exit(self, e: Exception = AssertionError):
        """Affiche l'erreur et ferme le programme

        Args:
            e (Exception, optional): Exception levée (si il y en a une). Defaults to AssertionError.
        """
        print(f"\n\nCode d'erreur : \n\t{self.code}")
        print(f"\nmessage : \n\t{self.msg}")
        if self.todo != None:
            print(f"\nSolution possible : \n\t{self.todo}")
        print(f"\ndebug info : \n\t- Version de f-study : {debug_info['verion']} \n\t- Version de Python : {debug_info['py_version']} \n\t- OS : {debug_info['plateforme']}")
        print(f"\nerreur levée : \n\t{repr(e)}\n")
        input('Appuyer sur Entrée pour quitter...')
        exit()
    
    @check_args
    def raise_and_continu(self, e: Exception = AssertionError):
        """Affiche l'erreur puis reprend le programme

        Args:
            e (Exception, optional): Exception levée (si il y en a une). Defaults to AssertionError.
        """
        print(f"\n\nCode d'erreur : \n\t{self.code}")
        print(f"\nmessage : \n\t{self.msg}")
        if self.todo != None:
            print(f"\nSolution possible : \n\t{self.todo}")
        print(f"\ndebug info : \n\t- Version de f-study : {debug_info['verion']} \n\t- Version de Python : {debug_info['py_version']} \n\t- OS : {debug_info['plateforme']}")
        print(f"\nerreur levée : \n\t{repr(e)}\n")
        input('Appuyer sur Entrée pour continuer...')

TestError = Error(
    'Test',
    'Rien à craindre, cette erreur est un test.',
)

BadPythonVersion = Error(
    'Bad Python version',
    'f-study nécessite Python 3.10 ou une version spérieure.',
    'Vous pouvez installer une nouvelle version de Python \033]8;;https://www.python.org/downloads/\033\\ici\033]8;;\033\\.'
)

RichNotFound = Error(
    'Rich not found',
    """La bibliothèque Rich n'est pas installée sur votre ordinateur.
    Elle est indispensable pour afficher les tableaux.
    (Si vous utilisez f-study via un exécutable veuillez signaler cette erreur, merci)""",
    """Vous pouvez installer Rich via cette commande : python -m pip install rich
    Pour plus d'informations consultez la page \033]8;;https://pypi.org/project/rich/\033\\PyPi\033]8;;\033\\ ou la page \033]8;;https://github.com/Textualize/rich\033\\GitHube\033]8;;\033\\ de Rich."""
)

SomethinWentWrong = Error(
    'Something went wrong',
    'f-study a cessé de fonctionner de manière inatendue et va tenter de redémarrer.'
)




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