import os
import csv
from us_state_abbrev import state_abbrev


#Functions

#separate first and last names
def separate_name(nm):
    return nm.split(" ")

#reformat date from YYYY-MM-DD to MM/DD/YYYY
def format_date(dt):
    #split delimited by -
    new_date = dt.split("-")
    new_DOB = new_date[1] + "/" + new_date[2] + "/" + new_date[0]
    return new_DOB

#reformat SSN from nnn-nn-nnnn to ***-**-nnnn
def format_SSN(ssn):
    # split delimited by -
    new_ssn = ssn.split("-")
    return "***-**-" + new_ssn[2]


#run this for files ending in _1 and _2
for suffix in range(1,3):
    file_name = "employee_data" + str(suffix) + ".csv"
    #print(file_name)

    bossCSV = os.path.join('../Resources',file_name)


    #create lists for each type of data that will be stored in the output file
    emp_id = []
    first = []
    last = []
    DOB_new = []
    SSN = []
    State = []


    # open the file and read it
    # Read in the CSV file
    with open(bossCSV, 'r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')

        # skip the title row
        next(csvreader, None)

        # Loop through the data
        for row in csvreader:

            #store the data from the row (Emp ID, Name, DOB, SSN, State) in output lists or local variables
            emp_id.append(row[0])

            #print(emp_id)

            full_name = row[1]
            DOB = row[2]
            SSN_input = row[3]
            State_long = row[4]


            #separate the name into first and last name
            new_name = separate_name(full_name)

            #print(new_name[0])
            #print(new_name[1])

            #store in output lists
            first.append(new_name[0])
            last.append(new_name[1])

            #reformat DOB from yyyy-mm-dd to DD/MM/YYYY and store in output list

            DOB_new.append(format_date(DOB))
            #DOB_new.append(DOB)

            # hide first 5 numbers of SSN using "*"
            SSN.append(format_SSN(SSN_input))

            # convert state to 2-letter abbreviation
            State.append(state_abbrev.get(State_long))


        #zip together the individual lists
        new_data = zip(emp_id, first, last, DOB_new, SSN, State)

        output_path = os.path.join('../Resources', 'updated_' + file_name)
        # Open the file using "write" mode. Specify the variable to hold the contents
        with open(output_path, 'w', newline='') as csvfile:
            # Initialize csv.writer
            csvwriter = csv.writer(csvfile, delimiter=',')
            # Write the first row (column headers)
            csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

            for i in new_data:
                csvwriter.writerow(i)
