# Wrapper to run setup.py using setuptools

import setuptools

if __name__ == '__main__':
    exec(open('setup.py', 'rt').read(), dict(__name__='__main__'))
