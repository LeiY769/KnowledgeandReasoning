

CREATE TABLE IF NOT EXISTS person(
    person_id INT NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NULL,

    PRIMARY KEY (person_id)
);

CREATE TABLE IF NOT EXISTS country(
    country_name VARCHAR(255) NOT NULL,
    country_id INT NOT NULL,
    PRIMARY KEY (country_id)
);

CREATE TABLE IF NOT EXISTS rating(
    rating_name VARCHAR(255) NOT NULL,
    rating_id INT NOT NULL,

    PRIMARY KEY (rating_id)
);

CREATE TABLE IF NOT EXISTS show(
    show_id VARCHAR(127) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description_film VARCHAR(4095) NOT NULL,
    type_show VARCHAR(255) NOT NULL,
    duration INT NOT NULL,
    release_date INT NOT NULL,
    date_added VARCHAR(127)NOT NULL,

    PRIMARY KEY (show_id)
); 

CREATE TABLE IF NOT EXISTS rated(
    show_id VARCHAR(127) NOT NULL,
    rating_id INT NOT NULL,
    PRIMARY KEY (show_id, rating_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (rating_id) REFERENCES rating(rating_id)
);

CREATE TABLE IF NOT EXISTS filmed_in(

    show_id VARCHAR(127) NOT NULL,
    country_id INT NOT NULL,

    PRIMARY KEY (show_id, country_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);

CREATE TABLE IF NOT EXISTS directed_by(
    show_id VARCHAR(127) NOT NULL,
    person_id INT NOT NULL,

    PRIMARY KEY (show_id, person_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);

CREATE TABLE IF NOT EXISTS acted_in(
    show_id VARCHAR(127) NOT NULL,
    person_id INT NOT NULL,

    PRIMARY KEY (show_id, person_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);

CREATE TABLE IF NOT EXISTS genre(
    genre_name VARCHAR(255) NOT NULL,
    genre_id INT NOT NULL,

    PRIMARY KEY (genre_id)

);

CREATE TABLE IF NOT EXISTS genresof(
    show_id VARCHAR(127) NOT NULL,
    genre_id INT NOT NULL,

    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);

