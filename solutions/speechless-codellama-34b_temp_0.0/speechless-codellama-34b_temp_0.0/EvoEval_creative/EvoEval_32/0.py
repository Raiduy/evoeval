def playlist_shuffle(playlist: list, seed: int):
    playlist_length = len(playlist)
    for i in range(playlist_length):
        if 'Rock' in playlist[i]:
            continue
        swap_index = seed % playlist_length
        (playlist[i], playlist[swap_index]) = (playlist[swap_index], playlist[i])
        seed = seed * 16807 % 2147483647
    return playlist