print('\033[1m' + 'Comodi  Copyright (C) 2013  Andreas Backx'.center(80))
print('This program comes with ABSOLUTELY NO WARRANTY.'.center(80))
print('This is free software, and you are welcome to redistribute it under'.center(80))
print('certain conditions; visit \'http://www.gnu.org/licenses\' for details.'.center(80) + '\033[0m\n')

from libs import Config
from libs import Bootstrap as lib_bootstrap

Bootstrap = lib_bootstrap.Bootstrap()
