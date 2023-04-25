import pandas as pd
import ast
import json

def non_personalized_rec(input_ingredients):

    merged_df = pd.read_csv('main/core/csv/merged_df.csv', usecols=['name','recipe_id','minutes','contributor_id','submitted','tags','nutrition','n_steps','steps','description','ingredients','n_ingredients','time_to_cook','rating'])
    ing_rec = pd.read_csv('main/core/csv/ing_rec2.csv', usecols=['ingredient','recipes'])
    def str_to_list(l):
        try:
            return ast.literal_eval(l)
        except ValueError:
            return []

    ing_rec['recipes'] = ing_rec['recipes'].apply(str_to_list)
    merged_df['steps'] = merged_df['steps'].apply(str_to_list)
    filtered_table = ing_rec[ing_rec['ingredient'].isin(input_ingredients)]
    l = filtered_table['recipes'].tolist()
    def find_intersection(lists):
        # convert each list to a set
        sets = [set(lst) for lst in lists]
        # take the intersection of all sets
        intersection = set.intersection(*sets)
        # convert the intersection back to a list
        result = list(intersection)
        return result
    r_with_other_ing = find_intersection(l)
    def exact_recipes(r_with_other_ing):
        req_ing_count = len(input_ingredients)
        df_recipes = merged_df[merged_df['recipe_id'].isin(r_with_other_ing)]
        df_ing  = df_recipes[df_recipes['n_ingredients']==req_ing_count]
        df_ing = df_ing.sort_values(by=['rating'], ascending=[False])
        return df_ing[0:10]
    def add_l(l):
        new_l = json.loads(l)
        s = sum(new_l)
        return s
    def low_cal(r_with_other_ing):
        df_recipes = merged_df[merged_df['recipe_id'].isin(r_with_other_ing)]
        df_recipes['calories'] = df_recipes['nutrition'].apply(add_l)
        df_low_cal = df_recipes.sort_values(by=['calories', 'rating'], ascending=[True, False])
        return df_low_cal[0:5]
    def few_steps(r_with_other_ing):
        df_recipes = merged_df[merged_df['recipe_id'].isin(r_with_other_ing)]
        df_low_steps = df_recipes.sort_values(by=['n_steps', 'rating'], ascending=[True, False])
        return df_low_steps[0:5]
    def order_by_time(r_with_other_ing):
        df_recipes = merged_df[merged_df['recipe_id'].isin(r_with_other_ing)]
        df_low_time = df_recipes.sort_values(by=['time_to_cook', 'rating'], ascending=[True, False])
        return df_low_time[0:5]


    ans = {}
    ans['exact_recipes'] = exact_recipes(r_with_other_ing).to_dict(orient='records')
    ans['low_cal'] = low_cal(r_with_other_ing).to_dict(orient='records')
    ans['few_steps'] = few_steps(r_with_other_ing).to_dict(orient='records')
    ans['order_by_time'] = order_by_time(r_with_other_ing).to_dict(orient='records')
    
    return ans