#Modules
from os import system
import time
import datetime

#ClearFunction
clear = lambda: system('clear')

#TimeFunction
def Time(t):
    time.sleep(t)

#SpaceFunction
def Space():
    print("")

#LoadingFunction
def Load(Text):
    Controller = 0

    def Loading(t):
        print(t)

        Time(0.15)

        clear()
        print(t + ".")

        Time(0.15)

        clear()
        print(t + "..")

        Time(0.15)

        clear()
        print(t + "...")

        Time(0.2)

        clear()

    clear()
    while Controller <= 3:
        Loading(Text)
        Controller += 1
        if Controller == 3:
            break

#Dates
CallDate = datetime.datetime.now()
Date = CallDate.strftime("%d")
Month = CallDate.strftime("%m")
Year = CallDate.strftime("%Y")
DateNow = Year + "-" + Month + "-" + Date

#Data
AllData = []
DatesData = []
Indicator = []
MeetData = []
ZoomData = []

#LoadAllData
with open('AllData.txt', 'r') as filehandle:
    AllData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadDatesData
with open('DatesData.txt', 'r') as filehandle:
    DatesData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadIndicator
with open('Indicator.txt', 'r') as filehandle:
    Indicator = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadMeetData
with open('MeetData.txt', 'r') as filehandle:
    MeetData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadZoomData
with open('ZoomData.txt', 'r') as filehandle:
    ZoomData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#System
def System():
    #Sections
    Section = int(0)
     #Section 0 = Menu Utama
     #Section 1 = Penghitung Kuota
     #Section 2 = Data Pemakaian
     #Section 3 = Tentang
     #Section 4 = Keluar

    #MainMenu
    print(f"{'KUOTER' : ^60}")
    print(f"{'--- Kuota Belajar ---' : ^61}")
    print("""
   1. Penghitung Kuota
   2. Data Pemakaian 
   3. Tentang
   4. Keluar
   """)
    MainChoice = int(
        input("   Ketik angka dan Enter untuk melanjutkan (1/2/3/4): "))

    #MainChoice
    if MainChoice == 1:
        Section = int(1)
        clear()
    elif MainChoice == 2:
        Section = int(2)
        clear()
    elif MainChoice == 3:
        Section = int(3)
        clear()
    elif MainChoice == 4:
        Section = int(4)
        clear()
    else:
        print("   Pilihan tidak valid, silahkan coba lagi.")
        Time(1)
        clear()
        System()

 #Section1

    def Section1():
        #Title
        def Title():
            print(f"{'PENGHITUNG KUOTA' : ^60}")
            Space()

    #Parameters
        Platform = int(0)
         #Platform 0 = Zoom
         #Platform 1 = Google Meet
        Device = int(0)
         #Device 0 = Desktop
         #Device 1 = Mobile
        Camera = int(0)
         #Camera 0 = No Camera (Audio Only)
         #Camera 1 = With Camera
        Resolution = int(0)
         #Resolution 0 = SD Camera
         #Resolution 1 = HD Camera
        ScreenShare = int(0)
         #ScreenShare 0 = No Screenshare
         #ScreenShare 1 = With Screenshare

        #DataInput
        VD = float(0)
        AD = float(0)
        SS = float(0)

        #Platform
        Title()
        print("   Pilih platform yang anda gunakan selama menjalani PJJ")
        print(""" 
       1. Zoom 
       2. Google Meet
       """)
        PlatformChoice = int(
            input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

        #PlatformChoice
        if PlatformChoice == 1:
            clear()
            P = " Zoom"
        elif PlatformChoice == 2:
            Platform = int(1)
            clear()
            P = " Meet"
        else:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section1()

        #Device
        Title()
        print("   Pilih versi device yang dijalankan platform" + P)
        print(""" 
       1. Desktop 
       2. Mobile
      """)
        DeviceChoice = int(
            input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

        #DeviceChoice
        if DeviceChoice == 1:
            clear()
        elif DeviceChoice == 2:
            Device = int(1)
            clear()
        else:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section1()

        #Camera
        Title()
        print("   Apakah anda menggunakan kamera?")
        print(""" 
       1. Tidak (Hanya Audio) 
       2. Iya
      """)
        CameraChoice = int(
            input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

        #CameraChoice
        if CameraChoice == 1:
            clear()
        elif CameraChoice == 2:
            Camera = int(1)
            clear()
        else:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section1()

        #Resolution
        Title()
        if Camera == 1 and Device == 0:
            print("   Pilih resolusi kamera anda")
            print(""" 
       1. SD (Standard Definition) 
       2. HD (High Defintion)
       """)
            ResolutionChoice = int(
                input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

            #ResolutionChoice
            if ResolutionChoice == 1:
                clear()
            elif ResolutionChoice == 2:
                Resolution = int(1)
                clear()
            else:
                print("   Pilihan tidak valid, silahkan coba lagi.")
                Time(1)
                clear()
                Section1()

        #ScreenShare
        clear()
        Title()
        print("   Apakah anda menggunakan fitur share screen?")
        print(""" 
       1. Tidak 
       2. Iya
      """)
        ScreenShareChoice = int(
            input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

        #ScreenShareChoice
        if ScreenShareChoice == 1:
            clear()
        elif ScreenShareChoice == 2:
            ScreenShare = int(1)
            clear()
        else:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section1()

        #Time
        Title()
        print("   Berapa lama waktu yang digunakan dalam platform" + P + "?")
        Space()
        WaktuPemakaian = int(
            input("   Masukkan angka dan Enter untuk melanjutkan (Jam): "))

        #TimeChoice
        if WaktuPemakaian == 0:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section1()

        #Participant
        clear()
        Title()
        print("   Berapa banyak peserta yang ada dalam platform" + P + "?")
        Space()
        JumlahPeserta = int(
            input("   Masukkan angka dan Enter untuk melanjutkan (Orang): "))

        #ParticipantChoice
        if JumlahPeserta == 0:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section1()

    #Combination
        #ZoomSD
        if JumlahPeserta <= 10 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.540)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.675)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.810)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.945)
        if JumlahPeserta >= 41 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(1.080)

        #ZoomSD + ScreenShare
        if JumlahPeserta <= 10 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.540)
            SS += float(0.045)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.675)
            SS += float(0.045)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.810)
            SS += float(0.045)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.945)
            SS += float(0.045)
        if JumlahPeserta >= 41 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(1.080)
            SS += float(0.045)

        #ZoomHD
        if JumlahPeserta <= 10 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.080)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.215)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.350)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.485)
        if JumlahPeserta >= 41 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.620)

        #ZoomHD + ScreenShare
        if JumlahPeserta <= 10 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.080)
            SS += float(0.045)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.215)
            SS += float(0.045)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.350)
            SS += float(0.045)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.485)
            SS += float(0.045)
        if JumlahPeserta >= 41 and Platform == 0 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.620)
            SS += float(0.045)

        #ZoomMobile
        if JumlahPeserta <= 10 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.270)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.337)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.405)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.472)
        if JumlahPeserta >= 41 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.540)

        #ZoomMobile + ScreenShare
        if JumlahPeserta <= 10 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.270)
            SS += float(0.045)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.337)
            SS += float(0.045)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.405)
            SS += float(0.045)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.472)
            SS += float(0.045)
        if JumlahPeserta >= 41 and Platform == 0 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.540)
            SS += float(0.045)

        #MeetSD
        if JumlahPeserta <= 10 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.135)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.270)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.405)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.540)
        if JumlahPeserta >= 41 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 0:
            VD += float(0.675)

        #MeetSD + ScreenShare
        if JumlahPeserta <= 10 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.135)
            SS += float(0.045)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.270)
            SS += float(0.045)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.405)
            SS += float(0.045)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.540)
            SS += float(0.045)
        if JumlahPeserta >= 41 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 0 and ScreenShare == 1:
            VD += float(0.675)
            SS += float(0.045)

        #MeetHD
        if JumlahPeserta <= 10 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.170)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.305)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.440)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.575)
        if JumlahPeserta >= 41 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 0:
            VD += float(1.710)

        #MeetHD + ScreenShare
        if JumlahPeserta <= 10 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.170)
            SS += float(0.045)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.305)
            SS += float(0.045)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.440)
            SS += float(0.045)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.575)
            SS += float(0.045)
        if JumlahPeserta >= 41 and Platform == 1 and Device == 0 and Camera == 1 and Resolution == 1 and ScreenShare == 1:
            VD += float(1.710)
            SS += float(0.045)

        #MeetMobile
        if JumlahPeserta <= 10 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.067)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.101)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.135)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.168)
        if JumlahPeserta >= 41 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 0:
            VD += float(0.202)

        #MeetMobile + ScreenShare
        if JumlahPeserta <= 10 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.067)
            SS += float(0.045)
        if JumlahPeserta >= 11 and JumlahPeserta <= 20 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.101)
            SS += float(0.045)
        if JumlahPeserta >= 21 and JumlahPeserta <= 30 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.135)
            SS += float(0.045)
        if JumlahPeserta >= 31 and JumlahPeserta <= 40 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.168)
            SS += float(0.045)
        if JumlahPeserta >= 41 and Platform == 1 and Device == 1 and Camera == 1 and ScreenShare == 1:
            VD += float(0.202)
            SS += float(0.045)

        #Audio
        if JumlahPeserta >= 0 and Camera == 0 and ScreenShare == 0:
            AD += float(0.032)

        #Audio + ScreenShare
        if JumlahPeserta >= 0 and Camera == 0 and ScreenShare == 1:
            AD += float(0.032)
            SS += float(0.045)

        #Function
        T = lambda t, v, a, s: t * (v + a + s)

        #Process
        HasilKuota = float(T(WaktuPemakaian, VD, AD, SS))
        KonversiKuota = round(HasilKuota, 2)
        PenggunaanKuota = str(KonversiKuota) + "GB"

        #OutputData
        if Platform == 0:
            ZoomData.append(PenggunaanKuota)
            AllData.append(KonversiKuota)
            MeetData.append("-")
            DatesData.append(DateNow)
            Indicator.append("X")
        elif Platform == 1:
            MeetData.append("        " + PenggunaanKuota)
            AllData.append(KonversiKuota)
            ZoomData.append("  -")
            DatesData.append(DateNow)
            Indicator.append("X")

        #SaveAllData
        with open('AllData.txt', 'w') as filehandle:
            for Data in AllData:
                filehandle.write('%s\n' % Data)

        #SaveDatesData
        with open('DatesData.txt', 'w') as filehandle:
            for Data in DatesData:
                filehandle.write('%s\n' % Data)

        #SaveIndicator
        with open('Indicator.txt', 'w') as filehandle:
            for Data in Indicator:
                filehandle.write('%s\n' % Data)

        #SaveMeetData
        with open('MeetData.txt', 'w') as filehandle:
            for Data in MeetData:
                filehandle.write('%s\n' % Data)

        #SaveZoomData
        with open('ZoomData.txt', 'w') as filehandle:
            for Data in ZoomData:
                filehandle.write('%s\n' % Data)

        #Intermission
        Load("Memproses Data")

        #Result
        clear()
        Title()
        print("   Kuota yang anda gunakan sebesar " + PenggunaanKuota +
              " / Hari")
        Space()

        #Recommendation
        print("   Rekomendasi jumlah kuota:")

        if KonversiKuota <= float(1):
            print("   30GB / Bulan")
        elif KonversiKuota >= float(1) and KonversiKuota <= float(5):
            print("   60GB / Bulan")
        elif KonversiKuota >= float(5) and KonversiKuota <= float(10):
            print("   120GB / Bulan")
        elif KonversiKuota >= float(10) and KonversiKuota <= float(15):
            print("   120GB / Bulan")
        elif KonversiKuota >= float(15):
            print("   Maaf, belum ada rekomendasi untukmu.")

        #Final
        Space()
        print("   Ingin menghitung kembali?")
        print("""
      1. Iya
      2. Tidak
      """)
        FinalChoice = int(
            input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

        #FinalChoice
        if FinalChoice == 1:
            clear()
            Section1()
        elif FinalChoice == 2:
            clear()
            System()
        else:
            print("   Pilihan tidak valid. Kembali ke Menu Utama")
            Time(2)
            clear()
            System()

 #Section2

    def Section2():
        #Intermission
        if "X" in Indicator:
            Load("Mengambil Data")
        else:
            clear()

        #Title
        print(f"{'DATA PEMAKAIAN' : ^60}")
        Space()

        #TableName
        print(f"{'Tanggal' : ^28}{'Zoom' : ^1}{'Meet' : ^28}")
        print(f"{'_______________________________________________' : ^60}")

        #TableContents
        if "X" in Indicator:
            for data in range(0, len(Indicator)):
                print(
                    f"{DatesData[data] : ^28}{ZoomData[data] : ^1}{MeetData[data] : ^25}"
                )
                Space()
        else:
            print(f"{'Belum ada data yang dimasukkan' : ^60}")
            Space()

        #Note
        Space()
        if "X" in Indicator:
          print("      *Note: 1GB = 1000MB*")
        Space()

        #Back
        Back = input("      Tekan Enter untuk kembali ke Menu Utama ")
        clear()
        System()

 #Section3

    def Section3():
        #Title
        print(f"{'TENTANG' : ^60}")
        Space()

        #Developer
        print("   Dibuat oleh Melvin Tungadi")
        Space()

        #Description
        print("   Deskripsi:")
        print("""
   "Aplikasi penghitung kuota untuk membantu
   keberlangsungan pembelajaran jarak jauh."

   Selama #DiRumahAja segalanya dilakukan
   menggunakan internet, termasuk kegiatan
   belajar mengajar. Bicara tentang internet
   tidak lepas dari penggunaan kuota.
   Terkadang, kuota kita tidak cukup dengan
   penggunaan kita sehingga kegiatan belajar
   mengajar menjadi tersendat. Dengan aplikasi
   ini, diharapkan anda bisa mengetahui penggunaan
   kuota anda melalui platform Zoom & Google Meet
   sehingga bisa memilih jumlah kuota yang pas
   sesuai dengan kebutuhan.
        """)

        #References
        print("   Sumber Referensi:")
        print("""   https://tinyurl.com/GoogleUsage
   https://tinyurl.com/ZoomUsage
   https://www.w3schools.com/
        """)
        Space()

        #Footer
        print("   V. 1.0.")
        print("   © Copyright 2021")
        Space()

        #Back
        Back = input("   Tekan Enter untuk kembali ke Menu Utama ")
        clear()
        System()

 #Section4

    def Section4():
        #ConfirmationInfo
        print("   Apakah anda ingin keluar?")
        print("""
     1. Iya
     2. Tidak
     """)

        #Confirmation
        Confirmation = int(
            input("   Ketik angka dan Enter untuk melanjutkan (1/2): "))

        if Confirmation == 1:
            clear()
            print("Terima kasih telah menggunakan!")
            Time(2)
            clear()
        elif Confirmation == 2:
            clear()
            System()
        else:
            print("   Pilihan tidak valid, silahkan coba lagi.")
            Time(1)
            clear()
            Section4()

 #MainConditions

    while Section == 1:
        Section1()
        break
    while Section == 2:
        Section2()
        break
    while Section == 3:
        Section3()
        break
    while Section == 4:
        Section4()
        break

#Excecute
System()