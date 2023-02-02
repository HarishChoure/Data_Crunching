import csv

def read_tsv_file(filename):
    with open(filename,'r') as file:
        rea = csv.reader(file,delimiter='\t')
        result = {}
        for row in rea:
            result[row[0]] = row[1:]
        return result

user_email_hash = read_tsv_file("user_email_hash.1m.tsv")
ip = read_tsv_file("ip_1m.tsv")
plain_email = read_tsv_file('plain_32m.tsv')

with open("output2.tsv", "w") as out_file:
    writer = csv.writer(out_file, delimiter="\t")
    writer.writerow(["Id", "username", "email", "hashed_password","plaintext" "ip"])

    for user_id in user_email_hash:
        user_data = user_email_hash[user_id]
        username = user_data[0]
        email = user_data[1]
        hashed_password = user_data[2]
        if user_id in ip:
            ip_address = ip[user_id][0]
        else:
            ip_address = ""
        if email in plain_email:
            plaintext = plain_email[user_id][0]
        else:
            plaintext = ""

        writer.writerow([user_id, username, email, hashed_password, plaintext,ip_address])

