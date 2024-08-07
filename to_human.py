"Module for shortening integers to more readable formats."

from typing import Optional, Union, List, Tuple
from math import log10
from _extras import round

def to_human(
    value: Union[int, str, float],
    units: Optional[Union[List[str], Tuple[str]]] = None,
    /,
    precision: int = 2
) -> str:
    """
    Turns a given number into its shortened abbreviated version in the format `"...U"` (where `U` is an accepted format).

    Parameters:
        - value: `Union[int, str, float]` - the value to abbreviate into a more readable format.
        - units: `Optional[Iterable[str]]` - the list of units to use instead of the standard units.
                                             Defaults to `None` where standard units will be used.
        - precision: `int` - the number of decimal points to round the final result to. Defaults to 2.
    """
    
    if not isinstance(value, (int, str, float)):
        raise ValueError('value argument is not an integer or a string.')
    
    if isinstance(value, float):
        if not value.is_integer():
            raise ValueError('this function cannot convert floats to an abbreviated format.')
    
    if isinstance(value, str):
        if not value.isdigit():
            raise ValueError('value argument cannot be converted from string to integer.')
        
    value = int(value) # make an integer
    
    exp = int(log10(value)) // 3 # clamp it down

    if units:
        if not all(x is str for x in units):
            raise ValueError('units list contain non-string inputs.')

    else:
        units = ['k', 'm', 'b', 't']

    cap = (len(units) - 1) * 3

    if exp > cap: exp = cap # cap to however many units there are

    base: float = value / 10**exp

    base = round(base, precision)

    U = units[exp // 3] if exp else ''

    return f'{base}{U}'