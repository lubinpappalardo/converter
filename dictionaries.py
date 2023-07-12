conversions = {
    
  #-------- Lenght conversion --------

  'm': {
      'cm': lambda x: x * 100,
      'mm': lambda x: x * 1000,
      'km': lambda x: x / 1000,
      'mi': lambda x: x / 1609.344,
      'ft': lambda x: x * 3.2808399,
      'in': lambda x: x * 39.3700787,
  },
  'cm': {
      'm': lambda x: x / 100,
      'mm': lambda x: x * 10,
      'km': lambda x: x / 100000,
      'mi': lambda x: x / 160934.4,
      'ft': lambda x: x / 30.48,
      'in': lambda x: x / 2.54,
  },
  'mm': {
      'm': lambda x: x / 1000,
      'cm': lambda x: x / 10,
      'km': lambda x: x / 1000000,
      'mi': lambda x: x / 1609344,
      'ft': lambda x: x / 304.8,
      'in': lambda x: x / 25.4,
  },
  'km': {
      'm': lambda x: x * 1000,
      'cm': lambda x: x * 100000,
      'mm': lambda x: x * 1000000,
      'mi': lambda x: x / 1.609344,
      'ft': lambda x: x * 3280.8399,
      'in': lambda x: x * 39370.0787,
  },
  'mi': {
      'm': lambda x: x * 1609.344,
      'cm': lambda x: x * 160934.4,
      'mm': lambda x: x * 1.6093E+6,
      'km': lambda x: x * 1.609344,
      'ft': lambda x: x * 5280,
      'in': lambda x: x * 63360,
  },
  'ft': {
      'm': lambda x: x / 3.2808399,
      'cm': lambda x: x * 30.48,
      'mm': lambda x: x * 304.8,
      'km': lambda x: x / 3280.8399,
      'mi': lambda x: x / 5280,
      'in': lambda x: x * 12,
  },
  'in': {
      'm': lambda x: x / 39.3700787,
      'cm': lambda x: x * 2.54,
      'mm': lambda x: x * 25.4,
      'km': lambda x: x / 39370.0787,
      'mi': lambda x: x / 63360,
      'ft': lambda x: x / 12,
  },

  #-------- Temperature conversion --------

  'c': {
    'f': lambda x: 1.8 * x + 32,
    'k': lambda x: x + 273.15,
  },

  'f': {
    'c': lambda x: (x - 32) / 1.8,
    'k': lambda x: 1.8 * (x - 32) + 273.15,
  },

  'k': {
    'c': lambda x: x - 273.15,
    'f': lambda x: 1.8 * (x - 273.15) + 32,
  },

  #-------- Speed conversion --------

  'mph': {
    'kph': lambda x: x * 1.609344,
    'mps': lambda x: x / 2.23693629,
    'kt': lambda x: x / 1.15077945,
    'mach': lambda x: x / 767.269148,
  },

  'kph': {
    'mph': lambda x: x / 1.609344,
    'mps': lambda x: x / 3.6,
    'kt': lambda x: x / 1.852,
    'mach': lambda x: x / 1234.8,
  },

  'mps': {
    'mph': lambda x: x * 2.23693629,
    'kph': lambda x: x * 3.6,
    'kt': lambda x: x * 1.94384449,
    'mach': lambda x: x / 343,
  },

  'kt': {
    'mph': lambda x: x * 1.15077945,
    'kph': lambda x: x * 1.852,
    'mps': lambda x: x / 1.94384449,
    'mach': lambda x: x / 666.738661,
  },

  'mach': {
    'mph': lambda x: x * 767.269148,
    'kph': lambda x: x * 1234.8,
    'mps': lambda x: x * 343,
    'kt': lambda x: x * 666.738661,
  },

  #-------- Weight conversion --------

  't': {
    'st': lambda x: x * 1.10231131,
    'lt': lambda x: x / 1.01604691,
    'kg': lambda x: x * 1000,
    'g': lambda x: x * 1000000,
    'mg': lambda x: x * 1.0000E+9,
    'lb': lambda x: x * 2204.62262,
    'oz': lambda x: x * 35273.962,
  },

  'st': {
    't': lambda x: x / 1.10231131,
    'lt': lambda x: x / 1.12,
    'kg': lambda x: x * 907.18474,
    'g': lambda x: x * 907184.74,
    'mg': lambda x: x * 907184740,
    'lb': lambda x: x * 142.857143,
    'oz': lambda x: x * 32000,
  },

  'lt': {
    't': lambda x: x * 1.01604691,
    'st': lambda x: x * 1.12,
    'kg': lambda x: x * 1016.04691,
    'g': lambda x: x * 1.0160E+6,
    'mg': lambda x: x * 1.0160E+9,
    'lb': lambda x: x * 2240,
    'oz': lambda x: x * 35840,
  },

  'kg': {
    't': lambda x: x / 1000,
    'st': lambda x: x / 907.18474,
    'lt': lambda x: x / 1016.04691,
    'g': lambda x: x * 1000,
    'mg': lambda x: x * 1000000,
    'lb': lambda x: x * 2.20462262,
    'oz': lambda x: x * 35.273962,
  },

  'g': {
    't': lambda x: x / 1000000,
    'st': lambda x: x / 907184.74,
    'lt': lambda x: x / 1.0160E+6,
    'kg': lambda x: x / 1000,
    'mg': lambda x: x * 1000,
    'lb': lambda x: x / 453.59237,
    'oz': lambda x: x / 28.3495231,
  },

  'mg': {
    't': lambda x: x / 1.0000E+9,
    'st': lambda x: x / 907184740,
    'lt': lambda x: x / 1.0160E+9,
    'kg': lambda x: x / 1000000,
    'g': lambda x: x / 1000,
    'lb': lambda x: x / 453592.37,
    'oz': lambda x: x / 28349.5231,
  },

  'lb': {
    't': lambda x: x / 2204.62262,
    'st': lambda x: x / 2000,
    'lt': lambda x: x / 2240,
    'kg': lambda x: x / 2.20462262,
    'g': lambda x: x * 453.59237,
    'mg': lambda x: x * 453592.37,
    'oz': lambda x: x * 16,
  },

  'oz': {
    't': lambda x: x / 35273.962,
    'st': lambda x: x / 32000,
    'lt': lambda x: x / 35840,
    'kg': lambda x: x / 35.273962,
    'g': lambda x: x * 28.3495231,
    'mg': lambda x: x * 28349.5231,
    'lb': lambda x: x / 16,
  },
  
} 


units = {
  'm': 'Meters',
  'cm': 'Centimeters',
  'mm': 'Millimeters',
  'km': 'Kilometers',
  'mi': 'Miles',
  'ft': 'Feet',
  'in': 'Inches',

  'c': 'Celsius',
  'f': 'Fahrenheit',
  'k': 'Kelvin',
  
  'mph': 'Miles/hour',
  'kph': 'Kilometers/hour',
  'mps': 'Meters/second',
  'kt': 'Knot',
  'mach': 'Mach',

  't': 'Metric ton',
  'st': 'Short ton',
  'lt': 'Long ton',
  'kg': 'Kilogram',
  'g': 'Gram',
  'mg': 'Milligram',
  'lb': 'Pound',
  'oz': 'Ounce',
  
}


numeral_conversions = {
  'dec': {
      'bin': lambda x: bin(int(x))[2:],
      'hex': lambda x: hex(int(x))[2:],
  },
  'bin': {
      'dec': lambda x: int(x, 2),
      'hex': lambda x: hex(int(x, 16))[2:],
  },
  'hex': {
      'dec': lambda x: int(x, 16),
      'bin': lambda x: bin(int(x, 16))[2:],
  },
}


numeral_systems = {
  'dec': 'decimal', 
  'hex': 'hexadecimal', 
  'bin': 'binary'
}
