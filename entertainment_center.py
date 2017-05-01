import fresh_tomatoes
import media



fight_club = media.Movie("fight club", "A story of a underground fight club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=J8FRBYOFu2w")


training_day = media.Movie("training day", "A story of a corrupt cop",
                           "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
                           "https://www.youtube.com/watch?v=DXPJqRtkDP0")
                             
Schindlers_List= media.Movie("Schindler's List", "It is based on the novel Schindler's Ark by Australian novelist Thomas Keneally",
                             "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg",
                             "https://www.youtube.com/watch?v=_cH8w0Cl_-k")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

Goodfellas = media.Top_5("Goodfellas", "1980 gangsters",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y", "Number 1")

interstellar = media.Top_5("Interstellar", "exploring new habitable planet",
                         "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                         "https://www.youtube.com/watch?v=0vxOhd4qlnA", "Number 2")

inception = media.Top_5("Inception", "The implantation of another person's idea into a target's subconscious",
                         "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                         "https://www.youtube.com/watch?v=66TuSJo4dZM", "Number 3")

psycho = media.Top_5("Psycho", "A Phoenix secretary embezzles $40,000, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b9/Psycho_%281960%29.jpg",
                         "https://www.youtube.com/watch?v=NG3-GlvKPcg", "Number 4")

Requiem_for_a_Dream = media.Top_5("Requiem for a Dream", "The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
                         "https://upload.wikimedia.org/wikipedia/en/9/92/Requiem_for_a_dream.jpg",
                         "https://www.youtube.com/watch?v=jzk-lmU4KZ4", "Number 5")


movies = [ Goodfellas, interstellar, inception, psycho, Requiem_for_a_Dream, training_day, Schindlers_List, fight_club, midnight_in_paris, ]
fresh_tomatoes.open_movies_page(movies)



#print(media.Movie.__doc__)


