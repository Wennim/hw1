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
       if row["TEMP"] != '-99.000' or row["TEMP"] != '-999.000':
           
        
            data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
C0A880_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
C0F9A0_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
C0G640_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
C0R190_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
C0X260_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

C0A880_data=sorted(C0A880_data,key= lambda k:k["TEMP"],reverse= True )
C0F9A0_data=sorted(C0F9A0_data,key= lambda k:k["TEMP"],reverse= True )
C0G640_data=sorted(C0G640_data,key= lambda k:k["TEMP"],reverse= True )
C0R190_data=sorted(C0R190_data,key= lambda k:k["TEMP"],reverse= True )
C0X260_data=sorted(C0X260_data,key= lambda k:k["TEMP"],reverse= True )

target_data=[]
target_data.append([C0A880_data[0]["station_id"],C0A880_data[0]["TEMP"]])
target_data.append([C0F9A0_data[0]["station_id"],C0F9A0_data[0]["TEMP"]])
target_data.append([C0G640_data[0]["station_id"],C0G640_data[0]["TEMP"]])
target_data.append([C0R190_data[0]["station_id"],C0R190_data[0]["TEMP"]])
target_data.append([C0X260_data[0]["station_id"],C0X260_data[0]["TEMP"]])

# Retrive ten data points from the beginning.


#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================