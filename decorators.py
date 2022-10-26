import functools


def check_args(fct) -> None:
    """Test les paramètres de la fonction décorée

    Args:
        fct (function): fonction décorée

    Returns:
        None
    """
    @functools.wraps(fct)
    def check(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        appel = f'{fct.__name__}({", ".join(args_repr + kwargs_repr)})'

        if fct.__name__=='__init__': array = len(args)-1
        else: array = len(args)
        for i in range(array):
            if fct.__name__=='__init__': j=i+1
            else: j=i
            annot_key_value = list(fct.__annotations__.items())[i]
            annot_value = list(fct.__annotations__.values())[i]

            if type(annot_value) == type:
                if type(args[j]) != annot_value:
                    raise TypeError(f'{repr(annot_key_value)} attendu | appel: {appel}')
            else:
                if args[j] != annot_value:
                    raise ValueError(f'{repr(annot_key_value)} attendu | appel: {appel}')

        for arg, value in kwargs.items():
            annot_key_value = [item for item in list(fct.__annotations__.items()) if arg in item][0]
            annot_value = fct.__annotations__[arg]

            if type(annot_value) == type:
                if type(value) != annot_value:
                    raise TypeError(f'{repr(annot_key_value)} attendu | appel: {appel}')
            else:
                if value != annot_value:
                    raise ValueError(f'{repr(annot_key_value)} attendu | appel: {appel}')

        return fct(*args, **kwargs)
    return check




#    f-study
#    Copyright (C) CHEVEREAU Edwyn
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    GNU GPLv3: https://www.gnu.org/licenses/gpl-3.0.html