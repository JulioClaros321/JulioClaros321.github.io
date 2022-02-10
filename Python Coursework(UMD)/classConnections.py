# Julio Claros
# 114153234
# 2018-19-11
# Midterm 2


class Person:
    """
    Function creates a person object with a name parameter as an attribute and
    a set of connections attribute

    """

    def __init__(self, name):
        self.name = name
        self.connections = set()

    def add_connection(self, other):
        """
        Adds a person object to an already existing person objects set of
        connections

        Arg 1: Other (Person Object): omitted to an already existing set of
        connections when called

        Returns:
            N/A
        """
        self.connections.add(other)
        other.connections.add(self)

    def get_second_connections(self):
        """
        Function takes a an instance of a person object, iterates through their
        set of connections and creates a new set of their connection's
        connections.

        Returns:
            secondary (set): a set of a person object's connection's connections
        """
        your_connections = set()
        for people in self.connections:
            for others in people.connections:
                your_connections.add(others)
        your_connections.remove(self)
        secondary = set(your_connections.difference(self.connections))
        return secondary
