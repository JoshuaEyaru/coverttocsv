import csv

def convert_log_to_csv(input_logfile_path, output_csvfile_path):
    #using with forto  with context management (cleanup after it's no longer needed)

    with open(input_logfile_path, 'r') as log_file, open(output_csvfile_path, 'w', newline='') as csv_file:

        #at this point we read the log file
        lines = log_file.readlines()

        #let's assume the header is the first line and extract it from the log file
        header = lines[0].strip().split()

        #Extract the data rows from the log file
        data_rows = [line.strip().split() for line in lines[1:]]

        #We then write the data to the csv file
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(data_rows)

    print(f"Conversion complete. CSV file saved at: {output_csvfile_path}")

#example test case
input_logfile_path = '/Users/joshuaeyaru/Documents/ARGONNE/Project/convert_to_csv/coverttocsv/inputlogfile/sedov.log'
output_csvfile_path = '/Users/joshuaeyaru/Documents/ARGONNE/Project/convert_to_csv/coverttocsv/outputcsv/sedovoutput.csv'

convert_log_to_csv(input_logfile_path, output_csvfile_path)