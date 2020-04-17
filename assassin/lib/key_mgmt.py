# -*- coding: utf-8 -*-

import os
import logging
from pathlib import Path
import apiKeys


def shodan_key():
    '''
    Function to load keys from environment vars rather that static file
    '''
    if 'SHODAN_KEY' in os.environ:
        shodanKey = os.environ['SHODAN_KEY']
        logging.debug('Found SHODAN_KEY in env vars')
        return shodanKey
    elif apiKeys.shodanKey != 'CHANGEME':
        '''
        apiKeys.py is a custom file you need to create & update
        Put it in the same directory as assassin.py
        Set the shodanKey from static file when value is not CHANGEME
        '''
        shodanKey = apiKeys.shodanKey
        logging.debug('Set shodanKey from apiKeys.py')
        return shodanKey
    logging.debug('Did NOT find SHODAN_KEY in env vars or in apiKeys.py file')
    return False


__author__ = ''
__copyright__ = ''
__credits__ = ['']
__license__ = 'http://www.apache.org/licenses/LICENSE-2.0'
__version__ = ''
__maintainer__ = ''
__email__ = 'fdiaz@paloaltonetworks.com'
