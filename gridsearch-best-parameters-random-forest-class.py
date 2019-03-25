from sklearn.grid_search import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

param_grid = { 
    'n_estimators': [200, 700],
    'max_features': ['auto', 'sqrt', 'log2'],
    'min_samples_leaf':[2,4],
    'min_samples_split':[4,6],
    'oob_score' : ['TRUE'],
    'random_state':[1]
    
    
    
}

CV_rfc = GridSearchCV(estimator=rf, param_grid=param_grid, cv= 5)
CV_rfc.fit(X_train, y_train.values.ravel())
print(CV_rfc.best_params_)
