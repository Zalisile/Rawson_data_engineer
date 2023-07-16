# Rawson_data_engineer
Code test for data engineering

**The code flow**


**Add_data_app:** 
The first image handles the database connection and table creation. It waits for a certain amount of time to ensure the database is ready before proceeding.

**Schema_app:** The second image processes the data from the CSV files, inserts the data into the tables,

and executes the SQL query to retrieve the required data. 

It also waits for a certain amount of time before querying and writing the JSON output file to ensure the data is available.

**A data folder containing four files:**

    -places.csv 113 rows, where each row has a city, county, and country name.
    
    -people.csv 10,000 rows, where each row has a first name, last name, date of birth, and city of birth.
    
    -sample_output.json Sample output file, to show what your output should look like.

**Instsructions on how to  running the code:**

Step 1: Download and unzip the code

        - Download the code from the provided GitHub link.
        - Unzip the downloaded file to a location of your choice.

Step 2: Open Command Prompt

        - Open Command Prompt (cmd) by pressing the Windows key, typing "cmd," and selecting the Command Prompt application.

Step 3: Navigate to the code directory

        - Use the `cd` command to navigate to the `Rawson_data_engineer-main` folder within the extracted code directory.
        - For example, if you extracted the code to `C:\path\to\Rawson_data_engineer-main`, run the following command:
                
                cd C:\path\to\Rawson_data_engineer-main


Step 4: Stop any existing Docker containers

        - Before running the code, make sure you don't have any other Docker containers running.
        - Run the following command to stop any running containers:

                docker compose down

Step 5: Build and run the Docker containers

        - Run the following command to build the Docker images and start the containers:

                docker-compose up --build


Step 6: Wait for the code to complete

        - The code may take approximately 10 minutes to run.
        - Wait for the code execution to finish.

After completing these steps, the code will have executed, and you should see the output and any generated files according to the code's logic.



**Some of the sources I have referenced:**

https://devopscube.com/build-docker-image/

https://docker-curriculum.com/

https://pythonspeed.com/articles/base-image-python-docker-images/#:~:text=If%20you%20want%20the%20absolute,Debian%20Bookworm%2C%20released%20June%202023.

https://stackoverflow.com/questions/tagged/docker

https://chat.openai.com/
