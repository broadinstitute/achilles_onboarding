import pandas as pd
from openpyxl import load_workbook

#load csv input of information for new cell lines to onboard
#csv input columns should be as follows:
    #COLUMN NAMES MUST BE EXACT, order is not important
    # Achilles Screening Project ID, Stripped Cell line name, Culture Medium, Culture Type, Arxspan Reg ID, Virus Pool Name
def load_csv_input(file_path, file_name):
    input_file = pd.read_csv(file_path + file_name, low_memory = False)
    return input_file

#function to create new cell line sheet using metadata
    #function input should be a pandas series with information: Achilles Screening Project ID, Stripped Cell line name, Culture Medium, Culture Type, Arxspan Reg ID, Virus Pool Name
def create_new_sheet(onboarding_metadata): 
    #template file paths and file names
    template_info = pd.read_csv(r'template_file_paths/template_file_paths.csv')
    template_info_library = template_info[template_info['library'].isin([metadata_dict['library'].upper()])]
    template_file_path = template_info_library['file_path'].values
    template_file_name = template_info_library['file_name'].values

    #Open template for specific library
    template = load_workbook(''.join(template_file_path + template_file_name))
    template_sheet = template['Cell Line Information']
    
    # dictionary for each datapoint and corresponding cell in the excel file - change the cell positions if the template positions is changed in any way
    excel_cell_positions = {'name' : 'D3', 'library' : 'D25', 'asp_id': 'D5', 
                            'media' : 'D9', 'culture_type' : 'D11', 'arx_id' : 'D4'}
    #variables for each piece of information in metadata
    metadata_dict = {
        'name' : onboarding_metadata['Stripped Cell line name'].upper().replace('-311CAS9', '').replace('-ENCAS12A', ''),
        'library' : onboarding_metadata['Virus Pool Name'].replace('-', ''),
        'asp_id' : onboarding_metadata['Achilles Screening Project ID'],
        'media' : onboarding_metadata['Culture Medium'],
        'culture_type' : onboarding_metadata['Culture Type'],
        'arx_id' : onboarding_metadata['Arxspan Reg ID'],
        }
    
    #input information into corresponding cell in file
    for key, value in excel_cell_positions.items():
        template_sheet[value] = metadata_dict[key]

    #save new sheet with correct file name
    output_file_path = r'/Volumes/GoogleDrive/Shared drives/GPP Cloud /Screening /Achilles/CRISPR/CRISPR screens/Cell Line Onboarding/'
    output_file_name = '{}_{}_{}.xlsx'.format(metadata_dict['name'].upper(), metadata_dict['library'].upper(), metadata_dict['asp_id'].upper())
    #Save the spreadsheets
    template.save(filename = output_file_path + output_file_name)
    print('Succesfully created sheet for {} {}'.format(metadata_dict['name'].upper(), metadata_dict['library'].upper()))


