#SVM: support vector machine

%matplotlib inline
import warnings
warnings.filterwarnings('ignore')  #suppress warning
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#use seaborn plotting defaults
import seaborn as sns
sns.set()

from sklearn.datasets.samples_generator import make_blobs
X, y = make_blobs(n_samples = 50, centers = 2, n_features = 2, random_state = 0, cluster_std = 0.60)
#generate random data to be clustered
print(X.shape)
print(y,shape)
plt.scatter(X[:, 0], X[:, 1], c = y, s = 50, cmap = 'autumn')