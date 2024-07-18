def sort_movies_by_ratings_and_release_date(movies_dict):
    sorted_movies = sorted(movies_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))
    return [movie[0] for movie in sorted_movies]