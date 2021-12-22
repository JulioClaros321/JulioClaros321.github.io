class Information:
    def __init__(self, fullname, username, date_of_birth, email,
                 confirm_email, password):
        self.fullname = fullname
        self.username = username
        self.date_of_birth = date_of_birth
        self.email = email
        self.confirm_email = confirm_email
        self.password = password


def gettop100fromdate(num_date):
    chart = billboard.ChartData('hot-100', date=num_date)
    print(chart)


def get_top100(num_date):
    num_one = input("What music should we return to you?: ")
    chart = billboard.ChartData('hot-100', date=num_date)
    print(chart[int(num_one) - 1])


def create_playlist(num_date):
    chart = billboard.ChartData('hot-100', date=num_date)
    playlist = set()
    while len(playlist) < 30:
        number = random.randint(1, 100)
        song = chart[number]
        if song in playlist:
            continue
        else:
            playlist.add(song)
        print(number, song)


def random_one(num_date, one_song):
    chart = billboard.ChartData('hot-100', date=num_date)
    number = random.choice(range(100))
    song = chart[number]
    rand_song = chart[one_song]
    print(rand_song)

    search_bar = str(rand_song)
    query = urllib.parse.quote(search_bar)
    searches = list()
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    browser = webbrowser.get()
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        searches.append('https://www.youtube.com' + vid['href'])
    browser.open(searches[0])


def just_one(num_date):
    chart = billboard.ChartData('hot-100', date=num_date)
    number = random.choice(range(100))
    song = chart[number]
    print(song)

    response = input("Would you like to play this song on Youtube? Y or N:")
    if response.lower() == "y":
        search_bar = str(song)
        query = urllib.parse.quote(search_bar)
        searches = list()
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        browser = webbrowser.get()
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            searches.append('https://www.youtube.com' + vid['href'])
        browser.open(searches[0])


def user_one(num_date, preference):
    chart = billboard.ChartData('hot-100', date=num_date)
    number = chart[preference]
    print(number)


def bargraph(num_date):
    chart = billboard.ChartData('hot-100', date=num_date)
    lst = list()
    lst1 = list()
    for song in chart[0:10]:
        lst.append(song.artist)
        lst1.append(song.weeks)

    y_pos = np.arange(len(lst))

    plt.barh(y_pos, lst1, align='center', alpha=0.5)
    plt.yticks(y_pos, lst)
    plt.xlabel('Number of Weeks')
    plt.title('Number of Weeks on Billboard Chart')
    plt.show()


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    import billboard
    import random
    import urllib.request
    from bs4 import BeautifulSoup
    import webbrowser
    import datetime

    print("Welcome to our Music Website!!")
    print("\n")
    print("Before using our website, you will need to fill out"
          "some personal information")
    print("\n")

    fullname = input("Enter your full name: ")
    username = input("Enter a username: ")
    dob = input("Enter your date of birth (yyyy-mm-dd): ")

    try:
        date_of_birth = datetime.datetime.strptime(dob, "%Y-%m-%d")
    except:
        print("Incorrect date!")

    email = input("Enter your email: ")
    confirm_email = input("Confirm your email again: ")
    password = input("Enter a password for your account (alphabets only):")
    for letter in password:
        if letter.isalpha() == (1 == 2):
            print("Make sure password contains just letters!")
            password = input("Enter another password for your account please:")

    user = Information(
        fullname,
        username,
        dob,
        email,
        confirm_email,
        password
    )

    date = input("Enter a date to receive top 100 songs (yyyy-mm-dd): ")
    gettop100fromdate(date)

    print("\n")

    answer = input("Generate 30 song playlist from year? Y or N: ")
    if answer.lower() == "y":
        create_playlist(date)
        one_song = int(input("Pick one song(row) to play: "))
        random_one(date, one_song)
    elif answer.lower() == "n":
        just_1 = input("Do you want just one random song? Y or N: ")
        if just_1.lower() == "y":
            just_one(date)
        elif just_1.lower() == "n":
            pick = input(
                "Would you like to pick the song for yourself? Y or N: ")
            if pick.lower() == "y":
                preference = int(input("Which row would you like?: "))
                user_one(date, preference - 1)
            elif pick.lower() == "n":
                print(
                    "We don't know what you want so... here is the top 100 again...")
                gettop100fromdate(date)

    bar_graph = input("Do you want a bar graph that shows the"
                      "number of weeks an artist"
                      "was on the charts? Y or N:")
    if bar_graph.lower() == "y":
        bargraph(date)





