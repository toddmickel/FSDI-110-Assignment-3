import os


def print_menu():
    print("-" * 43)
    print("--" + " " * 39 + "--")
    print("--        *** Audio Manager ***          --")
    print("--" + " " * 39 + "--")
    print("-" * 43)
    print("--" + " " * 39 + "--")
    print("-- [1] Register Album                    --")
    print("-- [2] Register Song                     --")
    print("-- [3] Print Catalog                     --")

    print("-- [5] Count all the songs in the system --")
    print("-- [6] Total $ in the catalog            --")
    # only delete album if there are no songs in it
    print("-- [7] Delete Album                      --")
    print("-- [8] Delete Song                       --")
    print("-- [9] Print the most expensive album    --")
    # Use whichever doesn't allow duplicated (tuple, dictionary, set, etc)
    print("-- [10] Print the unique genres          --")
    print("--" + " " * 39 + "--")
    print("-- [Q] Quit                              --")
    print("--" + " " * 39 + "--")
    print("-" * 43)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(text):
    clear()
    print("-" * 30)
    print("  " + text)
    print("-" * 30)
