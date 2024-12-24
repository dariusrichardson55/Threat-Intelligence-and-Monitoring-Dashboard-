# Description
This project demonstrates how to generate an API from LevelBlue/Labs as a CSV file, then import that CSV file into the Grafana dashboard, and provide an example of how to analyse that data to make it visually easier to identify specific cyberattacks.

# Websites
These are the websites used to create the dashboard.
<ul>
  <li>LevelBlue/Labs</li>
  <li>Grafana</li>
</ul>

# File
This is the Python file that will be used to generate the CSV file. 
<ul>
  <li>alienvault_fetch.py</li>
</ul>

# Local host
http://localhost:3000

# Project Walk-through

<h2>LevelBlue/Labs - Get the API Key</b></h2>
<p style="text-align:center">This API Key will need to be retrieved to put in the Python script (alienvault_fetch.py).</p>

You need to go to the LevelBlueLabs website (https://otx.alienvault.com/) and sign up.
![image](https://github.com/user-attachments/assets/602b62b5-6fbc-45a3-95ab-d9ce0545cd8d)

Next, go to the username and select settings, this is the page where you access the OTX API.
![image](https://github.com/user-attachments/assets/616aa1e5-ba33-4289-b825-eef82652dc7d)

Copy your OTX API Key.
![image](https://github.com/user-attachments/assets/b9e4b35e-fdcd-48d1-860f-b53610dc2185)

<h2><b>Download and Run Python Script</b></h2>
Next, you download and run the Python script file (the Python script file is in the GitHub repository). Before running the Python script, make sure to install Python on the command prompt, to do this enter ‘pip install requests pandas’ in the command prompt.

![image](https://github.com/user-attachments/assets/70ecd6c0-cf24-4870-b00d-b1dcf12e1ccc)

Next, make sure to use 'cd' and then the location of the file that you downloaded it to. Then enter type ‘python alienvault_fetch.py’ to run the file. Once that is complete you will see a csv file in the same location the python file is saved.

![image](https://github.com/user-attachments/assets/59895bd9-9d69-4103-8169-f4bbbc3bbc10)

<h2><b>Grafana - Create Dashboard</b></h2>
You need to go to the Grafana website (<a href="https://grafana.com/grafana/download?platform=windows">Download Grafana</a>) and then press ‘download the installer’.

![image](https://github.com/user-attachments/assets/647868c0-92f2-4da8-b01d-7a228cd3cf11)

To make sure that the localhost is running, go to services and select ‘Grafana’ if it is not running then press start but if it is running then close the services application.
![image](https://github.com/user-attachments/assets/ebd1bd49-007b-431a-ae26-0df16d1b9ee4)

Open the web browser and enter http://localhost:3000 in the web address. Enter admin for the username and password then press log in.
![image](https://github.com/user-attachments/assets/0247c2af-e072-4b40-8505-f354c81cbcae)

Note: The website might direct you to the update your password page, you can change the password or just press skip.
![image](https://github.com/user-attachments/assets/a2373fa6-f6c0-46a1-9c86-7c112ec6485c)

Cut the threat_intelligence file from where it was saved and paste it into the CSV folder. Go to C:\Program Files\GrafanaLabs\grafana\data\csv to paste the file.
![image](https://github.com/user-attachments/assets/ef8884b7-cd50-435d-bb3f-14a936651cd8)

To add the ‘threat_intelligence’ CSV file, select ‘add your first data source’
![image](https://github.com/user-attachments/assets/9665e68d-4f3c-4808-a087-ade0b46bd46a)

Next, type in CSV and then select CSV.
![image](https://github.com/user-attachments/assets/6da35d6e-360f-4700-91c5-1bd88ce0766d)

To upload the csv file, select the local file button then paste the file location (C:/Program Files/GrafanaLabs/grafana/data/csv/threat_intelligence.csv). Change each back slash‘\’ from the file location to forward slash ‘/’, this will allow Grafana to recognise the CSV file. Press Save and test. The screen should display success. Now click on Building a Dashboard.
![image](https://github.com/user-attachments/assets/d6a16c4e-3c53-49f4-8f81-3bb0b9655763)

Select add visualisation.
![image](https://github.com/user-attachments/assets/7c3607fc-226a-403b-993a-f829af174d68)

Then just select the CSV that you imported.
![image](https://github.com/user-attachments/assets/8648aca3-9d20-489b-8f74-04dfe4c42868)

To display the data, select the table view button.
![image](https://github.com/user-attachments/assets/74072a83-c7a1-40c0-81a3-e28f89ac4a25)

Now to filter the table for the dashboard, go to Transformations and then click Add Transformation.
![image](https://github.com/user-attachments/assets/f68e0677-cf61-420a-bd97-0a89336d13a0)

Select Filter and select ‘Filter data by values’.
![image](https://github.com/user-attachments/assets/af727f7a-509f-44a9-8a88-620451236c98)

This demonstrates how to filter the data to Pulse_Name for the type of cyberattack and the ‘type’ to a domain to see the names of websites mentioned in the indicator column. 
![image](https://github.com/user-attachments/assets/ae351c63-edc7-4da0-9d1c-fd5122b7f45e)

Name the dashboard ‘Cloud Atlas using a new backdoor’ then press save. Next, type dashboards in the search bar at the top and select ‘Dashboard’.
![image](https://github.com/user-attachments/assets/c0bc580b-675e-4df8-9aed-3444c33c2816)

This is the page where all created dashboards are stored.
![image](https://github.com/user-attachments/assets/0e070702-f45b-4157-89a9-ba99531022df)




