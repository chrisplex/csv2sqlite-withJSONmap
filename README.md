# csv2sqlite-withJSONmap

If you ever wanted to just take a few csv's and create a local db with very little setup, this is your script.

Check out the Repository (or download the code).

Open the `params.json` file to edit the params.json file and edit the filename, delimiter, filepath, column names. You can use active and type for further processing, but for now you can just ignore those. 
On the columns section, the key will be the name of the column that will be created while the parameter will be the name of the column of the csv.

If you modified keys, open the main 'loader.py' script to edit function call data_entry() and edit the `table_1` in case you edited it you passed in.

Close the params file and run the script. 

If you want to query anything, use https://github.com/sqlitebrowser/sqlitebrowser/releases
