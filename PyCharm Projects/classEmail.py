# Julio Claros
# 114153234
# 2018-31-10
# Exercise

"""
Script generates worker's email based on first, last and age provided
"""


class Person:
    """
    Defines a worker and assigns values based on worker first name, last name,
    and age and generates a meaningful worker email based on input provided.

    Arg1: First_name (string): First name of worker
    Arg 2: Last_name (string): last name of worker
    Arg 3: Age (INT): Age of worker

    Returns:
        self.email (string): A string consisting of a workers first name, last
        name, and age all constituted in the making of their personalized email.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + '.' + last_name + str(age) + "@Jcorp.com"

    def worker_info(self):
        print("GENERATING WORKER EMAIL......")
        return self.email


if __name__ == '__main__':
    import sys
    worker1 = Person(sys.argv[1], sys.argv[2], sys.argv[3])
    print(worker1.worker_info())
