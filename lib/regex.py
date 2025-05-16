import re

FINDALL_STRING = """
    It's such a lovely day today.
    Where'd all the time go?
    Some weather we're having today, huh?
    Tomorrow never knows!
    Maybe today's just not my day.
    It's clobbering time!
"""

my_pattern = r"[A-Z][A-z',\s]+today[A-z',\s]+[.?]|[A-Z][A-z',\s]+today\."
my_regex = re.compile(my_pattern)


