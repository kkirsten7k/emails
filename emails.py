#!/usr/bin/env python3
# coding: utf-8

#Change Google settings at https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Nf0UeZhqZF7oyW-I-mI_wxUCpb0brNbwv4UedSvi1GT-jXMD3N0lWtx53TwZd3qCTBFMWk-rjKX3cpCy70x6KA14nqSA



# In[1]:

print("hello world")

# In[1]:

import time
import numpy as np
import pandas as pd
import smtplib, ssl


# In[2]:


import os
import math
import sys
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# In[3]:



PORT = 465
TEACHER_EMAIL = "kirsten.kulhanek@kippsfcp.org"
TEACHER_PASSWORD = "KIPP3k94KK993"
# CLASS_PERIODS = sys.argv[1:] if not [] else ["1", "2", "5", "6", "7"]
CLASS_PERIODS = ["1", "2", "3", "4", "5", "6", "7"]

# In[3]: 

print(PORT)
print(CLASS_PERIODS)
# print(sys.argv[1:])

# In[4]:


def process_assignments(hw_assignments):
    missing_assignments = []
    for hw_name, hw_val in hw_assignments.items():
        if hw_val == 'missing':
            missing_assignments.append(hw_name)
            
    return missing_assignments


def send_email(s_name, s_email, s_assignments, period):
    ####################################################################################################################
    #Here you can change the messages if you would like.################################################################
    ####################################################################################################################
    _, f_name  = s_name.split(",")

    
    HEADER = f"""Hi{f_name}, <br />
<br />
I just wanted to reach out to you with an update on how you're doing so far, and give you the opportunity to start this cycle with some strong grades. <br />
Late work is docked for being late, however, any missing assignments will be locked in as 0s if they are not completed. <br />
The due date for any missing work this cycle is <b> Monday December 13th </b > but it's best to get your work in as soon as possible.<br />
See below for a plan to follow to turn in the most important assignments in this quarter: <br />
<br />

<h4> THESE ARE YOUR MISSING ASSIGNMENTS (If none are listed, none are missing) </h4>"""
    
    for assignment in s_assignments:
        HEADER += assignment + "<br />"

#INSERT THIS AT END OF EMAIL: I have office hours Thursdays 3-4pm. If you want to come, email me and I can send you the zoom link.  <br />
#       Or here is the
 #         <a href="https://calendly.com/niki-mirzamaani/30min?back=1&month=2020-10">link to Ms. M's office Hours </a>
  #     </p>
   #    <a href="https://docs.google.com/presentation/d/1yzGYJIDHk94Rzga0ZeDekLd6saxpeKx87UdD3Tww9HM/edit?usp=sharing">
  


    GEOMETRY_MESSAGE = f"""<html>
  <head></head>
  <body>
       <p>{HEADER}</p>
       <p>Once you have completed these Exit Tickets, please turn them in to the turn in basket in class. <br />

       </a>
       <p> Reach out to me if you have any questions! YOU GOT THIS! :) <br />
       Best, <br />
       Miss Kulhanek
       </p>
You are always welcome to come in during lunch for help.  <br />
    
       <a href="https://docs.google.com/presentation/d/1-ElwNqR2rKqoOh4A27HIOe6l4-jICJvX7gtSuG46uiA/edit?usp=sharing">
	</p>
       <a href="https://docs.google.com/presentation/d/1-ElwNqR2rKqoOh4A27HIOe6l4-jICJvX7gtSuG46uiA/edit?usp=sharing">
	   Quarter 2 Exit Tickets
	</a>
  </body>
</html>
"""

    AP_CALC_MESSAGE = f"""<html>
  <head></head>
  <body>
       <p>{HEADER}</p>
       <p>Once you have completed these Exit Tickets, please turn them in to the turn in basket in class. <br />
       You are always welcome to come in during lunch for help.  <br />
   
       </p>
       <p> Please reach out to me if you have any questions! YOU GOT THIS! :) <br />
       Best, <br />
       Miss. Kulhanek
       </p>
       <a href="https://docs.google.com/presentation/d/1ZJVeihLH3duq2eJBV_nLwCrQKanGTjW4T5J98BsRWxI/edit?usp=sharing">
           Quarter 2 Exit Tickets
       </a>
  </body>
</html>
"""

    email_content  = {"2": ("<action requested> AP Calculus Support", AP_CALC_MESSAGE),
                      "1": ("<action requested> Geometry Support", GEOMETRY_MESSAGE), 
                      "5": ("<action requested> Geometry Support", GEOMETRY_MESSAGE),
                      "6": ("<action requested> Geometry Support", GEOMETRY_MESSAGE),
                      "7": ("<action requested> Geometry Support", GEOMETRY_MESSAGE)}
    
    header, message = email_content[period]
    
    
    email = MIMEMultipart("alternative")
    email["Subject"] = header
    email["From"] = TEACHER_EMAIL
    email["To"]  = s_email
#"To" TEACEHR_EMAIL needs to become s_email
    
    email.attach(MIMEText(message, 'html'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', PORT) as server:
        server.login(TEACHER_EMAIL, TEACHER_PASSWORD)
        server.sendmail(TEACHER_EMAIL, s_email, email.as_string())
        server.quit()    
        
    


# In[6]:


for period in CLASS_PERIODS:
    print(period)
    time.sleep(100)
    gradebook = pd.read_csv(Path(os.getcwd() + f"/Grades - P. {period} Grades.csv"))
    gradebook = gradebook.fillna('missing')
    student_names, student_emails, assignments = gradebook.columns[0], gradebook.columns[1], gradebook.columns[2:]
    for _, student in gradebook.iterrows():
        s_name, s_email, s_assignments = student[student_names], student[student_emails], student[assignments]
        missing_assignments = process_assignments(s_assignments)
        send_email(s_name, s_email, missing_assignments, period)
        
#TEACHER_EMAIL needs to become s_email
        


# In[ ]:
