##Program Name:      MySorter.py
##Program Language:  Python
##Language Version:  2.7.9
##Platform Tested:   Windows 8.1, x86(32bit)
##Author:            Matt Kozlowski
##Date Created:      10/01/16


def outputDisplay():                                              # Define print sorted list function
   print("Beauty Out:")
   print(sortData)                                                
   print("")

def kozmoSorter(sortData):                                        # Define Sorter function
   x=0
   y=0
   print("Garbage In:")
   print(sortData)
   for fillslot in range(len(sortData)-1,((len(sortData)-1)/2),-1): # Set range for fillslot from end of sort data list to midpoint, decrement by 1
       positionOfMax=0
       positionOfMin=x                                            # Set FillSlotMin(x) = first position in list
       for location in range(x,fillslot+1):                       # Set comparison data range between fillSlotMin(x) and fillSlot
            if fillslot>=((len(sortData))/2):
                 if sortData[location]>sortData[positionOfMax]:   # Check if current location greater than positionofMax, if y, move flag to current pos
                     positionOfMax = location
            if x<=((len(sortData))/2):                            # Check if current location less than positionOfMin, if y, move flag to current pos
                 if sortData[location]< sortData[positionOfMin]:
                     positionOfMin = location                              
       if fillslot>=((len(sortData)/2)):                          # Swap values between fillslot and position of max,
                if fillslot!=positionOfMin:                       # Unless the fillslot location is flagged as positionOfMin
                   temp = sortData[fillslot]
                   sortData[fillslot] = sortData[positionOfMax]
                   sortData[positionOfMax] = temp
                if fillslot==positionOfMin:                       # If fillslot (max) is flagged as positionOfMin, set flag y = 1
                   y=1                                    
       if x<=((len(sortData)/2)):
            if y==1:                                              # If y is flagged true, swap values of positionOfMax and fillslotMin(x)
                temp1=sortData[x]
                sortData[x]=sortData[positionOfMax]
                sortData[positionOfMax]=temp1
                y=0
            temp1 = sortData[x]                                   # Otherwise swap values of positionOfMin and fillslotMin(x)
            sortData[x]=sortData[positionOfMin]
            sortData[positionOfMin]=temp1            
       x += 1                                                     # Increment fillslotMin(x) by 1 each time fillslot is decremented by 1.

          

sortData = [67, 45, 2, 13, 1, 998]
kozmoSorter(sortData)                                             # Call the sorter function kozmoSorter!
outputDisplay()
sortData = [89, 23, 33, 45, 10, 12, 45, 45, 45]
kozmoSorter(sortData)
outputDisplay()
