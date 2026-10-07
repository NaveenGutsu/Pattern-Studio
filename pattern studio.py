def draw_right_triangle(n):
    """Draws a stair-step pyramid."""
    for row in range(1, n + 1):
        # In row 1, print 1 star; row 2 prints 2 stars, etc.
        print("* " * row)


def draw_diamond(n):
    """Draws a shiny jewel pattern."""
    # 1. Top half (expanding)
    for row in range(1, n + 1):
        spaces = " " * (n - row)
        stars = "* " * row
        print(spaces + stars)

    # 2. Bottom half (shrinking)
    for row in range(n - 1, 0, -1):
        spaces = " " * (n - row)
        stars = "* " * row
        print(spaces + stars)


def draw_number_ladder(n):
    """Prints a counting number staircase."""
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()  # Jumps to the next line


def draw_hollow_box(n):
    """Draws a picture frame."""
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            # If we are on any of the outer borders, place a star
            if row == 1 or row == n or col == 1 or col == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")  # Empty air inside
        print()


def main():
    print("=================================")
    print("  WELCOME TO PATTERN STUDIO!     ")
    print("=================================")
    print("1. Staircase Triangle")
    print("2. Diamond Gem")
    print("3. Number Ladder")
    print("4. Hollow Picture Frame")
    print("5. Exit")

    while True:
        choice = input("\nChoose a shape (1-5): ")

        if choice == "5":
            print("Thanks for playing! Keep building!")
            break

        if choice in ["1", "2", "3", "4"]:
            size = int(input("How big should it be? (Try 5 to 10): "))
            print("\nGenerating...\n")

            if choice == "1":
                draw_right_triangle(size)
            elif choice == "2":
                draw_diamond(size)
            elif choice == "3":
                draw_number_ladder(size)
            elif choice == "4":
                draw_hollow_box(size)
        else:
            print("Oops! Pick a number between 1 and 5.")


if __name__ == "__main__":
    main()
