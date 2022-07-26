import pandas as pd
from openpyxl import load_workbook
import os

#load csv input of information for new cell lines to onboard
#csv input columns should be as follows:
    #COLUMNS ON THE INPUT ONBOARDING FILE MUST EXACTLY MATCH DATAPOINTS LISTED ON cell_locations/datapoint_cell_locations.csv
def load_csv_input(file_path, file_name):
    input_file = pd.read_csv(file_path + file_name, low_memory = False)
    return input_file

#function to create new cell line sheet using metadata
    #function input should be a dictionary with information that is to be entered into the template file
    #datapoints to input are customizable based on the file in r'cell_locations/datapoint_cell_locations.csv'
def create_new_sheet(onboarding_metadata):
    #declare output variables (output path and output name)
    output_file_path = r'/Volumes/GoogleDrive/Shared drives/GPP Cloud /Screening /Achilles/CRISPR/CRISPR screens/'
    screens_completed_path = r'/Volumes/GoogleDrive/Shared drives/GPP Cloud /Screening /Achilles/CRISPR/CRISPR screens/Screens completed passaging/'
    output_file_name = '{}_{}_{}.xlsx'.format(onboarding_metadata['STRIPPED Cell Line Name DepMap'].upper(), onboarding_metadata['Library'].upper(), onboarding_metadata['ASP ID'].upper())

    #check to see if file already exists, and do not save if sheet does already exist
    if os.path.exists(output_file_path + output_file_name):
        print('File already exists for {}! Will not overwrite existing file.\n'.format(output_file_name))
        raise Exception
    elif os.path.exists(screens_completed_path + output_file_name):
        print('File already exists for {}! Will not overwrite existing file.\n'.format(output_file_name))
        raise Exception
    else: #create new file and save if there is not an existing sheet
        #template file paths and file names
        template_info = pd.read_csv(r'template_file_info/template_file_paths.csv')
        template_info_library = template_info[template_info['library'].isin([onboarding_metadata['Library'].upper()])]
        template_file_path = template_info_library['file_path'].values
        template_file_name = template_info_library['file_name'].values

        #Open template for specific library
        template = load_workbook(''.join(template_file_path + template_file_name))
        
        #dictionary for each datapoint and corresponding cell in the excel file - change the cell positions if the template positions is changed in any way
        excel_cell_positions = pd.read_csv(r'template_file_info/datapoint_cell_locations.csv').set_index('datapoint')
        excel_cell_positions = excel_cell_positions[excel_cell_positions['library'].str.upper() == onboarding_metadata['Library'].upper()]
        
        #input information into corresponding cell in file
        for key, value in onboarding_metadata.items():
            datapoint_info = excel_cell_positions.loc[key]  #get info for a given datapoint such as tab_name, cell_location
            template_sheet = template[datapoint_info['tab_name']] #open template to corresponding tab for datapoint
            
            template_sheet[datapoint_info['cell_location']] = value #set excel cell as value

        #Save the spreadsheets
        template.save(filename = output_file_path + output_file_name)
        print('Succesfully created sheet for {} {}     :)\n'.format(onboarding_metadata['STRIPPED Cell Line Name DepMap'].upper(), onboarding_metadata['Library'].upper()))
