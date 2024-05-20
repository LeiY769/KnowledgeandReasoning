import psycopg2
from psycopg2 import sql
import csv

connect = psycopg2.connect(host="localhost",dbname = "postgres", user = "postgres", password = "210901", port = 5432)

cur = connect.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS person(
    person_id INT NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NULL,

    PRIMARY KEY (person_id)
);
""")
cur.execute(""" CREATE TABLE IF NOT EXISTS country(
    country_name VARCHAR(255) NOT NULL,
    country_id INT NOT NULL,
    PRIMARY KEY (country_id)
);
            """)
cur.execute(""" CREATE TABLE IF NOT EXISTS rating(
    rating_name VARCHAR(255) NOT NULL,
    rating_id INT NOT NULL,

    PRIMARY KEY (rating_id)
);
            """)
cur.execute(""" CREATE TABLE IF NOT EXISTS show(
    show_id VARCHAR(127) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description_film VARCHAR(4095) NOT NULL,
    duration INT NOT NULL,
    type_show VARCHAR(255) NOT NULL,
    release_date INT NOT NULL,
    date_added VARCHAR(127)NOT NULL,

    PRIMARY KEY (show_id)
); 
            """)
cur.execute("""CREATE TABLE IF NOT EXISTS rated(
    show_id VARCHAR(127) NOT NULL,
    rating_id INT NOT NULL,

    PRIMARY KEY (show_id, rating_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (rating_id) REFERENCES rating(rating_id)
);
            """)
cur.execute(""" CREATE TABLE IF NOT EXISTS filmed_in(

    show_id VARCHAR(127) NOT NULL,
    country_id INT NOT NULL,

    PRIMARY KEY (show_id, country_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);
            """)
cur.execute(""" CREATE TABLE IF NOT EXISTS directed_by(
    show_id VARCHAR(127) NOT NULL,
    person_id INT NOT NULL,

    PRIMARY KEY (show_id, person_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);          """)

cur.execute(""" CREATE TABLE IF NOT EXISTS acted_in(
    show_id VARCHAR(127) NOT NULL,
    person_id INT NOT NULL,

    PRIMARY KEY (show_id, person_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);
            """)
cur.execute(""" CREATE TABLE IF NOT EXISTS genre(
    genre_name VARCHAR(255) NOT NULL,
    genre_id INT NOT NULL,

    PRIMARY KEY (genre_id)

);
            """)
cur.execute(""" CREATE TABLE IF NOT EXISTS genresof(
    show_id VARCHAR(127) NOT NULL,
    genre_id INT NOT NULL,

    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);
            """)


person = "person.csv"

with open(person, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        id = row[0]
        firstname = row[1]
        lastname = row[2]
        cur.execute(""" INSERT INTO person (person_id,firstname,lastname) VALUES (%s,%s,%s)""",(id,firstname,lastname))
f.close()

country = "country.csv"

with open(country, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        id = row[1]
        cur.execute(""" INSERT INTO country (country_name,country_id) VALUES (%s,%s)""",(name,id))
f.close()

rating = "rating.csv"

with open(rating, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        id = row[1]
        cur.execute(""" INSERT INTO rating (rating_name,rating_id) VALUES (%s,%s)""",(name,id))
f.close()

show = "show.csv"

with open(show, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        id = row[0]
        title = row[1]
        description = row[2]
        duration = row[3]
        type_show = row[4]
        release_date = row[5]
        date_added = row[6]
        cur.execute(""" INSERT INTO show (show_id,title,description_film,duration,type_show,release_date,date_added) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(id,title,description,duration,type_show,release_date,date_added))
f.close()

rated = "rated.csv"

with open(rated, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        show_id = row[0]
        rating_id = row[1]
        cur.execute(""" INSERT INTO rated (show_id,rating_id) VALUES (%s,%s)""",(show_id,rating_id))
f.close()

filmed_in = "produced.csv"

with open(filmed_in, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        show_id = row[0]
        country_id = row[1]
        cur.execute(""" INSERT INTO filmed_in (show_id,country_id) VALUES (%s,%s)""",(show_id,country_id))
f.close()

directed_by = "director.csv"

with open(directed_by, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        show_id = row[0]
        person_id = row[1]
        cur.execute(""" INSERT INTO directed_by (show_id,person_id) VALUES (%s,%s)""",(show_id,person_id))
f.close()

acted_in = "actor.csv"

with open(acted_in, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        show_id = row[0]
        person_id = row[1]
        cur.execute(""" INSERT INTO acted_in (show_id,person_id) VALUES (%s,%s)""",(show_id,person_id))
f.close()

genre = "genre.csv"

with open(genre, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        id = row[1]
        cur.execute(""" INSERT INTO genre (genre_name,genre_id) VALUES (%s,%s)""",(name,id))
f.close()

genresof = "belong.csv"

with open(genresof, "r", encoding="utf8") as f :
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        show_id = row[0]
        genre_id = row[1]
        cur.execute(""" INSERT INTO genresof (show_id,genre_id) VALUES (%s,%s)""",(show_id,genre_id))
f.close()


connect.commit()


cur.close()
connect.close()