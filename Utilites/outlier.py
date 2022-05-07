import numpy as np
class outlier_detect:
    def __init__(self) -> None:
        pass
    def outlier_remove(self,df):
        self.df = df
        try:
            for i in self.df.describe().columns:
                self.Q1=self.df.describe().at['25%',i]
                self.Q3=self.df.describe().at['75%',i]
                self.IQR=self.Q3 - self.Q1
                self.LTV=self.Q1 - 1.5 * self.IQR
                self.UTV=self.Q3 + 1.5 * self.IQR
                self.x=np.array(self.df[i])
                self.p=[]
                for j in self.x:
                    if j < self.LTV or j>self.UTV:
                        self.p.append(self.df[i].median())
                    else:
                        self.p.append(j)
                self.df[i]=self.p
            return self.df
        except Exception  as e:
            print(e)