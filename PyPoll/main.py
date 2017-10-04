import os
import csv




#run this for files ending in _1 and _2

#CHANGE THIS TO 1,3 once _1 is available !!!!
for suffix in range(2,3):
    file_name = "election_data_" + str(suffix) + ".csv"
    #print(file_name)

    electionCSV = os.path.join('../Resources',file_name)

    total_votes = 0
    candidates = {} #dictionary will contain candidate name: number of votes
    percent_of_votes = 0.0

    #open the file and read it
    # Read in the CSV file
    with open(electionCSV, 'r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')

        # skip the title row
        next(csvreader, None)

        # Loop through the data
        for row in csvreader:
            #accumulate the total number of votes
            total_votes = total_votes + 1

            candidate = row[2]

            #if existing candidate, add to his/her total votes; otherwise add to candidates dictionary, 1 vote
            if candidate in candidates:
                candidates[candidate] = candidates[candidate] + 1

            else:  #add this candidate with 1 vote
                candidates[candidate] = 1


        #print(candidates)


        #compute results and write to output text file

        output_file = os.path.join('../Resources', 'Poll_Results_' + str(suffix) + ".txt")
        with open(output_file, 'w') as textfile:


            #print to screen
            print("Election Results")
            print("----------------------------------------")
            print("Total Votes: " + str(total_votes))
            print("----------------------------------------")

            #print to file
            textfile.write("Election Results\n")
            textfile.write("---------------------------------------------\n")
            textfile.write("Total Votes: " + str(total_votes) + "\n")
            textfile.write("---------------------------------------------\n")

            winner = ""
            winner_votes = 0
            #loop through dictionary of candidates and print out percent and total votes
            for i in candidates:
                #compute percentage
                candidate_votes = candidates[i]
                percent_of_votes = round(100.0 * candidate_votes/total_votes,2)

                #print and write candidate's vote tally
                print(i + ":\t" + str(percent_of_votes) + "% (" + str(candidate_votes) + ")")
                textfile.write(i + ":\t" + str(percent_of_votes) + "% (" + str(candidate_votes) + ")\n")

                #determine winner
                if candidate_votes > winner_votes:
                    winner_votes = candidate_votes
                    winner = i

            print("----------------------------------------")
            print ("Winner: " + winner)
            print("----------------------------------------")

            textfile.write("---------------------------------------------\n")
            textfile.write("Winner: " + winner + "\n")
            textfile.write("---------------------------------------------\n")



