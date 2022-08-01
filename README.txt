Python scripts to generate unique cell line sheets for Achilles screening. 

TEMPLATES 
There are excel files to be used as templates for each library located in the following folder: 
/Volumes/GoogleDrive/Shared drives/GPP Cloud /Screening /Achilles/CRISPR/CRISPR screens/Templates/

Each library has its own unique template. If you ever change the name, path, etc of the template files, you can update the template file information in a csv file located in the following path:
/template_file_info/template_file_paths.csv. This CSV file is also the place to add a new template path if Achilles begins screening with more libraries. 

Additionally, each template may have different locations for data, which can be specified in the following csv file: /template_file_info/datapoint_cell_locations.csv. It is important that the data points listed in this file match exactly the column headers from your input file (file containing the onboarding information for a given screen). The order of columns or datapoints is not important, but they must match spelling and case. Every column header on your input file must have a row in this ‘datapoint_cell_locations.csv’ file so the script knows where to input a piece of information. 

INPUT FILE
To run the script, you must create an input csv file that contains all the onboarding information for the screens you wish to create excel files for. 

Currently the input file contains the following columns: ASP ID, STRIPPED Cell Line Name DepMap, Media (Culture Conditions), Cell Type, Registration ID, Library. This data can be copy and pasted from the 'Thawing Plan' tab of Weekly Plan gsheet into the 'oboarding_template.csv' file and saved under a new name which you will specify when running the script.

It is important that the columns on your input file are directly listed in the following file: /template_file_info/datapoint_cell_locations.csv. The column headers from your input file are listed here as a 'datapoint'. New columns or data points can always be added. To do so, add a column header to your input file and add a new row(s) to ‘datapoint_cell_locations.csv’ for that datapoint. Since there are unique templates for every library, you will need to create a row for every library. For example, the datapoint ‘ASP ID’ has three rows in this csv file, which specifies the cell location for each library (currently three). 

To run the script:
1) Create input file containing onboarding information for a given screen
2) Save input file in the 'input_onboarding_data' folder and remember the name of your file 
3) In your terminal, navigate to the folder containing the onboarding scripts 
4) type 'python3 main.py INPUT_FILE_NAME.csv' with INPUT_FILE_NAME.csv being the name of the file you created containing all of the onboarding information
