from sklearn.model_selection import cross_validate
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score


class Modelevaluator(object):
    def __init__(self, model, x_train, x_test, y_train, y_test):
        self.model = model
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
    
    def r2score(self):
        self.model.fit(self.x_train, self.y_train)
        y_pred=self.model.predict(self.x_test)
        return (r2_score(self.y_test, y_pred))
    
    def cross_evaluation(self, cv_int):
        self.model.fit(self.x_train, self.y_train)
        scores_tfidf = cross_validate(self.model, self.x_train, self.y_train, cv=cv_int,
                              return_train_score=True,
                              return_estimator=False)
        mean_train = round(scores_tfidf['train_score'].mean(),3)
        mean_test = round(scores_tfidf['test_score'].mean(),3)
        if abs(mean_train - mean_test) > 0.05:
            return print('Overfitting',',','mean_train_score:',mean_train,',',
                 'mean_test_score:',mean_test)
        else:
            return print('Not Overfitting',',','mean_train_score:',mean_train,',',
                 'mean_test_score:',mean_test)
    
    def plot_feature_importances(self):
        importances = pd.Series(data=self.model.feature_importances_, index= self.x_train.columns)
        # Sort importances
        importances = importances.sort_values(ascending=False)
        # Draw a horizontal barplot of importances_sorted
        return importances
    
    def generate_predictions(self):
        self.model.fit(self.x_train, self.y_train)
        y_test_pred=self.model.predict(self.x_test)
        return y_test_pred
    
    def save_model(self, filename):
        pkl_filename = filename
        with open(pkl_filename, 'wb') as file: 
            return pickle.dump(self.model, file)