""" Run setups """
from __future__ import print_function

import os
from os.path import join as pjoin, isdir
import shutil
from glob import glob

if os.name == 'nt':
    bin_sdir = 'Scripts'
else:
    bin_sdir = 'bin'

from subprocess import CalledProcessError, Popen, PIPE

def mycall(cmd):
    print('Running: ', cmd)
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out.strip()

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
    mycall('virtualenv ' + '"{0}"'.format(sdir))
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
# A virtualenv with spaces in the path
bin_dir = mk_venv('venv with spaces')
mycall('"{0}" setup.py install'.format(pjoin(bin_dir, 'python')))
