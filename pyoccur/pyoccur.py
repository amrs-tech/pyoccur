"""
Package to operate with 
duplicates in lists
"""
import pandas as pd

def convert_df_to_dict(df):
    dict_var = df.to_dict()
    return dict_var

def convert_dict_to_df(dict_var):
    df = pd.DataFrame.from_dict(dict_var)
    return df

def has_dup(list_var):
    uniqlist = []
    for i in list_var:
        if type(i) == pd.core.frame.DataFrame:
            itod = convert_df_to_dict(i)
            if itod not in uniqlist:
                uniqlist.append(itod)
        else:
            if i not in uniqlist:
                uniqlist.append(i)
    if len(list_var) != len(uniqlist):
        return True
    return False

def get_dup(list_var):
    duplist = []
    uniqlist = []
    finaldup = []
    for i in list_var:
        if type(i) == pd.core.frame.DataFrame:
            itod = convert_df_to_dict(i)
            if itod not in uniqlist:
                uniqlist.append(itod)
            else:
                if itod not in duplist:
                    duplist.append(itod)
                    finaldup.append(i)
        else:
            if i not in uniqlist:
                uniqlist.append(i)
            else:
                if i not in duplist:
                    duplist.append(i)
                    finaldup.append(i)
    return finaldup

def remove_dup(list_var):
    uniqlist = []
    finaluniq = []
    for i in list_var:
        if type(i) == pd.core.frame.DataFrame:
            itod = convert_df_to_dict(i)
            if itod not in uniqlist:
                uniqlist.append(itod)
                finaluniq.append(i)
        else:
            if i not in uniqlist:
                uniqlist.append(i)
                finaluniq.append(i)
    return finaluniq
