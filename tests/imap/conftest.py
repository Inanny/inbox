""" Fixtures don't go here; see util/base.py and friends. """
# fixtures that are available by default
from tests.util.base import config, db, log, absolute_path


def pytest_generate_tests(metafunc):
    if 'db' in metafunc.fixturenames:
        dumpfile = absolute_path(config()['BASE_DUMP'])
        savedb = False

        metafunc.parametrize('db', [(dumpfile, savedb)], indirect=True)


def pytest_report_header():
    return "\nIMPORTANT: Remember to run py.test -s test_filename.py, "\
        "OAuth may need to be re-run!\n"
