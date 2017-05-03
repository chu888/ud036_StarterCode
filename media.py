# -*- coding: cp1252 -*-
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        (This is the constructor for the movie class, so I can create instances of movie.
        These movie objects are located in the "entertainment_center.py."
        You’ve given movies their own custom data structure by defining the movie class and
        constructor, and these objects are stored in a list data structure. )
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#The following code is the instance methods, it opens the URL for the movie trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



   

        

