#Console input and outputs


# Main menu
def main_menu():
    print("==================================================")
    print("Select the number of the operation you want to do.")
    print("")
    print("1 - Add Movie")
    print("2 - Categorize Movie")
    print("3 - Rate Movie")
    print("4 - Mark Movie as Watched")
    print("5 - Edit Movie")
    print("6 - Delete Movie")
    print("7 - Display Library")
    print("8 - Search Movies")
    print("9 - Sort Movies")
    print("10 - Random Recommendation")
    print("11 - Genre Suggestions")
    print("12 - Show Unwatched Movies")
    print("")
    print("0 - Exit")
    print("==================================================")

    user_operation = input("What do you want to do?")
    return user_operation
