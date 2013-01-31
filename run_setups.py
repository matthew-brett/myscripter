""" Run setups """
import os
from os.path import join as pjoin, isdir
import shutil
from glob import glob

if os.name == 'nt':
    bin_sdir = 'Scripts'
else:
    bin_sdir = 'bin'

from subprocess import check_call, CalledProcessError

def mycall(cmd):
    return check_call(cmd, shell=True)

try:
    mycall('virtualenv --help')
except CalledProcessError:
    raise RuntimeError("Need virtualenv installed")

# Run setups
mycall('python setup.py sdist --formats=zip')
sdist = glob(pjoin('dist', '*.zip'))[0]
mycall('python setupegg.py bdist_egg')
egg = glob(pjoin('dist', '*.egg'))[0]
if os.name == 'nt':
    mycall('python setup.py bdist_wininst')
    exe = glob(pjoin('dist', '*.exe'))[0]

def mk_venv(sdir):
    if isdir(sdir):
        shutil.rmtree(sdir)
    mycall('virtualenv ' + sdir)
    return pjoin(sdir, bin_sdir)

shutil.rmtree('build')
bin_dir = mk_venv('venv_repo')
mycall(pjoin(bin_dir, 'python') + ' setup.py install')
bin_dir = mk_venv('venv_sdist')
mycall(pjoin(bin_dir, 'easy_install') + ' ' + sdist)
bin_dir = mk_venv('venv_egg')
mycall(pjoin(bin_dir, 'easy_install') + ' ' + egg)
if os.name == 'nt':
    bin_dir = mk_venv('venv_exe')
    mycall(pjoin(bin_dir, 'easy_install') + ' ' + exe)
