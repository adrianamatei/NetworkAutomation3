#pylint_check
import pylint
import sys
print(sys.path)


args = [ '--rcfile=pylintrc', 'p2_module16/configure_ftd_int_experiment.py']
pylint.run_pylint(args)