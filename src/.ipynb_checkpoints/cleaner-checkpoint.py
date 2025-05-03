# Cleaner class for handling missing values and duplicates
class Cleaner:
    def clean(self, df):
        df = df.drop_duplicates()
        df = df.fillna(method='ffill')
        return df