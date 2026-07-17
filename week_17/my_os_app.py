import os
import sys


def clear_screen():
    # Clears the terminal screen depending on the OS
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    print("=" * 30)
    print("      OS PYTHON UTILITY        ")
    print("=" * 30)
    print(f"Current Directory: {os.getcwd()}")
    print("-" * 30)
    print("1. List files in current folder")
    print("2. Create a new folder")
    print("3. Check if a specific file exists")
    print("4. Exit")
    print("=" * 30)


def list_files():
    print("\n--- Files and Folders ---")
    files = os.listdir(".")
    if not files:
        print("(Folder is empty)")
    for file in files:
        print(f" - {file}")
    input("\nPress Enter to return to menu...")


def create_folder():
    folder_name = input("\nEnter the name of the new folder: ").strip()
    if folder_name:
        try:
            os.mkdir(folder_name)
            print(f"Success: Folder '{folder_name}' created!")
        except FileExistsError:
            print("Error: That folder already exists.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid name.")
    input("\nPress Enter to return to menu...")


def check_file():
    file_name = input("\nEnter the filename to look for (e.g., app.py): ").strip()
    if os.path.exists(file_name):
        print(f"Yes! '{file_name}' exists in this directory.")
    else:
        print(f"No, '{file_name}' could not be found.")
    input("\nPress Enter to return to menu...")


def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            list_files()
        elif choice == "2":
            create_folder()
        elif choice == "3":
            check_file()
        elif choice == "4":
            print("\nGoodbye!")
            sys.exit()
        else:
            input("\nInvalid choice. Press Enter to try again...")


if __name__ == "__main__":
    main()