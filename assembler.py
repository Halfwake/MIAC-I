import sys

if len(sys.argv) != 2:
    print "Invalid amount of arguments!"

file_name = sys.argv[1]
file_obj = open(file_name, "w")

while True:
    try: data = input()
    except: break
    data = chr(data)
    file_obj.write(data)

file_obj.close()
