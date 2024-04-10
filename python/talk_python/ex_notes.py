import sys
from typing import Optional


class DbException(Exception):
    pass


class DbConnectionException(DbException):
    pass


def connect_to_db(conn_str, server: Optional[str] = None, port: Optional[int] = None):
    if ('server' in conn_str and server) or ('port' in conn_str and port):
        raise DbConnectionException('Connection string is malformed')

    conn_str += f'&{server=}&{port=}'

    print(f'Connection to DB with {conn_str}')


def setup_app():
    # conn_str = 'mongo://user=mk&password=a&database=talkpython'
    conn_str = 'mongo://user=mk&password=a&database=talkpython&port=1000'

    server = 'localhost'
    port = 27017

    try:
        connect_to_db(conn_str, server, port)
    except DbConnectionException as dbe:
        dbe.add_note('Note: You cannot specify server or port in both the conn str and explicitly')
        dbe.add_note('Note: Amend the conn string and try again.')

        raise


def main():
    # setup_app()
    try:
        setup_app()
        print('App ready')
    except Exception as x:
        print(f'Error starting app:\n\t{type(x).__name__}: {x}')

        if x.__notes__:
            print(f'There are {len(x.__notes__)} notes')

            for n in x.__notes__:
                print(f'Note: {x}')
        
        sys.exit(7)


if __name__ == '__main__':
    main()
