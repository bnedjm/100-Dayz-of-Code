from smtplib import *
from datetime import *

# email_sender = "tester.py99@gmail.com"
# password = "Li*t0AQGEJ7u("
# app_password = "juslsfmekfbyvpnn"
#
# # email_receiver = "boukhedenna.nedjm@gmail.com"
# email_receiver = "chihanikarim07@gmail.com"
#
# with SMTP("smtp.gmail.com") as connect:
#     connect.starttls()
#     connect.login(user=email_sender, password=app_password)
#     connect.sendmail(
#         from_addr=email_sender,
#         to_addrs=email_receiver,
#         msg="Subject: SMTP .py Test Email\n\n"
#             "This is an automated test Email."
#     )

real_time = datetime.now()

year = real_time.year
month = real_time.month
day = real_time.day
hour_ = real_time.hour
min_ = real_time.minute
sec_ = real_time.second

print(real_time)

date_of_birth = datetime(year=1898, month=12, day=12)

print(date_of_birth)
 
