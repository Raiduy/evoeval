def playlist_shuffle(playlist: list, seed: int):
    playlist_length = len(playlist)
    playlist_copy = playlist.copy()
    playlist_copy.sort()
    for i in range(playlist_length):
        seed = seed * 16807 % 2147483647
        j = seed % playlist_length
        if 'Rock' not in playlist_copy[i]:
            (playlist_copy[i], playlist_copy[j]) = (playlist_copy[j], playlist_copy[i])
    return playlist_copy