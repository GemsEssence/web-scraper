import instaloader
import pandas as pd
import csv
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()


insta_users = []
with open("instagram_users.txt") as file:
    for line in file:
        insta_users.append(line.strip())


filename = "instagram_data.csv"
with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    fields = ['Username', 'User ID', 'Number of Posts', 'Followers Count', 'Following Count', 'Bio', 'External URL'] 
    csvwriter.writerow(fields)
    for user in insta_users:
        # Loading a profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, user)
        fields[0] = profile.username
        fields[1] = profile.userid
        fields[2] = profile.mediacount
        fields[3] = profile.followers
        fields[4] = profile.followees
        fields[5] = profile.biography
        fields[6] = profile.external_url

        csvwriter.writerow(fields)


print('Your data has been scraped please check the Data.csv file')