# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108000164.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
        if row["TEMP"] != '-99.000' and row["TEMP"] != '-999.000':
            data.append(row)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.

station_data=[]
for station in ['C0A880','C0F9A0','C0G640','C0R190','C0X260']:
  station_data.append(list(filter(lambda item: item['station_id'] == station, data)))
  

for i in range(5) :
  station_data[i]=sorted(station_data[i],key= lambda k:k["TEMP"],reverse= True )

target_data=[]
for i in range(5) :
  target_data.append([station_data[i][0]["station_id"],station_data[i][0]["TEMP"]])

#=======================================
# Part. 4
#=======================================
# Print result
print(target_data)
#========================================