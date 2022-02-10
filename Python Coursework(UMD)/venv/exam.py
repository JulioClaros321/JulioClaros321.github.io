def places_traveled(dictionary, name, name_two):
    main_person = set(dictionary[name])
    second_person = set(dictionary[name_two])
    difference = main_person.difference(second_person)
    print(difference)

if __name__ == '__main__':
    places_traveled({'Julie': {'United Kingdom', 'Japan', 'Turkey', 'Morocco',
    'Mexico', 'Brazil'},'Aaron': {'Japan', 'Thailand', 'South Korea', 'Vietnam',
    'Australia', 'India'}, 'Nikki': {'Italy', 'Greece', 'Turkey', 'Slovakia',
    'Mexico', 'Canada', 'Thailand'}}, "Julie", "Aaron")