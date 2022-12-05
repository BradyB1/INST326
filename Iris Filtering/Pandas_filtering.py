import sys
import argparse
import pandas as pd
   


def main(filename, species):

    '''Edits the Iris file to give it headers, reads into the iris file
    runs the filter functino with species and iris 

    args:
        filename(str): name of the file we are using 
        species(str): name of the Iris species 
        columns(list): gives the dataframe headers 
        iris(Database): The iris database 
    
    '''
    def filter(species, iris):
        '''function to filter out the species from the iris dataframe 
            it will use the describe function on filtered 
            
        args:
            species(str): the species of the iris plant 
            iris(df): dataframe we are working with 
            filtered(list): list containing the species we select 
            
        side effects: 
            will create a write to a txt doc. Will write the description of filtered variable to .txt
        '''
        #filteres select species 
        filtered = iris.loc[iris["Species"] == species]
        
        #returns description of the filtered data 
        print(filtered.describe())
        
        #Opens the text file and writes to it 
        with open("output.txt", "w") as f:
            #writes filtered.describe to the file 
            f.write(filtered.describe().to_csv())
    columns= ["sep len","sep wid","pet len","pet wid","Species"]
    iris = pd.read_csv(filename, names =columns)
    print(iris)
    filter(species, iris)


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--filename', type = str, help = 'Name of the file.')
    parser.add_argument('--species', type = str, help = 'Name of species of iris plant.')
    
    args = parser.parse_args(args_list)
    
    return args


if __name__ == "__main__":
    
    
    args = parse_args(sys.argv[1:])
    main(args.filename, args.species)





