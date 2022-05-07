# version 2

import sys

try:
    from yourscript import Person
except ModuleNotFoundError:
    print("Open the test script and replace 'yourscript' with the name"
          " of your script, minus the .py extension. Also make sure your"
          " script and the test script are in the same directory.",
          file=sys.stderr)
    sys.exit(1)
except ImportError:
    print("Could not import Person from your script.")
    sys.exit(1)

michael = Person("Michael")

assert michael.name == "Michael", \
    "Person.__init__() isn't setting the name attribute properly."
assert michael.connections == set(), \
    ("Person.__init__() isn't initializing the connections attribute to"
     " an empty set.")

emily = Person("Emily")
jessica = Person("Jessica")
jacob = Person("Jacob")
christopher = Person("Christopher")
ashley = Person("Ashley")
matthew = Person("Matthew")
sarah = Person("Sarah")

michael.add_connection(emily)

assert isinstance(michael.connections, set), \
    "Person.add_connection() broke self.connections: it is no longer a set."

assert isinstance(emily.connections, set), \
    "Person.add_connection() broke other.connections: it is no longer a set."

assert michael.connections == {emily}, \
    ("Person.add_connection() failed to add the other object to"
     " self.connections.")

assert emily.connections == {michael}, \
    "Person.add_connection() failed to add self to other.connections."

michael.add_connection(jacob)

assert michael.connections == {emily, jacob}, \
    "The value of self.connections is wrong after adding a second connection."

michael.add_connection(christopher)
michael.add_connection(jessica)

emily.add_connection(christopher)
christopher.add_connection(ashley)
jacob.add_connection(ashley)
jacob.add_connection(matthew)
jessica.add_connection(matthew)
ashley.add_connection(sarah)

assert michael.get_second_connections() == {ashley, matthew}, \
    "Person.get_second_connections() returned the wrong value for Michael."

assert emily.get_second_connections() == {ashley, jacob, jessica}, \
    "Person.get_second_connections() returned the wrong value for Emily."

assert christopher.get_second_connections() == {jacob, jessica, sarah}, \
    "Person.get_second_connections() returned the wrong value for Christopher."

assert ashley.get_second_connections() == {emily, michael, matthew}, \
    "Person.get_second_connections() returned the wrong value for Ashley."

assert sarah.get_second_connections() == {jacob, christopher}, \
    "Person.get_second_connections() returned the wrong value for Sarah."

assert matthew.get_second_connections() == {michael, ashley}, \
    "Person.get_second_connections() returned the wrong value for Matthew."

assert jessica.get_second_connections() == {emily, christopher, jacob}, \
    "Person.get_second_connections() returned the wrong value for Jessica."

assert jacob.get_second_connections() == {jessica, emily, christopher, sarah}, \
    "Person.get_second_connections() returned the wrong value for Jacob."


print("Success! Passed all tests.")
