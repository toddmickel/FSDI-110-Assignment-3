"""
Audio Manager
Author: Todd Mickel
Functionality: 
    - Register Albums
    - Register Songs
    - Display Catalog
"""

# Imports
from display import print_menu, clear, print_header
from album import Album
from song import Song
import pickle
import datetime

# Globals
catalog = []

# Functions


def serialize_data():
    try:
        writer = open('songManager.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print(" ** Data Saved!")

    except:
        print("** Error: Data was not saved!")


def deserialize_data():
    try:
        reader = open('songManager.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for item in temp_list:
            catalog.append(item)

        print(f"** Loaded {len(catalog)} albums and {count_songs()} songs!")

    except:
        print("** Error: No data was loaded")


def register_album():
    valid = False
    print_header("Register Album")
    albumTitle = input("What's the title of the album? ")
    genre = input("In which genre does this album belong? ")
    artistName = input("Which artist published " + albumTitle + "? ")
    while valid == False:
        try:
            release_year = int(input("In what year was this album released? "))
            if release_year < 1889 or release_year > datetime.datetime.now().year:
                print(f"Invalid year.  Try again!")
                continue
        except:
            print("\nEnter the year as a 4-digit integer.\n")
        else:
            valid = True
    valid = False
    while valid == False:
        try:
            price = float(input("How much does this album cost? "))
        except:
            print("\nEnter the price as a mixed number (x.xx).\n")
        else:
            valid = True

    id = 1
    if len(catalog) > 0:
        id = catalog[-1].id + 1

    album = Album(id, albumTitle, genre, artistName, price, release_year)
    print(album)

    catalog.append(album)
    print("\nAlbum saved!")


def print_catalog(show_songs):
    print_header("Your current catalog")
    for album in catalog:
        print(album)

    """
    print the catalog
    user picks an album 
    print the songs inside that album
    """
    if show_songs:
        print("-" * 30)
        try:
            album_id = int(
                input("Select album ID to see its songs, or [0] to close: "))

            if album_id == 0:
                return

            print("-" * 30)
            found = False
            for album in catalog:
                if album.id == album_id:
                    found = True
                    for song in album.songs:
                        print(song)

                    return album

            if not found:
                print("**Error:  Invalid ID!")

        except:
            print("Invalid entry")


def register_song():
    print_catalog(False)
    album_id = int(input("Select album ID: "))

    found = False
    for album in catalog:
        if album.id == album_id:
            found = True
            print_header("Register a Song to " + album.title)
            track_num = input("What's the track number for this song? ")
            song_title = input("What's the name of the song? ")
            length_secs = input("What's the length of the song in seconds? ")
            id = 1
            if len(album.songs) > 0:
                id = album.songs[-1].id + 1
            song = Song(id, track_num, song_title, length_secs)
            album.songs.append(song)
            print(song)

    if not found:
        print("**Error:  Invalid ID, try again!")


def count_songs():
    song_count = 0

    for album in catalog:
        for songs in album.songs:
            song_count += 1

    return song_count


def total_cost():
    catalog_cost = 0.00
    for album in catalog:
        catalog_cost += album.price

    formatted_cost = "${:,.2f}".format(catalog_cost)
    print(f"Total cost of all albums is {formatted_cost}")


def delete_album():
    album = print_catalog(False)
    print("-" * 30)
    album_id = int(input("Select Album ID: "))

    found = False
    for album in catalog:
        if album.id == album_id:
            found = True
            if len(album.songs) == 0:
                print(f"Deleting album {album.title}")
                catalog.remove(album)
                return True
            else:
                print(
                    f"Cannot remove {album.title}. All songs must first be deleted")
                return False

    if not found:
        print("Error.  Album could not be found.")
        return False


def delete_song():
    """
    - print catalog
    - print songs
    - choose song
    - validate song id
    - delete song
    """
    album = print_catalog(True)
    print("-" * 30)
    try:
        song_id = int(input("Select Song ID: "))

        found = False
        for song in album.songs:
            if song.id == song_id:
                found = True
                print(f"Removing {song.song_title}")
                album.songs.remove(song)
                return True

        if not found:
            print("** Error, song not found")
            return False

    except:
        print("Error.  Did you enter a valid Song ID?")


def most_expensive():
    if len(catalog) == 0:
        print("There are no albums in your catalog!")
        return

    result = 0
    for album in catalog:
        if album.price > result:
            result = album.price
            album_title = album.title

    formatted_result = "${:,.2f}".format(result)
    print(
        f"The most expensive album is {album_title}, which costs {formatted_result}")


def unique_genre():
    genres = set()
    for album in catalog:
        genres.add(album.genre)

    print(f"Unique genres in your catalog: \n{genres}")

    # Instructions


deserialize_data()
input("\nPress Enter to continue...")
option = ''
while option.upper() != 'Q':
    clear()
    print_menu()
    option = input("\nPlease select an option: ")

    if option.upper() == "Q":
        break

    elif option == "1":
        register_album()
        serialize_data()

    elif option == "2":
        register_song()
        serialize_data()

    elif option == "3":
        print_catalog(True)

    elif option == "5":
        print(f"There are {count_songs()} songs in the catalog")

    elif option == "6":
        total_cost()

    elif option == "7":
        success = delete_album()
        if success:
            serialize_data()

    elif option == "8":
        success = delete_song()
        if success:
            serialize_data()

    elif option == "9":
        most_expensive()

    elif option == "10":
        unique_genre()

    input("\nPress Enter to continue...")

print("\nSee ya!")
