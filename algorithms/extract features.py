
if __name__ == "__main__":
    import matplotlib
    import matplotlib.pyplot as plt
    import datetime
    from tsfresh.feature_extraction import MinimalFCParameters
    from tsfresh.feature_extraction import extract_features
    import pandas as pd
    
    
    #location source file
    source= "../rearangeddata/new 3-01/pandas-bake.pkl"
    savefeatures = "../rearangeddata/new 3-01/pandas-bake-features.pkl"
    excel = "../rearangeddata/new 3-01/pandas-bake-features.csv"
    
   
    settings = MinimalFCParameters()
    
    pf = pd.read_pickle(source)
    #lists= [True for x in range(len(pf))]
    #y= pd.Series(lists)          
    #extract features
    features = extract_features(pf, column_id="id",column_sort="time_stamp",default_fc_parameters=settings)
    #features = tsfresh.extract_relevant_features(pf,y, column_id="id",column_sort="time_stamp")
    features.to_pickle(savefeatures)
    features.to_csv(excel, sep=';')