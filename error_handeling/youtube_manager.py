import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test =  json.load(file)
            return test
 
    except FileNotFoundError:# this is like catch block and FileNotFoundError is error type (like we reade in java in exceptionHandeling)
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*50)
    for index,video in enumerate(videos,start=1):
          print(f"{index}.{video["name"]} Duration: {video['time']}")
    print("\n")
    print("*"*50)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
def update_video(videos):   
    list_all_videos(videos)# 1st we get all list of video so , we call this function
    index = int(input("Enter video index to update: "))
    if 1 <=index <= len(videos):# here we check that index is greater than 0 and index is less than length of videos
        name = (input("Enter video name: "))
        time = (input("Enter video time: "))
        videos[index-1] = {"name": name, "time": time}# to which index to update
        save_data_helper(videos)
    else:
        print("Invalid index")
       
   
    

def delete_video(videos):
    list_all_videos(videos)# 1st we get all list of video so , we call this function
    index = int(input("Enter video index to delete: "))
    if 1 <=index <= len(videos):# here we check that index is greater than 0 and index is less than length of videos
         del videos[index-1] # useing del keyword we delete the videos
         save_data_helper(videos)

def main():# # We define this main function so we can specify that the application starts from here.
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all Youtube videos")# like read
        print("2. Add a new video")# create
        print("3. Update a youtube video")# update
        print("4. Delete a youtube video")# delete
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        # print(videos)
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
