#pylint_check
import pylint
import sys
print(sys.path)


args = [ '--rcfile=pylintrc', 'tema2_problema1.py']
pylint.run_pylint(args)