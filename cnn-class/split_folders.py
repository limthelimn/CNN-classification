import splitfolders     # split folder to train, test, validation

input_folder = "datasets"

splitfolders.ratio(input_folder, output="datasets_split", 
                   seed=42, ratio=(.8, .1, .1), 
                   group_prefix=None)