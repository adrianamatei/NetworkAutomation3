#pylint_check
import pylint
import sys
print(sys.path)


args = [ '--rcfile=pylintrc', 'configure_ftd_int_experiment.py']
pylint.run_pylint(args)