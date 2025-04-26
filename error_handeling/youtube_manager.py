import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test =  json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:# this is like catch block and FileNotFoundError is error type (like we reade in java in exceptionHandeling)
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
          print(f"{index}.")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
def update_video(videos):   
    pass

def delete_video(videos):
    pass

def main():# # We define this main function so we can specify that the application starts from here.
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all Youtube videos")
        print("2. Add a new video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        print(videos)
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")

# To run the main function:
if __name__ == "__main__":# # '__' are called dunders (double underscores)
    main()
