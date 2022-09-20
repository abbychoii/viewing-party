# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if None in [title, genre, rating]: 
        return None
    movies["title"] = title
    movies["genre"] = genre
    movies["rating"] = rating
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if len(ratings) >= 1:
        avg_ratings = sum(ratings)/len(ratings)
        return avg_ratings
    return 0.0

def get_most_watched_genre(user_data):
    genres = []
    genre_most_count = 0
    most_common_genre = None

    for movie in user_data["watched"]:
        genres.append(movie["genre"])
        for genre in genres:
            if genres.count(genre) > genre_most_count:
                genre_most_count = genres.count(genre)
                most_common_genre = genre    
    
    return most_common_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# # -----------------------------------------

def get_common_watched(user_data):
    friends_data = user_data["friends"]
    common_watched = []

    for movie in user_data["watched"]:
        for friend in friends_data:
            for friend_movie in friend["watched"]:
                if movie["title"] == friend_movie["title"]:
                    common_watched.append(movie)
    return common_watched

def get_unique_watched(user_data):
    # friends data is a list of dictionaries with 
    # duplicate_watched = [title for movie in user_data["watched"] for title in movie]
    unique_watched = []
    common_watched = get_common_watched(user_data)

    for movie in user_data["watched"]:
        if movie not in common_watched and movie not in unique_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_data = user_data["friends"]
    common_watched = get_common_watched(user_data)
    unique_watched = []
    
    for friend in friends_data:
        for movie in friend["watched"]:
            if movie not in common_watched and movie not in unique_watched:
                unique_watched.append(movie)
    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_subscriptions = user_data["subscriptions"]
    friends_movies = get_friends_unique_watched(user_data)
    movie_recs = []
    
    for movie in friends_movies: 
        if movie["host"] in user_subscriptions:
            movie_recs.append(movie)
    
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    movie_recs_by_genre = []
    friends_movies = get_friends_unique_watched(user_data)
    user_genre = get_most_watched_genre(user_data)
    for movie in friends_movies:
        if movie["genre"] == user_genre: 
            movie_recs_by_genre.append(movie)
    return movie_recs_by_genre


def get_rec_from_favorites(user_data):
    user_unique = get_unique_watched(user_data)
    rec_from_favorites = []
    for user_unique_movie in user_unique:
        for fav_movie in user_data["favorites"]:
            if user_unique_movie["title"] == fav_movie["title"]:
                rec_from_favorites.append(user_unique_movie)
    return rec_from_favorites