import csv

import os



print(" Welcome to the BBC Viewership Data Analysis \n")



csv_file = "bbc_viewers.csv"



# Check if CSV file exists

if not os.path.exists(csv_file):

    print(f" CSV file '{csv_file}' not found in the folder!")

else:

    # Lists to store data

    shows = []

    viewers = []



    # Read the CSV

    with open(csv_file, "r") as file:

        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:

            shows.append(row[0])

            viewers.append(int(row[1]))



    # Total viewers

    total_viewers = sum(viewers)

    print("Total viewers across all shows:", total_viewers)



    # Most-watched show

    max_viewers = max(viewers)

    index_max = viewers.index(max_viewers)

    print("Most-watched show:", shows[index_max], "with", max_viewers, "viewers")



    # Least-watched show

    min_viewers = min(viewers)

    index_min = viewers.index(min_viewers)

    print("Least-watched show:", shows[index_min], "with", min_viewers, "viewers")



    print("\n Data analysis complete!")