from .main import DownRev

def autoload():
    return DownRev()

config = [{
    'name': 'downrev',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'DownRev',
            'description': 'See <a href="http://www.downrev.net">DownRev</a>',
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACJUlEQVQ4jaWTTU9TQRSGn7kd7rdtb29bMSFtMAGJwNpoNHGpv8GNS/+AS/+Cf8PEnQt2bjAuXElcENGgwQCthZa29PN+zbgAqbAznM0k75mcec47eUXtxWvNNUo65hwC0HBxXq2rfXGua0D6tnkdAGTeMbH9IpUwxDQU2XTIfqtDphRLq4s8qM+z157S7MdEccKo16bd7aLPWWXetTHzJSphiKXG3Hu8TsEyeLPxiXC+TDnIs7PXgmmC1AbV+h2q4TEHjYOzAYFnExkCNR3SOG7wrnnI4lKN+t01Gu0TtkZH/D4+uUBOmyO8hRVq8YDBJEIWPZu2AgMIPAeNpnPQIsmdMnLKeOmUwLPPgQUCDXZGpVoi1+4iS75DbwCGgIJvX3J+V0RYVg7Pdy7pw5JLcDomnTpnA370J8RpRimYXQTI+z5xFFE1zvRMabZ7GeJkBCqm5DvIwHfIMcJAE/x9SYNWiu4gYmes2DqKUIlikiiqNyRPqyNcz52ZaObAkoLAm63w5VeH5uGYtZsu99cLZJlic7dDaxJT8EJ8ew4AI/Ac3LyH61oUPRtL5vje7LGxfUSoI3w09WrA7Vtlnj9aZrlo8PZrh6JrEXgOsuBaVG4vsHnY4cP7b0T9CbXA4eWTVT7vtXBtk4I7I3v2cIVXH38yFZJ5dw6x3+7rWGnIUjKlMADLsgBQSpGmCaZpXfqFJE0QCHJSIrrDyX+n8d/QiShJrxXnP+ow2eJmJnk0AAAAAElFTkSuQmCC',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'passkey',
                    'default': '',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 0,
                    'description': 'Starting score for each release found via this provider.',
                },
            ],
        },
    ],
}]
