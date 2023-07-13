import smtplib as smtp

my_email = "kaes100day@gmail.com"
password = "jxhztihhykavxxbz"
second_mail = "kamil.sobania.97@gmail.com"

with smtp.SMTP("smtp.gmail.com") as connection_gmail:
    connection_gmail.starttls()
    connection_gmail.login(user=my_email, password=password)
    connection_gmail.sendmail(from_addr=my_email, to_addrs=second_mail,
                              msg="Subject:Hello\n\n"
                                  "This is body of my email")
