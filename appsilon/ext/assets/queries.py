from enum import Enum


class Queries(Enum):
    SELECT_MOVIES_AFTER_2013 = """
        SELECT ?movie ?movieLabel ?imdbId ?director ?directorLabel ?genre ?genreLabel ?publicationYear WHERE {
            ?movie  wdt:P31 wd:Q11424;                           # Instance
                    wdt:P577 ?publicationDate;                   # Publication date
                    wdt:P345 ?imdbId;                            # IMDb ID
                    wdt:P57 ?director.                           # Director
            ?movie  wdt:P136 ?genre.                             # Genre
            BIND(YEAR(?publicationDate) AS ?publicationYear)     # Year of publication

            FILTER (?publicationYear > 2013)
            FILTER (BOUND(?imdbId))

            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }
        LIMIT 100
    """
