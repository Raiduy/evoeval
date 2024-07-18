def sort_movies_by_ratings_and_release_date(movies_dict):
    sorted_movies = sorted(movies_dict.keys(), key=lambda x: (movies_dict[x][0], movies_dict[x][1]), reverse=True)
    return sorted_movies