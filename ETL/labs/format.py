
import re

def format_string_strip(value):
    valor_format  = value.strip()
    return valor_format


def format_string_exp(value):
    valor_format  = re.sub(' +',' ',value)
    return valor_format
 
def format_string(value):
    valor_format  = re.sub(' +',' ',value.strip())
    return valor_format 

print('Format strip:')
print(format_string_strip(' Hello '))
print(format_string_strip('Espacios al final '))
print(format_string_strip('    Espacios al inicio '))
print(format_string_strip('Espacios              entre             palabras'))


print('Format expresion regular:')
print(format_string_exp(' Hello '))
print(format_string_exp('Espacios al final '))
print(format_string_exp('    Espacios al inicio '))
print(format_string_exp('Espacios              entre             palabras'))


print('Format final:')
print(format_string(' Hello '))
print(format_string('Espacios al final '))
print(format_string('    Espacios al inicio '))
print(format_string('Espacios              entre             palabras'))