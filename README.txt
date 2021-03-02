 (1) how to setup and run your program 
 
 根據老師所給的範例程式：
  在part 2那裏讀進了csv檔的資料，然後remove在TEMP有'-99.000' and'-999.000'的資料：
  for row in mycsv:
        if row["TEMP"] != '-99.000' and row["TEMP"] != '-999.000':
            data.append(row)


然後在part 3對資料進行分析和整理:
我把每個“station_id”放進id的list裏面：
id=['C0A880','C0F9A0','C0G640','C0R190','C0X260']


再把csv的資料過濾，只將那五個的station的資料append進station_data:
for station in id :
  station_data.append(list(filter(lambda item: item['station_id'] == station, data)))
  
將station_data裏的‘TEMP"做大到小的排序：
for i in range(5) :
  station_data[i]=sorted(station_data[i],key= lambda k:k["TEMP"],reverse= True )

接著append每個station的名字和"TEMP"的第一個數據（也就是最大的）給target_data。如果該站的“TEMP"數據全是'-99.000'/'-999.000',在part 3的第一個for就沒有進到該站的數據，所以程式會跑不到，因爲list不存在。所以我用try and except的方法，讓run 不到的程式append"TEMP"為None的結果。：
target_data=[]
for i in range(5) :
  try: target_data.append([id[i],station_data[i][0]["TEMP"]])

  except :target_data.append([id[i],'None'])
  
  part 4 就print出結果：
  print(target_data)
  
  (2) what are the results
  108000164.csv的結果爲 [['C0A880', '22.000'], ['C0F9A0', '22.700'], ['C0G640', '24.700'], ['C0R190', '26.400'], ['C0X260', '24.400']]
