import json
import random
import string
import os.path
import getopt
import sys
from model.group import Group


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for _ in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
