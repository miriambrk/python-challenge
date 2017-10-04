import os
import csv

#run this for files ending in _1 and _2

for suffix in range(1,3):
    file_name = "budget_data_" + str(suffix) + ".csv"
    #print(file_name)

    budgetCSV = os.path.join('../Resources',file_name)

    total_revenue = 0.0
    total_months = 0
    avg_rev_change = 0.0
    greatest_increase = 0.0
    greatest_decrease = 0.0
    current_month_rev = 0.0
    last_month_rev = 0.0

    #list to keep track of change in revenue
    change_in_rev = []
    month_change_in_rev = []

    # Read in the CSV file
    with open(budgetCSV, 'r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip the title row
        next(csvreader, None)

        # Loop through the data
        for row in csvreader:

            #row[0] is date; row[1] is revenue
            total_months = total_months + 1
            current_month_rev = float(row[1])
            total_revenue = total_revenue + current_month_rev



            #compute revenue change and store in list; don't do for first record
            if total_months > 1:
                delta = current_month_rev - last_month_rev
                change_in_rev.append(delta)
                month_change_in_rev.append(row[0])
                #print(change_in_rev)

            last_month_rev = current_month_rev

        #compute the average revenue change by looping through the list
        total_change = 0.0
        for i in range(len(change_in_rev)):
            total_change = total_change + change_in_rev[i]

            if change_in_rev[i] > 0 and change_in_rev[i] > greatest_increase:
                greatest_increase = change_in_rev[i]
                greatest_month_inc = month_change_in_rev[i]
            if change_in_rev[i] < 0 and change_in_rev[i] < greatest_decrease:
                greatest_decrease = change_in_rev[i]
                greatest_month_dec = month_change_in_rev[i]

        avg_rev_change = total_change / len(change_in_rev)

        print("Financial Analysis of " + file_name)
        print("---------------------------------------------")

        print("Total Months: " + str(total_months))
        print("Total Revenue: $" + str(total_revenue))

        print("Average Revenue Change: $" + str(round(avg_rev_change,2)))

        print("Greatest Increase in Revenue:" + greatest_month_inc + " ($" + str(greatest_increase) + ")")

        print("Greatest Decrease in Revenue: " + greatest_month_dec + " ($" + str(greatest_decrease) + ")\n\n")




    #write the output to a text file
    output_file = os.path.join('../Resources', 'FinAnal_' + str(suffix) + ".txt")

    with open(output_file, 'w') as textfile:

        textfile.write("Financial Analysis\n")
        textfile.write("---------------------------------------------\n\n")

        textfile.write("Total Months: " + str(total_months)+ "\n")

        textfile.write("Total Revenue: $" + str(total_revenue) + "\n")

        textfile.write("Average Revenue Change: $" + str(round(avg_rev_change, 2))+ "\n")

        textfile.write("Greatest Increase in Revenue:" + greatest_month_inc + " ($" + str(greatest_increase) + ")\n")

        textfile.write("Greatest Decrease in Revenue: " + greatest_month_dec + " ($" + str(greatest_decrease) + ")\n")








