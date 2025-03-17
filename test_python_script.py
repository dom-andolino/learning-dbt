import os
import requests
import pandas as pd


def get_query_results(query_str):
    '''
    inputs: query_str = query string to search for
    output: dictionary of api result
    notes:
        hard coded limit to 500 which is max allowed per api docs
        hard coded types=Person to limit to results which are people
    '''

    h_dict = {'Accept': 'application/json'}
    p_dict = {
                'key': api_key,
                'types': 'Person',
                'limit': 500,
                'indent': True,
                'languages': 'en',
                'query': query_str
            }
    
    resp = requests.get(
                url = service_url, 
                headers = h_dict, 
                params = p_dict
            )
    
    if resp.status_code != 200:
        raise(Exception('{} error, {}'.format(resp.status_code, resp.reason)))
    else:
        resp_json = resp.json()
    
    return(resp_json)


def get_result_names(query_str):
    '''
    inputs: query_str = query string to search for
    output: df of celeb_nm, category, rnk
    '''
    
    result_df = pd.DataFrame(columns=["celeb_nm", 'cat', 'cat_rnk']) #initialize empty df
    results = get_query_results(query_str=query_str)['itemListElement']
    
    for cat_rnk, result in enumerate(results):
        #loop over all results to pull out names
        result_dict = result['result']
        result_name = result_dict['name']
        result_name_series = pd.DataFrame([[result_name, query_str, cat_rnk]], columns=result_df.columns) 
        result_df = pd.concat([result_df, result_name_series], ignore_index=True)
        
    return(result_df)



if __name__ == '__main__': 

    api_key = os.environ.get("GOOGLE_API_KEY")
    service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
    celeb_nm_output_path = 'data/test_python_script_output.csv'

    all_result_names_df = pd.DataFrame(columns=["celeb_nm", 'cat', 'cat_rnk']) #initialize empty df
    query_list = ['Actors', 'Netflix', 'NFL', 'YouTube', 'Bitcoin', 'Politician']

    for query in query_list:
        #call api and get list of names for each query
        print('\nGetting Names for: {}'.format(query))
        result_df = get_result_names(query_str=query) #get df of names matching query
        all_result_names_df = pd.concat([all_result_names_df, result_df], ignore_index=True) #append current df to all_df


    #add some extra calculated fields
    all_result_names_df.sort_values(by = ['celeb_nm', 'cat_rnk', 'cat'], inplace = True)
    all_result_names_df.reset_index(drop=True, inplace=True)
    all_result_names_df['cat_rnk'] = all_result_names_df['cat_rnk'].apply(lambda x: int(x)) #needs to be an into for below transforms to work
    all_result_names_df['num_cats'] = all_result_names_df.groupby(['celeb_nm'])['cat'].transform('count') # count of rows (ie number of serach terms the name came up in)
    all_result_names_df['bst_cat_rnk'] = all_result_names_df.groupby(['celeb_nm'])['cat_rnk'].transform('min') # lowest rnk will be the best match
    all_result_names_df['bst_cat_rnk_idx'] = all_result_names_df.groupby(['celeb_nm'])['cat_rnk'].transform('idxmin') #add index of best match so we can do below to get associated cat
    all_result_names_df['bst_cat'] = all_result_names_df.loc[all_result_names_df.bst_cat_rnk_idx, 'cat'].values #add best cat


    #dedupp, remove extra cols
    all_result_names_df.drop(['cat','cat_rnk', 'bst_cat_rnk_idx'], axis=1, inplace=True)
    all_result_names_df.drop_duplicates(subset = 'celeb_nm', keep = 'first', inplace = True)


    all_result_names_df.to_csv(celeb_nm_output_path, index=False, encoding='utf-8', sep=',') #save to csv
