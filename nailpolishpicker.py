import serial
import time

file_name = "serial.html" # Once created, open this file in a browser.

# Adapt serial port nr. & baud rate to your system.
serial_port = '/dev/cu.usbserial-023E583A'
baudrate = 115200

page_title = "Nail Polish Picker"
button_pressed = False
button_count = 0

def write_page(data_list):
    fo = open(file_name,"w+")
    # Start of HTML page.
    fo.write("<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.01//EN' 'http://www.w3.org/TR/html4/strict.dtd'>")
    fo.write("<html><head><title>"+page_title+"</title>") # Page & Head begin.
    fo.write("<meta http-equiv='refresh' content='1'>")
    fo.write("<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'>")
    fo.write("<link rel='shortcut icon' href='favicon.ico' />")
    fo.write("<link rel='icon' type='image/x-icon' href='favicon.ico' />")
    fo.write("<link rel='icon' type='image/png' href='favicon.png' />")
    fo.write("</head><body><center><p>"+page_title+"</p>") # Head end, body begin.

    # Table begin.
    #fo.write("<table border='1' border-spacing='5' style='text-align:center;'>")
    #for i in range(0,len(data_list),2):
    #fo.write("<td>"+str(button_count)+"</td>") # Table column 1.
    img_url = "/Users/Anvi/Downloads/redlicorice.jpeg"
    if (int(button_count)/2 % 7 == 0):
        img_url = "/Users/Anvi/Downloads/redlicorice.jpeg"
    if (int(button_count)/2 % 7 == 1):
        img_url = "/Users/Anvi/Downloads/orangedrink.jpeg"
    if (int(button_count)/2 % 7 == 2):
        img_url = "/Users/Anvi/Downloads/lemonsucker.jpeg"
    if (int(button_count)/2 % 7 == 3):
        img_url = "/Users/Anvi/Downloads/greentaffy.jpeg"
    if (int(button_count)/2 % 7 == 4):
        img_url = "/Users/Anvi/Downloads/bluefreezie.jpeg"
    if (int(button_count)/2 % 7 == 5):
        img_url = "/Users/Anvi/Downloads/purpleslushie.jpeg"
    if (int(button_count)/2 % 7 == 6):
        img_url = "/Users/Anvi/Downloads/magentajelly.jpeg"
    fo.write("<td>"+ "<img src=" + img_url + ">"+"</td>")
    fo.write("</html>") # Page end.
    # Done, close file.
    fo.close()

s = serial.Serial(serial_port,baudrate) # Open serial port.
s.dtr = 0 # Reset Arduino.
s.dtr = 1
print("Waiting for data...")
time.sleep(2) # Wait for Arduino to finish booting.
s.reset_input_buffer() # Delete any stale data.

while 1:
    write_page(0)
    data_str = s.readline().decode() # Read data & convert bytes to string type.
    data_str = data_str.replace(' ','') # Remove whitespace.
    data_str = data_str.replace('\r','') # Remove return.
    data_str = data_str.replace('\n','') # Remove new line.
    button_count = data_str
    print(data_str)
    write_page(data_str)