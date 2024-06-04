import time
from datetime import datetime

username = [
    {'nama' : 'Ferran', 'username' : 'rannn', 'password' : 'password'}, 
    {'nama' : 'Andrew', 'username' : 'ndree', 'password' : 'password' },
    {'nama' : 'Kasmal', 'username' : 'mall', 'password' : 'password' }
]

dir = [
    {'time' : '25/08/2023', 'waktu' : '12.30', 'folder' : '<DIR>', 'nama' : 'Pythong'},
    {'time' : '21/05/2023', 'waktu' : '08.57', 'folder' : '     ', 'nama' : 'Lazarus'},
    {'time' : '01/03/2023', 'waktu' : '10.32', 'folder' : '<DIR>', 'nama' : 'Videos'},
    {'time' : '01/03/2023', 'waktu' : '10.32', 'folder' : '<DIR>', 'nama' : 'Photo'},
    {'time' : '01/03/2023', 'waktu' : '10.32', 'folder' : '<DIR>', 'nama' : 'Documents'},
    {'time' : '28/09/2023', 'waktu' : '13.00', 'folder' : '<DIR>', 'nama' : 'Campus'},
    {'time' : '10/05/2023', 'waktu' : '23.23', 'folder' : '<DIR>', 'nama' : 'Job'},
    {'time' : '01/03/2023', 'waktu' : '10.32', 'folder' : '<DIR>', 'nama' : 'Desktop'},
    {'time' : '01/03/2023', 'waktu' : '10.32', 'folder' : '<DIR>', 'nama' : 'Music'},
    {'time' : '01/03/2023', 'waktu' : '10.32', 'folder' : '<DIR>', 'nama' : 'Favorites'}
    ]

dir2 = [
    {'time' : '09/07/2023', 'waktu' : '16.34', 'folder' : '     ', 'nama' : 'DaVinci Resolve.lnk'},
    {'time' : '25/09/2023', 'waktu' : '21.01', 'folder' : '     ', 'nama' : 'Mods'},
    {'time' : '12/07/2023', 'waktu' : '15.22', 'folder' : '     ', 'nama' : 'Spotify'},
    {'time' : '03/04/2023', 'waktu' : '10.35', 'folder' : '     ', 'nama' : 'Zoom'},
]



spes = ['Intel® Desktop Board DH55HC',
        'Leadtek Quadro 315 NVS 512MB DDR3 64 Bit (PCIe x16)',
        'DDR3 4GB PC 1600mhz/1333mhz',
        'Prosesor Intel® Core™ i5-650',
        'Windows 7',
        'SSD WD Green 240GB ',
        ]

def makedir (command,dir_list = dir):
    nama_direktori = command.split(maxsplit=1)[1]
    timing = datetime.now ()
    timing_time = timing.strftime("%H:%M")
    timing = datetime.now ()
    timing_now = timing.strftime("%d/%m/%Y")
    folder = '<DIR>'
    dir_list.append({'time':timing_now,'waktu':timing_time,'folder':folder,'nama':nama_direktori})
    print(f"Direktori berhasil dibuat: {nama_direktori}")

def direc (command,dir_list = dir,dir_list2 = dir2 ):
    if command == 'dir': 
        for item in dir_list:
            values = [f"{value}" for value in item.values()]
            print(" ".join(values), end="\n")
    else:
        nama_direktori = command.split(maxsplit=1)[1]
        if nama_direktori.lower() == "desktop":
            for htem in dir_list2:
                values = [f"{value}" for value in htem.values()]
                print(" ".join(values), end="\n")
        else :
            print ("Parameternya salah")

def remdir (command,dir_list=dir):
    nama_direktori = command.split(maxsplit=1)[1]
    for item in dir_list:
        if item["nama"] == nama_direktori:
            jawaban = input(f"Anda Yakin Ingin Menghapus File {nama_direktori} ? ")
            if jawaban.lower() == "ya":
                dir_list.remove(item)
                print(f"Directory '{nama_direktori}' berhasil di hapus.")
                break  
    else:
        print(f"Directory '{nama_direktori}' tidak di temukan dalam list.")

                

def loading_bar(iterations=50, total=50):
    for i in range(iterations + 1):
        percent = int((i / total) * 100)
        loading_bar_str = f"Progress: [{'=' * i}{' ' * (total - i)}] {percent}%"
        print(loading_bar_str, end='\r')
        time.sleep (0.05)
    print()

def boot_process():
    print("Sistem sedang melakukan proses boot...")
    time.sleep(1)
    print("Sistem Mengecek RAM")
    loading_bar()
    print("Sistem Mengecek ROM")
    loading_bar()
    print("Sistem Mengecek Storage")
    loading_bar()
    print("Sistem Mengecek Mouse")
    loading_bar()
    print("Sistem Mengecek Keyboard")
    loading_bar()
    print("Sistem Mengecek Display")
    loading_bar()
    print("Sistem Mengecek Sistem Operasi")
    loading_bar()
    print("Proses boot selesai.")

def spesifikasi():
    print("Spesifikasi")
    for i in spes:
        print(i)

def login(list1=username):
    print("Ketik 'exit' Jika ingin keluar dari sistem ")
    exit_flag = False  
    user = None

    while not exit_flag:
        username_inp = input("Masukkan Username Anda: ")
        time.sleep(0.1)

        if username_inp.lower() == 'exit':
            exit_flag = True  
            break  

        for user_data in list1:
            if username_inp == user_data['username']:
                while not exit_flag:
                    password_inp = input("Masukkan Password Anda: ")
                    time.sleep(0.1)
                    if password_inp == user_data['password']:
                        print()
                        print(f"Selamat Datang Di Cli, {user_data['nama']}")
                        user = user_data['nama']
                        exit_flag = True  
                    elif password_inp.lower() == 'exit':
                        exit_flag = True  
                        break  
                    else:
                        print("Salah Masukkan Password")
                break 
        else:
            print("Salah Masukkan Username")

    return user

def back(command,awalan,access):
    nama_direktori = command.split(maxsplit=1)[1]
    if nama_direktori == "..":
        if awalan == 0:
            return 1
        elif awalan  == 1: 
            return 2
        else:
            print (f"'{command}' tidak dikenal")
            return awalan
    elif nama_direktori == 'users':
        if awalan == 2:
            return 1
        elif awalan == 1:
            print (f"'{command}' tidak dikenal")
            return 1
        elif awalan == 0:
            print (f"'{command}' tidak dikenal")
            return 0
        elif awalan == 3:
            print (f"'{command}' tidak dikenal")
            return 3
        else:
            print (f"'{command}' tidak dikenal")
            return awalan
    elif nama_direktori == access.lower():
        if awalan == 1:
            return 0
        elif awalan == 2:
            print (f"'{command}' tidak dikenal")
            return 2
        elif awalan == 3:
            print (f"'{command}' tidak dikenal")
            return 3
        else:
            print (f"'{command}' tidak dikenal")
            return awalan
    elif nama_direktori == '':
        print (f"'{nama_direktori}' tidak dikenal")
        return awalan
    else:
        print(f"'{command}' tidak dikenal")
        return awalan  

def switch(command):
    if command == "d:":
        return 3
    elif command == "c:":
        print (f"'{command}' tidak dikenal")
    else:
        print (f"'{command}' tidak dikenal")

def switchB(command):
    if command == "c:":
        return 2
    elif command == "d:":
        print (f"'{command}' tidak dikenal")
    else:
        print (f"'{command}' tidak dikenal")



def clear_screen():
    print("\033c", end="",flush=True)

def timing ():
    timing = datetime.now ()
    timing_time = timing.strftime("%H:%M:%S")
    print ('Waktu Sekarang:',(timing_time))

def waktu ():
    timing = datetime.now ()
    timing_now = timing.strftime("%d/%m/%Y")
    print ('Tanggal Sekarang:',(timing_now))


def shutdown():
    print("Menutup sistem operasi...")
    time.sleep(2)
    print("Sistem telah dimatikan.")

# Mulai nya dari sini
# Proses Booting

clear_screen()
boot_process()
print()

clear_screen()
spesifikasi()

print()
while True: 
    jwb = input ("Masukkan Ingin Login atau Shutdown : ")
    print()
    if jwb.lower() == "login":
        print()
        access = login(username)
        if access:
            awalan = 0
            while True:
                if awalan == 0:
                    os = ("C")
                    user = ("Users")
                    command = input(f"{os}:/{user}/{access}> ")
                elif awalan == 1:
                    os = ("C")
                    user = ("Users")
                    command = input(f"{os}:/{user}> ")
                elif awalan == 2:
                    os = ("C")
                    command = input(f"{os}:/> ")
                elif awalan == 3:
                    os = ("D")
                    command = input(f"{os}:/> ")
                else:
                    print()

                if command.lower() == "log out":
                    break
                elif command.lower() == "date":
                        waktu()
                elif command.lower()=="cls":
                    clear_screen()
                elif command.lower().startswith("dir"):
                    direc(command,dir,dir2)
                elif command.lower().startswith("mkdir"):
                    makedir(command,dir)
                elif command.lower().startswith("rmdir"):
                    remdir(command,dir)
                elif command.lower() =='time':
                    timing()
                elif command.lower() == "d:":
                    awalan = switch(command)
                elif command.lower() == "c:":
                    awalan = switchB(command)
                elif command.lower().startswith("cd"):
                    awalan = back(command,awalan,access)
                elif command.lower() == "help":
                    print("""For more information on a specific command, type HELP command-name
        CLS            Clears the screen.
        DEL            Deletes one or more files.
        DATE           Displays or sets the date.
        DIR            Displays a list of files and subdirectories in a directory.
        EXIT           Quits the CMD.EXE program (command interpreter).
        HELP           Provides Help information for Windows commands.
        RMDIR          Removes a directory.
        TIME           Displays or sets the system time.        
        For more information on tools see the command-line reference in the online help""")
            
                else:
                    print(f"Perintah tidak dikenali: {command}")
                

    elif jwb.lower() =="shutdown":
        break
    else:
        print (f"Perintah Tidak Dikenali")

shutdown()