import smtplib
import yaml
with open ("abc.yaml","r") as st:
    for x in yaml.safe_load_all(st):
        email =x["user"]["email"]
        pws = x["user"]["password"]
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, pws)
server.sendmail(email,"mhmdjwadsrdarabady01@gmail.com","hi")
server.quit()
#send email with python 