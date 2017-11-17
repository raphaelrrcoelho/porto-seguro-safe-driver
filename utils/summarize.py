import pandas as pd

def get_feature_importance_df(feature_importances, column_names, top_n = 25):
    """Get feature importance data frame.
 
    Parameters
    ----------
    feature_importances : numpy ndarray
        Feature importances computed by an ensemble 
            model like random forest or boosting
    column_names : array-like
        Names of the columns in the same order as feature 
            importances
    top_n : integer
        Number of top features
 
    Returns
    -------
    df : a Pandas data frame
 
    """
     
    imp_dict = dict(zip(column_names, feature_importances))

    top_features = sorted(imp_dict, key = imp_dict.get, 
                          reverse=True)[0:top_n]
    
    top_importances = [ imp_dict[feature] for feature in top_features ]
    
    df = pd.DataFrame(
            data = {'feature': top_features, 'importance': top_importances})
    
    return df

def get_meta(df,
             special = {'id': {'role': 'id', 'level': 'nominal'},
                        'target': {'role': 'target', 'level': 'binary'}},
             suffix_level = {'bin': 'binary', 'cat': 'nominal'},
             dtype_level = {'float64': 'interval', 'int64': 'ordinal'}):
    """Get metadata from data frame.
 
    Parameters
    ----------
    special : dict
        Dictionary with features that need special treatment. e.g. id, target
    suffix_level : dict
        Dictionary that maps suffixes in columns names to levels
    dtype_level: dict
        Dictionary that maps dtypes from columns to levels
 
    Returns
    -------
    df : a Pandas data frame
 
    """
    data = []

    for col in df.columns:
        dtype = df[col].dtype

        if col in special.keys():
            role = special[col].get('role', None)
            level = special[col].get('level', None)
        else:
            role = 'input'
            level = None

        if not level:
            for suffix in suffix_level.keys():
                if suffix in col:
                    level = suffix_level[suffix]

        if not level:
            level = dtype_level.get(str(dtype), None)

        # Initialize keep to True for all variables except for id
        keep = False if col == special['id']['role'] else True

        col_dict = {
            'varname': col,
            'role': role,
            'level': level,
            'keep': keep,
            'dtype': dtype
        }

        data.append(col_dict)

    meta = pd.DataFrame(data, columns = ['varname', 'role', 'level', 'keep', 'dtype'])
    meta.set_index('varname', inplace = True)

    return meta
    data = []

    for col in df.columns:
        dtype = df[col].dtype

        if col in special.keys():
            role = special[col].get('role', None)
            level = special[col].get('level', None)
        else:
            role = 'input'
            level = None

        if not level:
            for suffix in suffix_level.keys():
                if suffix in col:
                    level = suffix_level[suffix]

        if not level:
            level = dtype_level.get(str(dtype), None)

        # Initialize keep to True for all variables except for id
        keep = False if col == special['id']['role'] else True

        col_dict = {
            'varname': col,
            'role': role,
            'level': level,
            'keep': keep,
            'dtype': dtype
        }

        data.append(col_dict)

    meta = pd.DataFrame(data, columns = ['varname', 'role', 'level', 'keep', 'dtype'])
    meta.set_index('varname', inplace = True)

    return meta
