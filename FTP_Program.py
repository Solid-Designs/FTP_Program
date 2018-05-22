from ftplib import FTP
import socket


class ServerInfo:
    def __init__(self):
        print('Welcome to the FTP program. \n')
        while True:  # Request server location from input
            self.input_location = str(input('Input Server Location: '))
            try:
                self.server_location = FTP(self.input_location)
                break
            except socket.gaierror:
                print('error')

        self.server_location.login()  # Login to server. Username and password checking coming soon.
        while True:  # Request grab or place file
            self.input_grab_place = input('Would you like to grab or place a file?'
                                          '\nPress G to grab\nPress P to place\nEnter the corresponding key: ').upper()

            if self.input_grab_place == 'G':
                self.grab_file()
                break
            elif self.input_grab_place == 'P':
                self.place_file()
                break
            else:
                print('Invalid input. Please try again')

    def grab_file(self):
        print(self.server_location.dir())

    def place_file(self):
        print('Placed')


my_server = ServerInfo()

# ftp = FTP('ftp.sunet.se')
# ftp.login()
#
# print(ftp.getwelcome())
#
# files = ftp.dir()
# print(files)
#
#
# def grab_file():
#     file_name = 'favicon.ico'
#     local_file = open(r'C:\Users\Administrator.Christopher-PC\Desktop\Sticky Notes\'' + file_name, 'wb')
#
#     # def custom_write(line):
#        # local_file.write(line + '\n')
#
#     ftp.retrbinary('RETR ' + file_name, local_file.write)
#     ftp.quit()
#     local_file.close()
#
#
# def place_file():
#     file_name = 'filename.txt'
#     ftp.storbinary('STOR ' + file_name, open(file_name, 'rb'))
#     ftp.quit()
#
#
# grab_file()

