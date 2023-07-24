# dynatrace_availability_hosts
Get availability by hosts from Dynatrace 

It'll help if you need to gather availability by hosts from dynatrace monitoring system for a certain period of time. 
The script will generate an Excel file with host and availability metrics. 

1. add liberies
   pip install tkcalendar
   pip install datetime
   pip install requests
   pip install xlwt
2. generate token in Dynatrace
  Management->Access tokens->Generate new token 

  Scopes: ![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/a78442fe-6f3c-4950-9523-9d895021a464)


4. add token to dt_availability_by_hosts.py file

   ![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/6baf6b4d-e876-4081-aab5-5af847d20db2)

   
How to use it: run the script

![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/db5bc415-5bd2-4b5b-b822-286dd40d4011)


then you'll see en Excel file in the same directorie

![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/cad3acde-5d5f-4045-ab41-e776355cd67a)



