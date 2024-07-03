from App import Visualize
import seaborn as sns
# Loading the dataset
df = sns.load_dataset("penguins")
# making an instances
ans = Visualize(df)
ans.Univariate_Histogram()
ans.Univariate_Distplot()
ans.Univariate_Normalized()
ans.Univariate_Probability()
ans.Univariate_Kde_Plot()
ans.Univariate_Ecdf_Plot()
ans.Univariate_ECDF_Plot()