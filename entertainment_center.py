import fresh_tomatoes

"""
The import "fresh_tomatoes.py" help generate a website that displays these movies, it provides a starter code repository 
that contains a Python module. 
"""

import media

"""
The media file contain the class "movie", which contain the constructor, and within
the constructor, the instances variables structured the self, storyline, poster image, and trailer URL.
"""

fight_club = media.Movie("Fight Club", "A story of a underground fight club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=J8FRBYOFu2w")

training_day = media.Movie("Training day", "A story of a corrupt cop",
                           "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
                           "https://www.youtube.com/watch?v=DXPJqRtkDP0")
                             
Schindlers_List= media.Movie("Schindler's List", "It is based on the novel Schindler's Ark by Australian novelist Thomas Keneally",
                             "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                             "https://www.youtube.com/watch?v=_cH8w0Cl_-k")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

Goodfellas = media.Movie("Goodfellas", "1980 gangsters",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

interstellar = media.Movie("Interstellar", "exploring new habitable planet",
                         "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                         "https://www.youtube.com/watch?v=0vxOhd4qlnA")

inception = media.Movie("Inception", "The implantation of another person's idea into a target's subconscious",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=66TuSJo4dZM")

psycho = media.Movie("Psycho", "A Phoenix secretary embezzles $40,000, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b9/Psycho_%281960%29.jpg",
                         "https://www.youtube.com/watch?v=NG3-GlvKPcg")

Requiem_for_a_Dream = media.Movie("Requiem for a Dream", "The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
                         "https://upload.wikimedia.org/wikipedia/en/9/92/Requiem_for_a_dream.jpg",
                         "https://www.youtube.com/watch?v=jzk-lmU4KZ4", )

"""
The instances are the names of my 9 favorite movies. The data inside the bracket are structured by
the instances variables that came from media.Movie.show_trailer
(self, storyline, poster image, and trailer URL.) By calling the constructor media.Movie() it instantiate the movie objects.
"""

movies = [ Goodfellas, interstellar, inception, psycho, Requiem_for_a_Dream, training_day, Schindlers_List, fight_club, midnight_in_paris, ]

#This is an array that contain the list of my favorite 9 movies.

fresh_tomatoes.open_movies_page(movies)

"""
The fresh_tomatoes.py module calls the open_movies_page, which is an argument that list and
creates an HTML file which will display 9 of my favorite movies.
This list of movies is what the open_movies_page() function needs as input in order to build the HTML file, 
so I can display your website.
"""

