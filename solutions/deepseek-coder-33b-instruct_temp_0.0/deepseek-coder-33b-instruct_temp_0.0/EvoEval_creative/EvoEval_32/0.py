def playlist_shuffle(playlist: list, seed: int):
    """Return a new playlist order based on a numerical seed.

    Given a list of song titles (strings) as 'playlist' and an odd integer 'seed',
    implement an algorithm to shuffle the playlist to create a new order.
    The same seed should always produce the same shuffled playlist.

    The shuffling algorithm should use the seed to produce a series of swaps in the sorted list.
    To produce the series, start at index 0 and swap with the element
    at the index `seed % playlist_length`. It's important to note that if a song title contains the word "Rock", it should remain unmoved during the swapping process (the swap operation will be skipped). For the next index, update the
    seed using the formula: seed = (seed * 16807) % 2147483647. Continue this process
    from the next index until the end of the list. Note that the seed will be updated for every index (swapped or not).


    >>> playlist_shuffle(["One More Time", "Around the World", "Harder Better Faster Stronger", "Technologic", "Robot Rock"], 7)
    ['Harder Better Faster Stronger', 'One More Time', 'Technologic', 'Around the World', 'Robot Rock']
    >>> playlist_shuffle(["Song 2", "Parklife", "Country House", "Song 2", "Girls & Boys"], 3)
    ['Song 2', 'Parklife', 'Girls & Boys', 'Song 2', 'Country House']
    """
    playlist_length = len(playlist)
    for i in range(playlist_length):
        if 'Rock' not in playlist[i]:
            swap_index = seed % playlist_length
            (playlist[i], playlist[swap_index]) = (playlist[swap_index], playlist[i])
        seed = seed * 16807 % 2147483647
    return playlist