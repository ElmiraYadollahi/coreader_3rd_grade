import csv
output = ['PS208\n43:51\nOUTBOUND\nFDEX\n708135']
output = output[0].split('\n')
output_file = "output_file.csv"
timestamp = self.getTime()
lookAt = ",Robot State: " + ',' + data.data 
create_columns = [timestamp + lookAt]
output_columns = create_columns[0].split(',')       
with open(self.filePath, 'a') as csvfile:
    wr = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)

    
    wr.writerow(output_columns)
with open(output_file, 'ab') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(output)