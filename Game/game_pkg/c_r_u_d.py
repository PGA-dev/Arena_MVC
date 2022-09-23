'''CRUD
    --SQLite3 currently used
    --Upgrade to SQLAlchemy and Dataset a future param
    --used by model to interact with data *list of dictionaries in the old model
'''

from game_pkg import exceptions as mvc_exc
import sqlite3
from sqlite3 import OperationalError, IntegrityError, ProgrammingError

'''
Basic SQLite3 connectors
'''
DB_name = 'GameDB'


def connect_to_db(db=None):
    """Connect to a sqlite DB. Create the database if there isn't one yet.

    Open a connection to a SQLite DB (either a DB file or an in-memory DB).
    When a database is accessed by multiple connections, and one of the
    processes modifies the database, the SQLite database is locked until that
    transaction is committed.

    Parameters
    ----------
    db : str
        database name (without .db extension). If None, create an In-Memory DB.

    Returns
    -------
    connection : sqlite3.Connection
        connection object
    """
    if db is None:
        mydb = ':memory:'
        print('New connection to in-memory SQLite DB...')
    else:
        mydb = '{}.db'.format(db)
        print('New connection to SQLite DB...')
    connection = sqlite3.connect(mydb)
    return connection




# TODO: use this decorator to wrap commit/rollback in a try/except block ?
# see http://www.kylev.com/2009/05/22/python-decorators-and-database-idioms/

# DB Connect @wrapper
def connect(func):
    """Decorator to (re)open a sqlite database connection when needed.

    A database connection must be open when we want to perform a database query
    but we are in one of the following situations:
    1) there is no connection
    2) the connection is closed

    Parameters
    ----------
    func : function
        function which performs the database query

    Returns
    -------
    inner func : function
    """
    def inner_func(conn, *args, **kwargs):
        try:
            # I don't know if this is the simplest and fastest query to try
            conn.execute(
                'SELECT name FROM sqlite_temp_master WHERE type="table";')
        except (AttributeError, ProgrammingError):
            conn = connect_to_db(DB_name)
        return func(conn, *args, **kwargs)
    return inner_func


# Disconnect @wrapper
def disconnect_from_db(db=None, conn=None):
    if db is not DB_name:
        print("You are trying to disconnect from a wrong DB")
    if conn is not None:
        conn.close()

'''
SQL Injection scrubber
'''
def scrub(input_string):
    """Clean an input string (to prevent SQL injection).

    Parameters
    ----------
    input_string : str

    Returns
    -------
    str
    """
    return ''.join(k for k in input_string if k.isalnum())

@connect
def create_table(conn, table_name):
    table_name = scrub(table_name)
    sql = 'CREATE TABLE {} (rowid INTEGER PRIMARY KEY AUTOINCREMENT,' \
          'name TEXT UNIQUE, ac INTEGER, damage INTEGER, hp INTEGER, to_hit REAL)'.format(table_name)
    try:
        conn.execute(sql)
    except OperationalError as e:
        print(e)



@connect
def insert_char(conn, name, ac, damage, hp, to_hit, table_name):
    table_name = scrub(table_name)
    sql = "INSERT INTO {} ('name', 'ac', 'damage', 'hp', 'to_hit') VALUES (?, ?, ?, ?, ?)"\
        .format(table_name)
    try:
        conn.execute(sql, (name, ac, damage, hp, to_hit,))
        conn.commit()
    except IntegrityError as e:
        raise mvc_exc.CharAlreadyStored(
            f'{e}: {name} already stored in table {table_name}')


@connect
def insert_chars(conn, chars, table_name):
    table_name = scrub(table_name)
    sql = "INSERT INTO {} ('name', 'ac', 'damage', 'hp', 'to_hit') VALUES (?, ?, ?, ?, ?)"\
        .format(table_name)
    entries = list()
    for x in chars:
        entries.append((x['name'], x['ac'], x['damage'], x['hp'], x['to_hit']))
    try:
        conn.executemany(sql, entries)
        conn.commit()
    except IntegrityError as e:
        print('{}: at least one in {} was already stored in table "{}"'
              .format(e, [x['name'] for x in chars], table_name))


'''
converter
'''
def tuple_convert(attribute_tuple):
    att_dict = dict()
    att_dict['id'] = attribute_tuple[0]
    att_dict['name'] = attribute_tuple[1]
    att_dict['ac'] = attribute_tuple[2]
    att_dict['damage'] = attribute_tuple[3]
    att_dict['hp'] = attribute_tuple[4]
    att_dict['to_hit'] = attribute_tuple[5]
    return att_dict


'''
Select Statements
'''
@connect
def select_char(conn, char_name, table_name):
    table_name = scrub(table_name)
    char_name = scrub(char_name)
    sql = 'SELECT * FROM {} WHERE name="{}"'.format(table_name, char_name)
    c = conn.execute(sql)
    result = c.fetchone()
    if result is not None:
        return tuple_convert(result)
    else:
        raise mvc_exc.CharNotStored(
            'Can\'t read "{}" because it\'s not stored in table "{}"'
            .format(char_name, table_name))


@connect
def select_all(conn, table_name):
    table_name = scrub(table_name)
    sql = 'SELECT * FROM {}'.format(table_name)
    c = conn.execute(sql)
    results = c.fetchall()
    return list(map(lambda x: tuple_convert(x), results))

'''
Update Character functionality
'''
@connect
def update_char(conn, name, ac, damage, hp, to_hit, table_name):
    table_name = scrub(table_name)
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE name=? LIMIT 1)'\
        .format(table_name)
    sql_update = 'UPDATE {} SET price=?, quantity=? WHERE name=?'\
        .format(table_name)
    c = conn.execute(sql_check, (name,))  # we need the comma
    result = c.fetchone()
    if result[0]:
        c.execute(sql_update, ( ac, damage, hp, to_hit, name))
        conn.commit()
    else:
        raise mvc_exc.CharNotStored(
            'Can\'t update "{}" because it\'s not stored in table "{}"'
            .format(name, table_name))

'''
Delete Character Functionality
'''
@connect
def delete_char(conn, name, table_name):
    table_name = scrub(table_name)
    sql_check = 'SELECT EXISTS(SELECT 1 FROM {} WHERE name=? LIMIT 1)'\
        .format(table_name)
    table_name = scrub(table_name)
    sql_delete = 'DELETE FROM {} WHERE name=?'.format(table_name)
    c = conn.execute(sql_check, (name,))  # we need the comma
    result = c.fetchone()
    if result[0]:
        c.execute(sql_delete, (name,))  # we need the comma
        conn.commit()
    else:
        raise mvc_exc.CharNotStored(
            'Can\'t delete "{}" because it\'s not stored in table "{}"'
            .format(name, table_name))





