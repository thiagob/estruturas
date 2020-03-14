import importlib
import os

import inspect

def in_unit_test():
  current_stack = inspect.stack()
  for stack_frame in current_stack:
    for program_line in stack_frame[4]:    # This element of the stack frame contains 
      if "unittest" in program_line:       # some contextual program lines
        return True
  return False

folders = [ f.name for f in os.scandir('.') if f.is_dir()]
folders = [f for f in folders if f[0] not in ['.', '_']]
folders.remove('tests')
folders.remove('docs')

# Inform the default library you want to use
library = "template" # <<<<<<<<
if len(folders) == 2:
    library = "thiagob"
else:
    folders.remove('template')
    folders.remove('thiagob')

    library = folders[0]

# elif not in_unit_test():
#     print("Which library do you want to import?")
#     for idx, val in enumerate(folders):
#         print(" Press %i for %s" % (idx, val))
#     n = int(input("Number: "))

#     library = folders[n]

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("from " + library + " import lib")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

lib = importlib.import_module(library)