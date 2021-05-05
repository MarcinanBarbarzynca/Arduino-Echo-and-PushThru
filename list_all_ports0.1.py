
import serial
import time
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

def readData(object): #object type:  object = serial.Serial()
    buffer = ""
    while True:
        oneByte = object.read(1)
        if oneByte == b"\n":    #method should returns bytes #wait for EOL
            return buffer
        else:
            buffer += oneByte.decode("ascii")

print("Dostępne porty com: ")
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

print()
seq = []
for port, desc, hwid in sorted(ports):
        if(port.find("USB")>0 or port.find("COM")>0):
            print("Odnaleziony port COM: "+port)
            ser = serial.Serial(port, 9600, timeout=1,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS)
            print("Otwieram port:")
            #ser.open()
            print("Nadaję wiadomość: ?\\r\\n")
            print(("?\r\n".encode()))
            print("Czekam na odpowiedź")
            ser.write("?\r\n".encode()) #.encode works
            #ser.write(bytes(b"?\r\n")) #bytes() works
            #ser.write("?".encode()) #works too
            #time.sleep(1)
            print(readData(ser))

            ser.close()
