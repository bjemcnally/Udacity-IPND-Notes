import fresh_tomatoes
import media # refers to media.py file

"""toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")""" # specifies Movie class within media file                    
# print(toy_story.storyline)

"""avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")"""

imitation_game = media.Movie(
    "The Imitation Game",
    "The true enigma was the man who cracked the code",
    "http://cdn1.thr.com/sites/default/files/imagecache/portrait_300x450/2014/09/the_imitation_game_a_p.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
)

# print(avatar.storyline)
# avatar.show_trailer()

the_rock = media.Movie(
    "The Rock",
    "A mild-mannered chemist and an ex-con must lead the counterstrike when a rogue group of military men, led by a renegade general, threaten a nerve gas attack from Alcatraz against San Francisco.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/82/The_Rock_%28movie%29.jpg/220px-The_Rock_%28movie%29.jpg",
    "https://www.youtube.com/watch?v=313n0wga2xo")
# print(the_rock.storyline)

sense_and_sensibility = media.Movie(
    "Sense and Sensibility",
    "Lose your heart and come to your senses.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Sense_and_sensibility.jpg/215px-Sense_and_sensibility.jpg",
    "https://www.youtube.com/watch?v=Q1rb_c_t1-s")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=niD-jahFURU")

playing_by_heart = media.Movie(
    "Playing by Heart",
    "If romance is a mystery, there's only one way to figure it out.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Playing_by_heart.jpg/220px-Playing_by_heart.jpg",
    "https://www.youtube.com/watch?v=DppPtpEbFag")

the_holiday = media.Movie(
    "The Holiday",
    "Two women troubled with guy-problems swap homes in each other's countries, where they each meet a local guy and fall in love.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Theholidayposter.jpg/220px-Theholidayposter.jpg",
    "https://www.youtube.com/watch?v=2py-VG-UHhI")

movies = [imitation_game, the_rock, sense_and_sensibility, ratatouille, playing_by_heart, the_holiday]
# print(media.Movie.VALID_RATINGS)
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)