import datetime
import pandas as pd

class Datetime:
    def __init__(self) -> None:
        pass
    def date_time_parser(self,datetime):
        self.datetime = datetime
        try:
            self.parsed_date = [i.split(' ')[0] for i in datetime]
            self.time_stamp =[i.split(' ')[1] for i in datetime]
            return (self.parsed_date , self.time_stamp)
                              
        except Exception as e:
            print(e)