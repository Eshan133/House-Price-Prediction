from abc import ABC, abstractmethod

import pandas as pd

# Abstract class (Base Class)
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform Basis data inspection

        Parameters:
        - df(pd.DataFrame)

        Returns:
        - None
        """
        pass

#----------------------------------------------------        
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspects and prints data types and non-null counts

        Parameters:
        - df(pd.DataFrame)

        Returns:
        - None
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints summary statistics to the console.
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["0"]))
#----------------------------------------------------

# This class allows you to switch between different data inspection strategies.
class DataInspector:
    def __init__(self, strategy:DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy
    
    def set_strategy(self, strategy:DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy
    
    def execute_inspection(self,df:pd.DataFrame):
        """
        Executes the inspection using current strategy

        Parameters:
        df(pd.DataFrame)

        Returns:
        None
        """
        self._strategy.inspect(df)

    if __name__ == '__main__':
        pass