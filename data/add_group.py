import random
import string
from model.group import Group


constant = [
    Group(name="name-1", header="header-1", footer="footer-1"),
    Group(name="name-2", header="header-2", footer="footer-2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for _ in range(5)
]

