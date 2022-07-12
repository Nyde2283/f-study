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