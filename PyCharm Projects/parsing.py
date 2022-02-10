import pandas as pd
import mysql.connector
import csv

db = mysql.connector.connect(host="localhost", database ="movies",
                             user="root", password="Immalegacy5")

links = pd.read_csv("links.csv")
credits = pd.read_csv("credits.csv")
keywords = pd.read_csv("keywords.csv")
movies = pd.read_csv("movies_metadata.csv", dtype="unicode", low_memory=False,
                     dialect= None)
cursor = db.cursor()


def movie_table():

    counter = 0
    while counter < 20:
        sql_formula = "INSERT INTO titles (id, movie_id, imdb_id, title) " \
                  "VALUES (%s, %s, %s, %s)"

        title = (movies["id"][counter], counter + 1, movies["imdb_id"][counter],
             movies["title"][counter])

        cursor.execute(sql_formula, title)
        db.commit()
        counter += 1


def financial_table():
    counter = 0
    sql_formula = "INSERT INTO financial_info (id, budget, revenue) " \
                  "VALUES (%s, %s, %s)"

    while counter < 20:

        title = (movies["id"][counter], movies["budget"][counter],
                 movies["revenue"][counter])

        cursor.execute(sql_formula, title)
        db.commit()
        counter += 1


def movie_crew():

    sql_formula = "INSERT INTO movie_crew (imdb_id, director, main_char," \
                      " leading_actor) VALUES (%s, %s, %s, %s)"

    titles = [(movies["imdb_id"][0], "John Lasseter", "Woody", "Tom Hanks"),
        (movies["imdb_id"][1], "Larry J Franco", "Alan Parrish", "Robin Williams"),
        (movies["imdb_id"][2], "Howard Deutch", "Max Goldman", "Walter Mathhau"),
        (movies["imdb_id"][3], "Forest Whitaker", "Savannah Vannah", "Whitney Houston"),
        (movies["imdb_id"][4], "Alan Silvestri", "George Banks", "Steve Martin"),
        (movies["imdb_id"][5], "Michael Mann", "Vincent Hanna", "Al Pacino"),
        (movies["imdb_id"][6], "Sydney Pollack", "Linus Larrabee", "Harrison Ford"),
        (movies["imdb_id"][7], "David Loughery", "Tom Sawyer", "Jonathan Taylor"),
        (movies["imdb_id"][8], "Peter Hyams", "Darren Thomas", "Jean-Claude Van"),
        (movies["imdb_id"][9], "Martin Campbell", "James Bond", "Pierce Brosnan"),
        (movies["imdb_id"][10], "John Seale", "Andrew Shepard", "Michael Douglas"),
        (movies["imdb_id"][11], "Adam Weiss", "Dracula", "Leslie Nielsen"),
        (movies["imdb_id"][12], "Steven Spielberg", "Balto", "Kevin Bacon"),
        (movies["imdb_id"][13], "Oliver Stone", "Richard Nixon", "Anthony Hopkins"),
        (movies["imdb_id"][14], "Peter Levy", "Morgan Adams", "Greena Davis"),
        (movies["imdb_id"][15], "Martin Scorsese", "Sam Ace", "Robert De Niro"),
        (movies["imdb_id"][16], "Ang Lee", "Marianne Dashwood", "Kate Winslet"),
        (movies["imdb_id"][17], "Combustible Edison", "Ted the Bellhop", "Tim Roth"),
        (movies["imdb_id"][18], "Steve Oedekerk", "Ace Ventura", "Jim Carrey"),
        (movies["imdb_id"][19], "Joseph Ruben", "John", "Wesley Snipes")]
        #(movies["id"][20], "Barrey Sonnenfeld", "Chili Palmer", "John Travolta")]
        #(movies["id"][21], "Mark Tarlov", "Helen Hudson", "Sigourney Weaver"),
        #(movies["id"][22], "Richard Donner", "Robert Rath", "Sylvester Stallone"),
        #(movies["id"][23], "Victor Salva", "Jessie Caldwell", "Mary Steenburgen"),
        #(movies["id"][24], "Stuart Reynolds", "Ben Sanderson", "Nicholas Cage"),
        #(movies["id"][25], "William Shakespeare", "Othello", "Laurence"),
        #(movies["id"][26], "Lesli Linka", "Young Roberta Martin", "Christina Ricci"),
        #(movies["id"][27], "Roger Mitchell", "Anne Elliott", "Amanda Root"),
        #(movies["id"][28], "Jean-Pierre Jeunet", "One", "Ron Perlman"),
        #(movies["id"][29], "Zhang Yimou", "Xiao Jingbao", "Gong Li") ]

    cursor.executemany(sql_formula, titles)
    db.commit()


def production_company():
    sql_formula = "INSERT INTO production_company (imdb_id, prod_comp, " \
                  "prod_country, release_date) VALUES (%s, %s, %s, %s)"

    titles = [(movies["imdb_id"][0], "Pixar Animation Studios", "USA", movies["release_date"][0]),
              (movies["imdb_id"][1], "Tristar Pictures", "USA", movies["release_date"][1]),
              (movies["imdb_id"][2], "Warner Bros", "USA", movies["release_date"][2]),
              (movies["imdb_id"][3], "Twentieth Century Fox Film", "USA", movies["release_date"][3]),
              (movies["imdb_id"][4], "Sandollar Productions", "USA", movies["release_date"][4]),
              (movies["imdb_id"][5], "Regency Enterprises", "USA", movies["release_date"][5]),
              (movies["imdb_id"][6], "Paramount Pictures", "USA, Germany", movies["release_date"][6]),
              (movies["imdb_id"][7], "Walt Disney Pictures", "USA", movies["release_date"][7]),
              (movies["imdb_id"][8], "Universal Pictures", "USA", movies["release_date"][8]),
              (movies["imdb_id"][9], "United Artist", "USA, United Kingdom", movies["release_date"][9]),
              (movies["imdb_id"][10], "Columbia Pictures", "USA", movies["release_date"][10]),
              (movies["imdb_id"][11], "Columbia Pictures", "USA, France", movies["release_date"][11]),
              (movies["imdb_id"][12], "Universal Pictures", "USA", movies["release_date"][12]),
              (movies["imdb_id"][13], "Hollywood Pictures", "USA", movies["release_date"][13]),
              (movies["imdb_id"][14], "Le Studio Canal + Mark Productions", "USA, Germany, France", movies["release_date"][14]),
              (movies["imdb_id"][15], "Universal Pictures", "USA, France", movies["release_date"][15]),
              (movies["imdb_id"][16], "Columbia Pictures", "USA, United Kingdom", movies["release_date"][16]),
              (movies["imdb_id"][17], "Miramax Films", "USA", movies["release_date"][17]),
              (movies["imdb_id"][18], "Warner Bros", "USA", movies["release_date"][18]),
              (movies["imdb_id"][19], "Columbia Pictures", "USA", movies["release_date"][19])]

    cursor.executemany(sql_formula, titles)
    db.commit()


def ratings_table():
    counter = 0
    sql_formula = "INSERT INTO ratings (id, popularity) VALUES (%s, %s)"

    while counter < 20:
        title = (movies["id"][counter], movies["popularity"][counter])

        cursor.execute(sql_formula, title)
        db.commit()
        counter += 1


def movie_summary():

    sql_formula = "INSERT INTO movie_summary (movie_id, overview, adult, " \
                  "runtime) VALUES (%s, %s, %s, %s)"

    titles = [(1, movies["overview"][0], movies["adult"][0], movies["runtime"][0]),
              (2, movies["overview"][1], movies["adult"][1], movies["runtime"][1]),
              (3, movies["overview"][2], movies["adult"][2], movies["runtime"][2]),
              (4, movies["overview"][3], movies["adult"][3], movies["runtime"][3]),
              (5, movies["overview"][4], movies["adult"][4], movies["runtime"][4]),
              (6, movies["overview"][5], movies["adult"][5], movies["runtime"][5]),
              (7, movies["overview"][6], movies["adult"][6], movies["runtime"][6]),
              (8, movies["overview"][7], movies["adult"][7], movies["runtime"][7]),
              (9, movies["overview"][8], movies["adult"][8], movies["runtime"][8]),
              (10, movies["overview"][9], movies["adult"][9], movies["runtime"][9]),
              (11, movies["overview"][10], movies["adult"][10], movies["runtime"][10]),
              (12, movies["overview"][11], movies["adult"][11], movies["runtime"][11]),
              (13, movies["overview"][12], movies["adult"][12], movies["runtime"][12]),
              (14, movies["overview"][13], movies["adult"][13], movies["runtime"][13]),
              (15, movies["overview"][14], movies["adult"][14], movies["runtime"][14]),
              (16, movies["overview"][15], movies["adult"][15], movies["runtime"][15]),
              (17, movies["overview"][16], movies["adult"][16], movies["runtime"][16]),
              (18, movies["overview"][17], movies["adult"][17], movies["runtime"][17]),
              (19, movies["overview"][18], movies["adult"][18], movies["runtime"][18]),
              (20, movies["overview"][19], movies["adult"][19], movies["runtime"][19])]

    cursor.executemany(sql_formula, titles)
    db.commit()

def genre():

    sql_formula = "INSERT INTO genre (movie_id, genre) VALUES (%s, %s)"

    titles = [(1, "Animation,Comedy,Family"),
              (2, "Adventure,Fantasy,Family"),
              (3, "Romance,Comedy"),
              (4, "Comedy,Drama,Romance"),
              (5, "Comedy"),
              (6, "Action,Drama,Thriller"),
              (7, "Comedy,Romance"),
              (8, "Action,Adventure,Drama,Family"),
              (9, "Action,Adventure,Thriller"),
              (10, "Adventure,Action,Thriller"),
              (11, "Comedy,Drama,Romance"),
              (12, "Comedy,Horror"),
              (13, "Family,Animation,Adventure"),
              (14, "History,Drama"),
              (15, "Action,Adventure"),
              (16, "Drama,Crime"),
              (17, "Drama,Romance"),
              (18, "Crime,Comedy"),
              (19, "Crime,Comedy,Adventure"),
              (20, "Action,Comedy,Adventure")]

    cursor.executemany(sql_formula, titles)
    db.commit()


if __name__ == '__main__':
    production_company()