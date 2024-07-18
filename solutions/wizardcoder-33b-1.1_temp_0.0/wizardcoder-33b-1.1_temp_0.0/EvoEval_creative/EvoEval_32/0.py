def playlist_shuffle(playlist: list, seed: int):
    playlist_length = len(playlist)
    new_playlist = playlist.copy()
    skip_indices = [i for (i, song) in enumerate(playlist) if 'Rock' in song]
    for i in range(playlist_length):
        if i not in skip_indices:
            swap_index = seed % playlist_length
            (new_playlist[i], new_playlist[swap_index]) = (new_playlist[swap_index], new_playlist[i])
            seed = seed * 16807 % 2147483647
    return new_playlist