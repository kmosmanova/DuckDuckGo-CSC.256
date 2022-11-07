import presidents
import pytest

# list of presidents' last names with removed duplicates
PRESIDENTS_LASTNAME = ("Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson",
                     "Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore",
                     "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
                     "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt",
                     "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
                     "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter",
                     "Bush", "Clinton", "Obama", "Trump", "Biden")

# get the list of queried names from duckduckgo
queried_presidents = presidents.get_ddg_presidents()

# extract last names for comparison
queried_lastname = []
for name in queried_presidents:
    queried_lastname.append(name.split(' ')[-1])

# test that all last names are present in the queried results
@pytest.mark.parametrize("president", PRESIDENTS_LASTNAME)
def test_is_all_presidents(president):
    assert president in queried_lastname

