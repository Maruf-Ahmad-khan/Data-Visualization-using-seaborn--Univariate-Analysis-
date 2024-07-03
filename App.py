import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

class Visualize:
     def __init__(self, df):
        self.df = df

     # Histogram 
     def Univariate_Histogram(self, folder_path="plots", file_name="univariate_histogram.png"):
        sns.set()
        plt.figure(figsize=(10, 5))
        sns.histplot(self.df["flipper_length_mm"], kde=True)
        plt.title("Univariate Analysis")
        plt.grid(True)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.show()
      
     # Distplot (Histogram)   
     def Univariate_Distplot(self, folder_path="plots", file_name="univariate_distplot.png"):
        sns.set()
        plt.figure(figsize=(10, 5))
        sns.distplot(self.df["flipper_length_mm"], kde=True)
        plt.title("Univariate Distribution Plot")
        plt.grid(True)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.show()
        
        
     # Normalised (Histogram)
     def Univariate_Normalized(self, folder_path="plots", file_name="Univariate_Normalized.png"):
        sns.set()
        plt.figure(figsize=(10, 5))
        sns.histplot(data=self.df, x="flipper_length_mm", hue='species', stat='density', kde=True)
        plt.title("Univariate Normalized Plot")
        plt.grid(True)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        plt.savefig(file_path)
        plt.show()
        
     def Univariate_Probability(self, folder_path = "plots" , file_name = "Univariate_Probability.png"):
          sns.set()
          plt.figure(figsize=(10,5))
          sns.histplot(data = self.df, x = "flipper_length_mm", hue = "species", stat = 'probability', kde = True)
          plt.title("Univariate Probability Plot")
          plt.grid(True)
          os.makedirs(folder_path, exist_ok=True)
          file_path = os.path.join(folder_path, file_name)
          plt.savefig(file_path)
          plt.show()
          
     def Univariate_Kde_Plot(self, folder_path = "plots" , file_name = "Univariate_Kde.png"):
          sns.set()
          plt.figure(figsize=(10,5))
          sns.displot(data = self.df, x = "flipper_length_mm", hue = "species", multiple= 'stack', kde = True)
          plt.title("Univariate Kde Multiple Stack Plot")
          plt.grid(True)
          os.makedirs(folder_path, exist_ok=True)
          file_path = os.path.join(folder_path, file_name)
          plt.savefig(file_path)
          plt.show()
          
     def Univariate_Ecdf_Plot(self, folder_path = "plots" , file_name = "Univariate_Ecdf.png"):
          sns.set()
          plt.figure(figsize=(10,5))
          sns.displot(data = self.df, x = "flipper_length_mm", kind = 'ecdf')
          plt.title("Univariate Ecdf  Plot")
          plt.grid(True)
          os.makedirs(folder_path, exist_ok=True)
          file_path = os.path.join(folder_path, file_name)
          plt.savefig(file_path)
          plt.show()
          
     def Univariate_ECDF_Plot(self, folder_path = "plots" , file_name = "Univariate_ECDF.png"):
          sns.set()
          plt.figure(figsize=(10,5))
          sns.displot(data = self.df, x = "flipper_length_mm",hue='species', kind = 'ecdf')
          plt.title("Univariate ECDF  Plot")
          plt.grid(True)
          os.makedirs(folder_path, exist_ok=True)
          file_path = os.path.join(folder_path, file_name)
          plt.savefig(file_path)
          plt.show()