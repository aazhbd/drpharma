import sys, os

os.environ.update(LC_CTYPE='en_US.UTF-8', LC_ALL='en_US.UTF-8')

_curdir = os.path.abspath(os.curdir)
os.chdir(os.path.dirname(__file__))
SETTINGS_ROOT = os.path.abspath(os.curdir)
APP_ROOT = os.path.abspath('../..')
LIB_ROOT = os.path.abspath('%s/libs' % APP_ROOT)
os.chdir(_curdir); del _curdir

for root in (APP_ROOT, LIB_ROOT):
    if(root not in sys.path):
        sys.path.insert(0, root)

for script_dir in ('bin', 'Scripts'):
    try:
        _pyenv = os.path.join(APP_ROOT, 'pyenv', script_dir, 'activate_this.py')
        execfile(_pyenv, dict(__file__=_pyenv))
        del _pyenv
    except:
        pass

del sys, os
