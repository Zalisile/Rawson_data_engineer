# Rawson_data_engineer
Code test for data engineering

**The code flow**


**Add_data_app:** 
The first image handles the database connection and table creation. It waits for a certain amount of time to ensure the database is ready before proceeding.

**Schema_app:** The second image processes the data from the CSV files, inserts the data into the tables, and executes the SQL query to retrieve the required data. It also waits for a certain amount of time before querying and writing the JSON output file to ensure the data is available.
The  Github repo containing:

**Some of the sources I have referenced:**

https://devopscube.com/build-docker-image/
https://docker-curriculum.com/
https://pythonspeed.com/articles/base-image-python-docker-images/#:~:text=If%20you%20want%20the%20absolute,Debian%20Bookworm%2C%20released%20June%202023.
https://stackoverflow.com/questions/tagged/docker
