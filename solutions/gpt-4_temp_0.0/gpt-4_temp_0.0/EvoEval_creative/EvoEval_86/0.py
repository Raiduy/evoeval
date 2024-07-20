def sort_movies_by_ratings_and_release_date(movies_dict):
    """
    Every movie lover has a favorite genre and likes to watch movies based on their ratings and release year. 
    Given a dictionary where each key-value pair represents a movie, develop a function that sorts these movies 
    according to ratings (from high to low) and if the ratings are same, then sort according to the release year 
    (from new to old). The function should return the sorted list of movie names.

    The dictionary has the following format:
    { "movie_name": [rating, release_year] }

    Ratings are from 1 to 10, and release years are four digit numbers.

    Examples:
    movies_dict = {"Inception": [8.8, 2010], "The Dark Knight": [9, 2008], 
                   "Interstellar": [8.6, 2014], "The Dark Knight Rises": [8.4, 2012]}
    sort_movies_by_ratings_and_release_date(movies_dict) ➞ ["The Dark Knight", "Inception", "Interstellar",
                                                             "The Dark Knight Rises"]
    
    movies_dict = {"Toy Story": [8.3, 1995], "Toy Story 2": [7.9, 1999], 
                   "Toy Story 3": [8.3, 2010], "Toy Story 4": [7.8, 2019]}
    sort_movies_by_ratings_and_release_date(movies_dict) ➞ ["Toy Story 3", "Toy Story", 
                                                             "Toy Story 2", "Toy Story 4"]
    """
    sorted_movies = sorted(movies_dict.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    return [movie[0] for movie in sorted_movies]