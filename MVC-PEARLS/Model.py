import csv
from csv import writer

class Model :
    def __init__(self):
        self.data = []
        line_count = 0
        with open('DataUser.csv') as dataFile :
            csv_reader = csv.reader(dataFile, delimiter=',')
            if(csv_reader == None):
                dataFile.close()
            else :
                for row in csv_reader:
                    self.data.append(row)
                    line_count += 1
                dataFile.close()
    
    def _set_data(self, userName, passWord):
        self.data.append([userName, passWord])
        with open('DataUser.csv', 'a', newline='') as dataFile:
            csv_writer = writer(dataFile)
            csv_writer.writerow([userName, passWord])
        dataFile.close()
        
    def _get_data(self):
        return self.data
    
    def _get_round(self, userName):
        return len(self.data)+1
    
    def _clear(self) :
        open("DataUser.csv", "w+").close()