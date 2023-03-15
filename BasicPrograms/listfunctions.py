series=["Breaking Bad","Game Of Throneas","Sherlock","Peaky Blinders","Daredevil"]
rankings=[1,2,3,4,5]
print(rankings)
series.extend(rankings)         #extend function

print(series)

series.append("The Walking Dead")   #append functoin
print(series)

rankings.insert(3,"new")            #insert function
print(rankings)

series.remove("Peaky Blinders")    #remove functions
print(series)