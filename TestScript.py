import pyads

# connect to plc and open connection
plc = pyads.Connection('127.0.0.1.1.1', pyads.PORT_TC3PLC1)
plc.open()

for i in range(5):
    val1 = plc.read_by_name("MAIN.fValue")   # read current variable value
    val2 = plc.read_by_name("MAIN.nValue")   # read current variable value
    print(val1) # print value
    print(val2) # print value

    plc.write_by_name("MAIN.fValue", val1+1)     # increment value and write it back to PLC
    plc.write_by_name("MAIN.nValue", val2+1)     # increment value and write it back to PLC

# close connection
plc.close()

print('Press enter to leave application')
input()