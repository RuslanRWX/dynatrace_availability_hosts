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

  Scopes: ![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/8239244b-a5e4-458d-9403-29e0a07b141f)

4. add token to dt_availability_by_hosts.py file

   ![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/44bf2e6c-f241-4a96-a3ef-e323a8ef50cd)
   

   
How to use it

![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/9fa0b6e7-35fb-4d84-9ffb-20b61dfc460f)

then you'll see en Excel file in the same directorie

![image](https://github.com/ruslansvs2/dynatrace_availability_hosts/assets/18479441/cff408f7-eb70-4c1c-aac4-9b2a08acc601)


