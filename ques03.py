def count_favourite_singers(songs):
    # Dictionary to store the count of songs for each singer
    singer_counts = {}

    # Count the number of songs for each singer
    for singer in songs:
        if singer in singer_counts:
            singer_counts[singer] += 1
        else:
            singer_counts[singer] = 1

    # Find the maximum number of songs any singer has
    max_songs = max(singer_counts.values())

    # Count the number of singers with the maximum number of songs
    favourite_singers_count = sum(1 for count in singer_counts.values() if count == max_songs)

    return favourite_singers_count

# Example usage
playlist = [1, 2, 3, 1, 2, 1, 4, 2, 2]  # Replace this with the actual playlist
num_favourite_singers = count_favourite_singers(playlist)
print("Number of Favourite Singers:", num_favourite_singers)
