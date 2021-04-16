from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator, print_json
from pprint import pprint
from school_wiz import SchoolWiz, str2Fun
import fire

import os
import io
import sys
import time
import json
import pysnooper

sys.path.append(".")


def hello(name="World"):
    return "Hello %s!" % name

@pysnooper.snoop('./log/file.log')
class Utility(object):
    """A simple utility class."""

    # [START functions_microtime]
    def microtime(self, get_as_float=False):
        """microtime() returns the number of seconds since the Unix epoch (0:00:00 January 1,1970 GMT) 
        get_as_float, boolean, optional, if True, microtime() returns a float"""
        return round(time.time()) if not get_as_float else float(time.time())
    # [END functions_microtime]

    # [START functions_url_path_]
    def url_path_(self, base_url):
        """url_path_() returns the path component (parts) of incoming Flask request URL"""
        if base_url is not None:
            from urllib.parse import unquote, urlparse
            from pathlib import PurePosixPath
            return PurePosixPath(
                unquote(
                    urlparse(
                        base_url
                    ).path
                )
            ).parts
        return None
    # [END functions_url_path_]



class Pick(object):
    """A simple pick any cli class."""

    # [START functions_any]
    def any(self, verbose=False):
        style = style_from_dict({
            Token.Separator: '#cc5454',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',
            Token.Answer: '#f44336 bold',
            Token.Question: '',
        })

        questions = [
            {
                'type': 'checkbox',
                'message': 'Select toppings',
                'name': 'toppings',
                'choices': [
                    Separator('= The Meats ='),
                    {
                        'name': 'Ham'
                    },
                    {
                        'name': 'Ground Meat'
                    },
                    {
                        'name': 'Bacon'
                    },
                    Separator('= The Cheeses ='),
                    {
                        'name': 'Mozzarella'
                    },
                    {
                        'name': 'Cheddar'
                    },
                    {
                        'name': 'Parmesan'
                    },
                    Separator('= The usual ='),
                    {
                        'name': 'Mushroom'
                    },
                    {
                        'name': 'Tomato'
                    },
                    {
                        'name': 'Pepperoni'
                    },
                    Separator('= The extras ='),
                    {
                        'name': 'Pineapple'
                    },
                    {
                        'name': 'Extra cheese',
                        'disabled': 'legacy'
                    },
                    {
                        'name': 'Olives',
                        'disabled': 'legacy'
                    }
                ],
                'validate': lambda answer: 'You must choose at least one topping.'
                if len(answer) == 0 else True
            }
        ]

        if verbose is True:
            @pysnooper.snoop()
            def runWithVerboseOutput():
                answers = prompt(questions, style=style)
                pprint(answers)
                return None

            runWithVerboseOutput()
            return None

        answers = prompt(questions, style=style)
        pprint(answers)
        return None
        # [END functions_any]


if __name__ == '__main__':
    custom_style_2 = style_from_dict({
        Token.Separator: '#6C6C6C',
        Token.QuestionMark: '#FF9D00 bold',
        Token.Selected: '#5F819D',
        Token.Pointer: '#FF9D00 bold',
        Token.Instruction: '',
        Token.Answer: '#5F819D bold',
        Token.Question: '',
    })

    questions = [
        {
            'type': 'password',
            'message': 'What\'s the passcode?',
            'name': 'password'
        }
    ]

    str0 = prompt(questions, style=custom_style_2)['password']

    if not str0:
        pprint(''.join(['Unauthorized request~!']))
        sys.exit(1)

    str1 = str(hash(str0))
    str2 = str(hash(str2Fun()))
    str1_hex_id_debug = str(hash(''.join([hex(id(str1))[:5], str1]))).replace('-', '')

    if len(str1) not in [len(str2)]:
        pprint(''.join(['Unauthorized request~! ', str1_hex_id_debug]))
        sys.exit(1)

    if str1 not in [str2]:
        pprint(''.join(['Unauthorized request~! ', str1_hex_id_debug]))
        sys.exit(1)

    # https://github.com/google/python-fire/blob/master/docs/guide.md
    fire.Fire({  # when you call Fire, it fires off (executes) your command
        'hello': hello,
        'u': Utility(),
        'wiz': SchoolWiz(),
        'pick': Pick()
    })

# From the command line:
# python main.py hello
# python main.py hello --name=David
# python main.py hello --help

# python main.py u microtime -get_as_float True
# python main.py u url_path_ -base_url 'https://google.com/documents/templates/?templateKey=AziJs92kSAMoq90NFALm2opS'
# python main.py u --help

# python main.py pick any
# python main.py pick any --verbose
