error_list = {
    'test': 'Rien à craindre, cette erreur est un test.',
    'bad Python version': 'f-study nécessite Python 3.10 ou une version spérieure',
    'Rich not found': """La bibliothèque Rich n'est pas installée sur votre ordinateur.
    Elle est indispensable pour afficher les tableaux.
    Pour plus d'informations consultez la page \033]8;;https://pypi.org/project/rich/\033\\PyPi\033]8;;\033\\ ou la page \033]8;;https://github.com/Textualize/rich\033\\GitHube\033]8;;\033\\ de Rich.
    (Si vous utilisez f-study via un .EXE (qui a pu être extrait d'un .ZIP ou .RAR) veuillez signaler cette erreur, merci)"""
}

def def_debug_info(prog_info):
    global debug_info
    debug_info = prog_info

def exit_on_error(error_code):
    print(f"""\nCode d'erreur :
    {error_code}

message :
    {error_list.get(error_code)}

debug info :
    - Version de f-study : {debug_info['version']}
    - Version de Python : {debug_info['py_version']}
    - OS : {debug_info['platforme']}\n""")
    input('Appuyer sur Entrée pour quitter...')
    exit()

