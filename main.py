# MAIN FUNCTION TO CREATE NEW CELL LINE SHEETS FROM AN INPUT CSV FILE

def main():
    #import relevant modules and functions
    import pandas as pd
    from openpyxl import load_workbook
    from cell_line_onboarding import load_csv_input, create_new_sheet
    import argparse
    
    #get input file from argument passed to script 
    parser = argparse.ArgumentParser(description='Create new excel files for unique Achilles CRISPR screens.')
    parser.add_argument('input_file', metavar='N', type=str, nargs= 1,
                    help='The exact name of your input csv file')

    args = parser.parse_args()

    input_file_name = args.input_file[0]
    
    if '.csv' in input_file_name:
        pass
    elif '.csv' not in input_file_name:
        input_file_name = input_file_name + '.csv'

    #create pd df from input information csv file
    input_file_path = r'input_onboarding_data/'   #path of input file
    onboarding_data = load_csv_input(input_file_path, input_file_name)

    #load input file as dictionary
    print('\n----------------------------------------------------------------\nAttempting to create {} cell line sheets\n----------------------------------------------------------------\n'.format(onboarding_data.shape[0]))    #inform user size of the inputted file
    
    #variables to keep track of succesful creations and fails
    fail = []
    success = []
    
    #iterate over inputted csv file - each row contains relevant information for that cell line
    for index, row in onboarding_data.iterrows():
        data = row.to_dict()
        try: 
            print('Creating excel file for {}...'.format(data['STRIPPED Cell Line Name DepMap']))
            create_new_sheet(data)
            success.append(data['STRIPPED Cell Line Name DepMap'])
        except Exception:
            print('Failed to create excel file for {}'.format(data['STRIPPED Cell Line Name DepMap']))
            fail.append(data['STRIPPED Cell Line Name DepMap'])
            pass
        
    #print information for which sheets were created and which were not
    print('____________________________________________________________________________________________\n')              
    print('Created {} cell line sheets for: {}'.format(len(success), success))
    print('____________________________________________________________________________________________\n')
    print('Failed to create {} cell line sheets for: {}'.format(len(fail), fail))
    print('____________________________________________________________________________________________\n')

if __name__ == '__main__':
    main()




