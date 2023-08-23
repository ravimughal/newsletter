import csv

def get_emails_from_csv(csv_filename):
    emails = []

    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)

        for row in csvreader:
            if row: 
                email = row[0]
                emails.append(email)

    return emails
