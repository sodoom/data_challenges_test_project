from os import DirEntry
from data_challenges_test_project.lib import added

def test_add():
    output = added(2,4)
    assert isinstance(output, int)
