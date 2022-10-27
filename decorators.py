from functools import wraps


def check_args(fct):
    """Test les paramètres de la fonction décorée

    Args:
        fct (function): fonction décorée
    """
    args_names = fct.__code__.co_varnames
    @wraps(fct)
    def check(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        appel = f'{fct.__name__}({", ".join(args_repr + kwargs_repr)})'
        dict_args_value = {}
        for i in range(len(args)):
            dict_args_value[args_names[i]] = args[i]
        for key, value in kwargs.items():
            dict_args_value[key] = value
        
        for arg, value in dict_args_value.items():
            annot_key_type = [item for item in list(fct.__annotations__.items()) if arg in item] #liste avec un seul élément
            if len(annot_key_type) != 0: #si l'argument est compris dans les annotations
                annot_key_type = annot_key_type[0]
                annot_type = annot_key_type[1]
                if type(annot_type) == type:
                    if type(value) != annot_type:
                        raise TypeError(f'{repr(annot_key_type)} attendu | appel: {appel}')
                else:
                    if value != annot_type:
                        raise ValueError(f'{repr(annot_key_type)} attendu | appel: {appel}')

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