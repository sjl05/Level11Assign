"""
Level #11 Assignment – Video Game Catalog Manager
IS 303 – Hilton
A gaming website has provided a CSV file containing information about video games. The
catalog needs to be reviewed, updated, and prepared for future use. Create a Python program that
reads the provided video_games_raw.csv file and updates the catalog.
Download video_games_raw.csv
Your program should:
• Read the CSV file using Pandas.
• Ask the user for a specific row number to inspect.
• Use .iloc[] to display information about the selected game.
• Ask the user to enter a new status for that game, such as Backlog, Playing, Completed,
or Dropped.
• Use .at[] to update the selected game’s status.
• Add a Recommended column to the panda.
• Set Recommended to Yes for games that meet both of these criteria:
o Rating is at least 8.
o Price is $40 or less.
• Set Recommended to No for all other games.
• Use .query() to display the recommended games.
• Save the updated data to a new file named video_games_cleaned.csv.
The original CSV file should remain unchanged.
The exact games displayed will depend on the information in the provided CSV file.
Your program should demonstrate your understanding of:
• .iloc[] for accessing a row by position
• .at[] for changing one specific value
• .loc[] for changing multiple rows
• .query() for filtering data
• .to_csv() for saving the updated DataFrame
Submit your PUBLIC GitHub link through Canvas.
Sample Session:
VIDEO GAME CATALOG MANAGER
Enter a row number to inspect: 4
Selected Game:
Title: Stardew Valley
Platform: PC
Genre: Simulation
Rating: 8.8
Current Status: Backlog
Enter a new status:
Completed
Recommended Games:
Title Platform Price Rating
0 The Legend of Zelda: Breath of the Wild Switch 39.99 9.5
2 Stardew Valley PC 14.99 8.8
5 Minecraft PC 29.99 9.0
The catalog has been updated.
Saved as video_games_cleaned.csv.
"""
#Samuel Lyon
#IS303 Hilton

#imports
import pandas as pd
#global varibles
statuses = ["backlog", "playing", "completed", "dropped"]
#main code
#make a dataframe based off the csv
dfvgr = pd.read_csv("video_games_raw.csv")
print("Video Game Catalog Manager")
print("Enter 'q' to quit and see the recommended games")
while True:
    try:
        #query the user for which row
        print("Enter a row to inspect information about that game, row numbers start at 0.")
        row_num = input("Row: ")
        if row_num == 'q':
            break
        row_num = int(row_num) #This will cause an error if the user doesn't enter a value that can be an integer
        title = dfvgr.iloc[row_num, 0] #This will cause an error if the index does not correspond to a row
        #printing all the information for the selected game
        print("")
        print("Selected Game:")
        print(f"Title: {title}")
        print(f"Platform: {dfvgr.iloc[row_num, 1]}")
        print(f"Genre: {dfvgr.iloc[row_num, 2]}")
        print(f"Rating: {dfvgr.iloc[row_num, 5]}")
        print(f"Current Status: {dfvgr.iloc[row_num, 8]}")
        #begins a loop to tell ask the user if they want to modify the status for the game
        modify_true = True
        while modify_true:
            modify_yn = input("Do you want to modify the status of this game? ").strip().lower()
            if modify_yn == "yes":
                status_changed = False
                #begins a loop to ask the user what status they want to change it to validates based on a list
                while status_changed == False:
                    print("")
                    print("What do you want to change the status to?\nExamples: Backlog, Playing, Completed, Dropped")
                    status = input("New Status: ").strip().lower()
                    if status in statuses:
                        previous_status = dfvgr.iloc[row_num, 8]
                        #saves the new status to the dataframe
                        dfvgr.at[row_num,"Status"] = status.title()
                        print(f"Status has been updated from {previous_status} to {dfvgr.iloc[row_num, 8]}")
                        status_changed = True
                        modify_true = False
                    elif status not in statuses:
                        print("Please enter one of the above statuses")
            elif modify_yn == "no":
                print("")
                print("Okay, we won't modify the status of this game.")
                modify_true = False
            else:
                print("Please enter whether or not you want to modify the status of the game.")
            print("")
    except IndexError: 
        print("We don't have information for that row")
    except ValueError:
        print("We don't recognize that input, please try again.")
    except: #catching all other errors
        print("Something went wrong, please try again.")

#make a copy of the dataframe
dfvgc = dfvgr.copy()
dfvgc["Recommended"] = "No" #set all the rows in the new column "Recommend" to "No"
dfvgc.loc[(dfvgc["Rating"] >= 8) & (dfvgc["Price"] <= 40.0), ["Recommended"]] = "Yes" #set the rows that meet the criteria to Yes
print(dfvgc.query("Recommended == 'Yes'")[["Title", "Platform", "Price", "Rating"]]) #printing the specific output

#puts the finished csv in a file
dfvgc.to_csv("video_games_cleaned.csv", index=False)
#let the user know what has been done
print("The catalog has been updated") 
print("The new catalog has been saved to video_games_cleaned.csv")
