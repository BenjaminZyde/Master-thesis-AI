if __name__ == "__main__":
    
    
    import pandas as pd
    import tsfresh
        
    #location source file
    source= "../rearangeddata/new 3-01/pandas-finalproof.pkl"
    inputs = "../rearangeddata/new 3-01/series-finalproof.pkl"
   
    #settings = MinimalFCParameters()
    
    pf = pd.read_pickle(source)
    
    test = pf.query("id== \"DO47100000006A058341\"")
	

    
 
    
    
    #y=pd.read_pickle(inputs)
    #del pf['set_temperature']
            
    #extract features
    #features = extract_features(pf, column_id="id",column_sort="time_stamp",default_fc_parameters=settings)
    df_rolled,y = tsfresh.utilities.dataframe_functions.make_forecasting_frame(test['real_temperature'],"temperature",6,1)
    #needs one time series, kind of data (str), rolling direction 
   
    
    #features.to_pickle(savefeatures)
    #features.to_csv(excel, sep=';')

