from dictionaries import conversions, units, numeral_conversions, numeral_systems

def unit_convert(value, from_unit, to_unit):
  if from_unit in units and to_unit in units: # check if the units exist
    if to_unit in conversions[from_unit]: # check if the from_unit can be converted in to_unit
        conversion_func = conversions[from_unit][to_unit]
        result = conversion_func(float(value))
        return f"{value} {from_unit} = {round(result, 4)} {to_unit}"
    else:
        return f"Couldn't convert {units[from_unit]} in {units[to_unit]}"
  else:
    return f'"{from_unit if not from_unit in units else to_unit}" not found...'


def get_units_list():
  return '\n'.join([f'{unit}  -  {units[unit]}' for unit in conversions])
  

def numeral_convert(value, from_system, to_system):
  if from_system in numeral_systems and to_system in numeral_systems: # check if the units exist
    if to_system in numeral_conversions[from_system]: # check if the from_unit can be converted in to_unit
      conversion_func = numeral_conversions[from_system][to_system]
      result = conversion_func(value)
      return f"{value} ({numeral_systems[from_system]}) => {result} ({numeral_systems[to_system]})"
    else:
        return f"Couldn't convert {numeral_systems[from_system]} in {numeral_systems[to_system]}"
  else:
    return f'"{from_system if not from_system in numeral_systems else to_system}" not found...'
