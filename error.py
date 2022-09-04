error_list = {
    'Test': {
        'msg': 'Rien à craindre, cette erreur est un test.',
        'to do': None
    },
    'Bad Python version': {
        'msg': 'f-study nécessite Python 3.10 ou une version spérieure.',
        'to do': 'Vous pouvez installer une nouvelle version de Python \033]8;;https://www.python.org/downloads/\033\\ici\033]8;;\033\\.'
    },
    'Rich not found': {
        'msg': """La bibliothèque Rich n'est pas installée sur votre ordinateur.
    Elle est indispensable pour afficher les tableaux.
    (Si vous utilisez f-study via un .EXE (pouvant venir d'un .ZIP ou .RAR) veuillez signaler cette erreur, merci)""",
    'to do': """Vous pouvez installer Rich via cette commande : python -m pip install rich
    Pour plus d'informations consultez la page \033]8;;https://pypi.org/project/rich/\033\\PyPi\033]8;;\033\\ ou la page \033]8;;https://github.com/Textualize/rich\033\\GitHube\033]8;;\033\\ de Rich.""",
    },
    'Something went wrong': {
        'msg': 'f-study a cessé de fonctionner de manière inatendue, il va tenter de redémarrer.',
        'to do': None
    }
} #Format : error_list = dict{error_code: dict{msg: str, to do: str}, ...}

def def_debug_info(prog_info):
    """Définie les information de débogage

    Args:
        prog_info (dict): dictionnaire avec les clefs 'version', 'py_version' et 'platforme'
    """
    global debug_info
    debug_info = prog_info

def exit_on_error(error_code):
    """Affiche une erreur puis ferme le programme

    Args:
        error_code (str): code correspondant à une des clefs de error_list
    """
    print(f"""\n\nCode d'erreur :
    {error_code}

message :
    {error_list.get(error_code).get('msg')}""")

    if error_list.get(error_code).get('to do') != None:
        print(f"""\nsolution possible :
    {error_list.get(error_code).get('to do')}""")

    print(f"""\ndebug info :
    - Version de f-study : {debug_info['version']}
    - Version de Python : {debug_info['py_version']}
    - OS : {debug_info['platforme']}\n""")
    input('Appuyer sur Entrée pour quitter...')
    exit()

def display_error(error_code):
    """Affiche une erreur puis reprend le programme

    Args:
        error_code (str): code correspondant à une des clefs de error_list
    """
    print(f"""\n\nCode d'erreur :
    {error_code}

message :
    {error_list.get(error_code).get('msg')}""")

    if error_list.get(error_code).get('to do') != None:
        print(f"""\nsolution possible :
    {error_list.get(error_code).get('to do')}""")

    print(f"""\ndebug info :
    - Version de f-study : {debug_info['version']}
    - Version de Python : {debug_info['py_version']}
    - OS : {debug_info['platforme']}\n""")
    input('Appuyer sur Entrée pour continuer...')




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