import os
from dotenv import load_dotenv
from dotenv import dotenv_values


def br(delimiter='-', length=80):
    print(f'\n{delimiter * length}\n')


br()


load_dotenv()  # take environment variables from .env
# load_dotenv(find_dotenv(usecwd=True))

# os.getenv('TOKEN', default='Not found')
token = os.getenv('TOKEN', 'Not Found')
# token = os.getenv('TOKEN', None)

# environs = dotenv_values('.env')

# print(token)
#
# print(environs)

config = {
    **dotenv_values('.env'),
    **dotenv_values('.env.dev'),
    **dotenv_values('.env.sensitive'),
    # **os.environ
}


print(config)

br()

print(token)
