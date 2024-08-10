import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        
        print("Dataset fetched and saved successfully.")

        # Assuming the content is in text format (e.g., CSV, JSON)
        dataset_content = response.text

        return dataset_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {str(e)}")
        return None
    
    
from sklearn.base import BaseEstimator,TransformerMixin

class DataFrameSelector(BaseEstimator,TransformerMixin):
    #Takes dataframe as input and selects only those features and converts them into numpy arrays
    def __init__(self,attribute_names):
        self.attribute_names=attribute_names
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        return X[self.attribute_names].values

