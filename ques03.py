def count_favourite_singers(songs):
    singer_counts = {}

    for singer in songs:
        if singer in singer_counts:
            singer_counts[singer] += 1
        else:
            singer_counts[singer] = 1

    max_songs = max(singer_counts.values())

    favourite_singers_count = sum(1 for count in singer_counts.values() if count == max_songs)

    return favourite_singers_count

playlist = [1, 2, 3, 1, 2, 1, 4, 2, 2]  
num_favourite_singers = count_favourite_singers(playlist)
print("Number of Favourite Singers:", num_favourite_singers)
