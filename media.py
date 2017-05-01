import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Top_5(Movie):
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube,
                 top_5_favorite):
        print("Top 5")
        Movie.__init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)
        self.top_5_favorite = top_5_favorite

    def show_info(self):
        print("Movie Title - "+self.title)
        print("Storyline - " +self.storyline)
        print("Top 5 Favorite - "+self.top_5_favorite)

   

        

