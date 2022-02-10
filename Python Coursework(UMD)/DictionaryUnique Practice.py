
def places_travel(dictionary, name):
    unique = set(dictionary[name])
    places = set()
    total = set()
    for people in dictionary:
        if people == name: continue
        else:
            places = dictionary[people]
            total = total.union(places)
        difference = unique.difference(total)
    print(difference)


def unique_places(dictionary, name):
    main_person = set(dictionary[name])
    total = set()
    unqiue = set()
    for people in dictionary:
        if people == name:
            continue
        else:
            guess = (dictionary[people])
            total = total.union(guess)
        unique = main_person.difference(total)
    print(unique)


if __name__ == '__main__':
    places_travel({'Julie': ['United Kingdom', 'Japan', 'Turkey', 'Morocco',
    'Mexico', 'Brazil'], 'Aaron': ['Japan', 'Thailand', 'South Korea', 'Vietnam'
    ,'Australia', 'India'], 'Nikki': ['Italy', 'Greece', 'Turkey', 'Slovakia',
    'Mexico', 'Canada', 'Thailand']}, "Nikki")

    unique_places({'Julie': ['United Kingdom', 'Japan', 'Turkey', 'Morocco',
    'Mexico', 'Brazil'], 'Aaron': ['Japan', 'Thailand', 'South Korea', 'Vietnam'
    ,'Australia', 'India'], 'Nikki': ['Italy', 'Greece', 'Turkey', 'Slovakia',
    'Mexico', 'Canada', 'Thailand']}, "Nikki")

