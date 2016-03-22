#!/usr/bin/env python

"""
Execute 'git branch -a'
"""

from __future__ import print_function
import sys
import subprocess
import pdb

BAD_CALL = 99 

def execute(command):
    """Execute a shell command and return the return code, standard output,
    and standard error."""

    try :
        process = subprocess.Popen(command,
                                   shell=False,
                                   close_fds=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        out, err = process.communicate()
        code = process.returncode
    except Exception as e :
        code, out, err = ( BAD_CALL, '', str(e) )

    return code, out, err

def main() :
    command = [ 'git', 'branch', '-a' ]
    code, out, err  = execute(command) 
    if code == 0 :
        print(out)
    else :
        print("Error: {} ({})".format(err, code), file=sys.stderr)

    return code

if __name__ == '__main__' :
    sys.exit(main())
