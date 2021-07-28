#Modules
from os import system
import time
import datetime

#ClearFunction
clear = lambda: system("cls")

#WaitFunction
def wait(number):
    time.sleep(number)

#SpaceFunction
def space():
    print("")

#BackFunction
def back(space,text):
    input(space + text)
    clear()
    mainSystem()
    
#ErrorFunction
def error(text):
    print("   " + text)
    wait(1)
    clear()

#SaveFunction
def saveData():
    #SaveAllData
        with open("data/AllData.txt", "w") as filehandle:
            for Data in AllData:
                filehandle.write("%s\n" % Data)

        #SaveDatesData
        with open("data/DatesData.txt", "w") as filehandle:
            for Data in DatesData:
                filehandle.write("%s\n" % Data)

        #SaveIndicator
        with open("data/Indicator.txt", "w") as filehandle:
            for Data in Indicator:
                filehandle.write("%s\n" % Data)

        #SaveMeetData
        with open("data/MeetData.txt", "w") as filehandle:
            for Data in MeetData:
                filehandle.write("%s\n" % Data)

        #SaveYoutubeData
        with open("data/YoutubeData.txt", "w") as filehandle:
            for Data in YoutubeData:
                filehandle.write("%s\n" % Data)

        #SaveZoomData
        with open("data/ZoomData.txt", "w") as filehandle:
            for Data in ZoomData:
                filehandle.write("%s\n" % Data)

#LoadingFunction
def load(text):
    controller = 0

    def loading(t):
        print(t)
        wait(0.1)
        clear()
        print(t + ".")
        wait(0.1)
        clear()
        print(t + "..")
        wait(0.1)
        clear()
        print(t + "...")
        wait(0.1)
        clear()

    clear()
    while controller <= 2:
        loading(text)
        controller += 1
        if controller == 2:
            break

#Dates
callDate = datetime.datetime.now()
date = callDate.strftime("%d")
month = callDate.strftime("%m")
year = callDate.strftime("%Y")
DateNow = year + "-" + month + "-" + date

#GlobalData
AllData = []
DatesData = []
Indicator = []
LanguageIndicator = []
MeetData = []
YoutubeData = []
ZoomData = []

#LoadAllData
with open("data/AllData.txt", "r") as filehandle:
    AllData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadDatesData
with open("data/DatesData.txt", "r") as filehandle:
    DatesData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadIndicator
with open("data/Indicator.txt", "r") as filehandle:
    Indicator = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadLanguageIndicator
with open("data/LanguageIndicator.txt", "r") as filehandle:
    LanguageIndicator = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadMeetData
with open("data/MeetData.txt", "r") as filehandle:
    MeetData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#LoadYoutubeData
with open("data/YoutubeData.txt", "r") as filehandle:
    YoutubeData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]
    
#LoadZoomData
with open("data/ZoomData.txt", "r") as filehandle:
    ZoomData = [
        current_data.rstrip() for current_data in filehandle.readlines()
    ]

#System
def mainSystem():
    #Sections
    Section = int(0)
       #Section 0 = Menu Utama / Main Menu
       #Section 1 = Penghitung Kuota / Data Calculator
       #Section 2 = Data Pemakaian / History
       #Section 3 = Tentang / About
       #Section 4 = Bahasa / Language
       #Section 5 = Reset Data
       #Section 6 = Keluar / Exit

    #Language
    if "English" in LanguageIndicator:
        menuText = """
   1. Data Calculator
   2. History
   3. About
   4. Language
   5. Reset History
   6. Exit
   """
        mainInputText = "Type the number and press Enter to continue "
        userInputText = "Type a number and press Enter to continue "
        hourText = "(Hour): "
        peopleText = "(People): "
        errorText = "Your input is invalid, please try again."
        errorMainText = "Your input is invalid, going back to Main Menu."
        backText = "Press Enter to go back to Main Menu."
        processText = "Processing"
        resetText = "Resetting"
        loadText = "Loading"
        section1Title = "DATA CALCULATOR"
        section2Title = "HISTORY"
        section3Title = "ABOUT"
        section4Title = "LANGUAGE"
        platformText = "Choose your platform:"
        deviceText = "Choose your device:"
        cameraText = "Is the camera enabled?:"
        yesNoText = """ 
       1. Yes 
       2. No
       """
        resolutionText = "Select your camera's resolution:"
        screenShareText = "Are you using the Share Screen feature?:"
        qualityText = "Choose your prefered video quality:"
        timeText = "How many hours did you spend on"
        participantText = "How many participants are there on your"
        resultTextFront = "Your data usage is "
        resultTextBack = " / Day"
        estimationText = "Estimated amount of data plan required:"
        estimationTextMonth = " / Month"
        estimationTextLimit = "Sorry, there are no choices for you yet."
        finalText = "Want to calculate again?"
        tableNameDate = "Date"
        tableContentsText = "No data has been entered yet."
        backText = "Press Enter to go back to Main Menu."
        developerText = "Made By Melvin Tungadi"
        infoText = """
   This is just a personal project to experiment
   with programming, all of the data shown in the 
   program is just an estimate and not an accurate
   result.
        
   *Don't take all of the results and recommendations
    as a real huide
        
   Thank you for trying this program!
   """
        referencesTitleText = "References:"
        languageText = "Select your prefered language:"
        languageChoiceText = """
   1. English
   2. Bahasa Indonesia
   """
        resetQuestionText = "Do you want to reset your history data?"
        resetConfirmationText = "Data has been reset."
        exitText = "Do you want to exit?"
        confirmationText = "Thank you for using!"
        
    else:
        menuText = """
   1. Penghitung Kuota
   2. Data Pemakaian
   3. Tentang
   4. Bahasa
   5. Reset Data Pemakaian
   6. Keluar
   """
        mainInputText = "Ketik angka dan tekan Enter untuk melanjutkan "
        userInputText = "Masukkan angka dan tekan Enter untuk melanjutkan "
        hourText = "(Jam): "
        peopleText = "(Orang): "
        errorText = "Pilihan anda tidak valid, silahkan coba lagi."
        errorMainText = "Pilihan anda tidak valid, kembali ke Menu Utama."
        backText = "Tekan Enter untuk kembali ke Menu Utama."
        processText = "Memproses Data"
        resetText = "Mereset Data"
        loadText = "Mengambil Data"
        section1Title = "PENGHITUNG KUOTA"
        section2Title = "DATA PEMAKAIAN"
        section3Title = "TENTANG"
        section4Title = "BAHASA"
        platformText = "Pilih platform anda:"
        deviceText = "Pilih device anda:"
        cameraText = "Apakah anda menggunakan kamera?:"
        yesNoText = """ 
       1. Iya 
       2. Tidak
   """
        resolutionText = "Pilih resolusi kamera anda:"
        screenShareText = "Apakah anda menggunakan fitur Share Sceen?:"
        qualityText = "Pilih preferensi kualitas video anda:"
        timeText = "Berapa lama waktu yang digunakan dalam platform"
        participantText = "Berapa banyak peserta yang ada dalam platform"
        resultTextFront = "Kuota yang anda gunakan sebesar "
        resultTextBack = " / Hari"
        estimationText = "Perkiraan jumlah kuota yang dibutuhkan:"
        estimationTextMonth = " / Bulan"
        estimationTextLimit = "Maaf, belum ada pilihan untukmu."
        finalText = "Ingin menghitung kembali?"
        tableNameDate = "Tanggal"
        tableContentsText = "Belum ada data yang dimasukkan."
        developerText = "Dibuat oleh Melvin Tungadi"
        infoText = """
   Sebuah proyek pribadi untuk bereksperimen dengan
   programming, semua data yang ditampilan dalam
   program hanyalah perkiraan dan bukan hasil yang
   akurat.
        
   *Jangan mengambil semua hasil dan rekomendasi
    sebagai panduan nyata.
        
   Terima kasih telah mencoba program ini!
   """
        referencesTitleText = "Referensi:"
        languageText = "Pilih preferensi bahasa:"
        languageChoiceText = """
   1. Bahasa Inggris
   2. Bahasa Indonesia
   """
        resetQuestionText = "Apakah anda ingin mereset data pemakaian anda?"
        resetConfirmationText = "Data Pemakaian telah direset."
        exitText = "Apakah anda ingin keluar?"
        confirmationText = "Terima kasih telah menggunakan!"        
        
    #MainMenu
    print(f"{'KUOTER' : ^60}")
    print(f"{'--- Kuota Meter ---' : ^61}")
    print(menuText)
    MainChoice = str(input("   " + mainInputText + "(1/2/3/4/5/6): "))
        
    #MainChoice
    if MainChoice == "1":
        Section = int(1)
        clear()
    elif MainChoice == "2":
        Section = int(2)
        clear()
    elif MainChoice == "3":
        Section = int(3)
        clear()
    elif MainChoice == "4":
        Section = int(4)
        clear()
    elif MainChoice == "5":
        Section = int(5)
        clear()
    elif MainChoice == "6":
        Section = int(6)
        clear()

    else:
        error(errorText)
        mainSystem()

    #Section1
    def section1():
        #Title
        def title():
            print(f"{section1Title : ^60}")
            space()

        #InputValues
        Platform = int(0)
           #Platform 0 = Zoom
           #Platform 1 = Google Meet
           #Platform 2 = Youtube
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
        YT = float(0)

        #Platform
        title()
        print("   " + platformText)
        print(""" 
       1. Zoom 
       2. Google Meet
       3. Youtube
       """)
        print("   " + backText)
        space()
        PlatformChoice = str(input("   " + mainInputText + "(1/2/3): "))

        #PlatformChoice
        if PlatformChoice == "1":
            P = " Zoom"
            clear()
            
        elif PlatformChoice == "2":
            Platform = int(1)
            P = " Google Meet"
            clear()
            
        elif PlatformChoice == "3":
            Platform = int(2)
            P = " Youtube"
            clear()
            
        elif PlatformChoice == "":
            clear()
            mainSystem()
            
        else:
            error(errorText)
            section1()

        #Device
        if Platform == 0 or Platform == 1:
            title()
            print("   " + deviceText)
            print(""" 
       1. Desktop 
       2. Mobile
      """)
            DeviceChoice = str(input("   " + mainInputText + "(1/2): "))

            #DeviceChoice
            if DeviceChoice == "1":
                clear()
            
            elif DeviceChoice == "2":
                Device = int(1)
                clear()
            
            else:
                error(errorText)
                section1()

        #Camera
        if Platform == 0 or Platform == 1:
            title()
            print("   " + cameraText)
            print(yesNoText)
            CameraChoice = str(input("   " + mainInputText + "(1/2): "))

            #CameraChoice          
            if CameraChoice == "1":
                Camera = int(1)
                clear()
                
            elif CameraChoice == "2":
                clear()    
            
            else:
                error(errorText)
                section1()

        #Resolution
        if Camera == 1 and Device == 0:
            title()
            print("   " + resolutionText)
            print(""" 
       1. SD (Standard Definition) 
       2. HD (High Defintion)
       """)
            ResolutionChoice = str(input("   " + mainInputText + "(1/2): "))

            #ResolutionChoice
            if ResolutionChoice == "1":               
                clear()

            elif ResolutionChoice == "2":
                Resolution = int(1)
                clear()

            else:
                error(errorText)
                section1()

        #ScreenShare
        if Platform == 0 or Platform == 1:        
            title()
            print("   " + screenShareText)
            print(yesNoText)
            ScreenShareChoice = str(input("   " + mainInputText + "(1/2): "))

            #ScreenShareChoice
            if ScreenShareChoice == "1":
                ScreenShare = int(1)
                clear()
                
            elif ScreenShareChoice == "2":
                clear()
            
            else:
                error()
                section1()

        #YoutubeQuality
        if Platform == 2:
            title()
            print("   " + qualityText)
            print(""" 
       1. 144p 
       2. 240p
       3. 360p
       4. 480p
       5. 720p (HD)
       6. 1080p (Full HD)
       7. 1440p (Quad HD)
       8. 2160p (Ultra HD / 4K)
       9. 4320p (Full Ultra HD / 8K)
      """)
            QualityChoice = str(input("   " + mainInputText + "(1/2/3/4/5/6/7/8/9): "))
        
            #YoutubeQualityChoice
            if QualityChoice == "1":
                YT += float(0.060)
                clear()
                
            elif QualityChoice == "2":
                YT += float(0.215)
                clear()
            elif QualityChoice == "3":
                YT += float(0.375)
                clear()                
            elif QualityChoice == "4":
                YT += float(0.570)
                clear()               
            elif QualityChoice == "5":
                YT += float(1.950)
                clear()              
            elif QualityChoice == "6":
                YT += float(3.300)
                clear()             
            elif QualityChoice == "7":
                YT += float(5.400)
                clear()         
            elif QualityChoice == "8":
                YT += float(14.250)
                clear()              
            elif QualityChoice == "9":
                YT += float(15.750)
                clear()
            
            else:
                error(errorText)
                section1()

        #Time
        title()
        print("   " + timeText + P + "?")
        space()
        WPInput = str(input("   " + userInputText + hourText))

        #TimeChoice
        WaktuPemakaian = int(WPInput)
        WPInputCheck = WPInput.isdigit()
        if WPInputCheck == False:
            error(errorText)
            section1()
            
        else:
            clear()

        #Participant
        if Platform == 0 or Platform == 1:
            title()
            print("   " + participantText + P + "?")
            space()
            JPInput = str(input("   " + userInputText + peopleText))

            #ParticipantChoice
            JumlahPeserta = int(JPInput)
            JPInputCheck = JPInput.isdigit()
            if JPInputCheck == False:
                error(errorText)
                section1()
            
            else:
                clear()

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
        T = lambda t, v, a, s, y: t * (v + a + s + y)

        #Process
        HasilKuota = float(T(WaktuPemakaian, VD, AD, SS, YT))
        KonversiKuota = round(HasilKuota, 2)
        PenggunaanKuota = str(KonversiKuota) + "GB"

        #OutputData
        if Platform == 0:
            ZoomData.append(PenggunaanKuota)
            AllData.append(KonversiKuota)
            MeetData.append("-")
            YoutubeData.append("-")
            DatesData.append(DateNow)
            Indicator.append("X")
            
        elif Platform == 1:
            MeetData.append("        " + PenggunaanKuota)
            AllData.append(KonversiKuota)
            ZoomData.append("  -")
            YoutubeData.append("      -")
            DatesData.append(DateNow)
            Indicator.append("X")
            
        elif Platform == 2:
            YoutubeData.append("    " + PenggunaanKuota)
            AllData.append(KonversiKuota)
            ZoomData.append("  -")
            MeetData.append("      -")
            DatesData.append(DateNow)
            Indicator.append("X")

        #SaveData
        saveData()
        
        #Intermission
        load(processText)

        #Result
        title()
        print("   " + resultTextFront + PenggunaanKuota + resultTextBack)
        space()

        #Estimation
        print("   " + estimationText)

        if KonversiKuota <= float(1):
            print("   30GB" + estimationTextMonth)
        elif KonversiKuota >= float(1) and KonversiKuota <= float(5):
            print("   60GB" + estimationTextMonth)
        elif KonversiKuota >= float(5) and KonversiKuota <= float(15):
            print("   120GB" + estimationTextMonth)
        elif KonversiKuota >= float(15):
            print("   " + estimationTextLimit)

        #Final
        space()
        print("   " + finalText)
        print(yesNoText)
        FinalChoice = str(input("   " + mainInputText + "(1/2): "))

        #FinalChoice
        if FinalChoice == "1":
            clear()
            section1()
        elif FinalChoice == "2":
            clear()
            mainSystem()
        else:
            print("   " + errorMainText)
            wait(2)
            clear()
            mainSystem()

    #Section2
    def section2():
        #Intermission
        if "X" in Indicator:
            load(loadText)
        else:
            clear()

        #Title
        print(f"{section2Title : ^76}")
        space()

        #TableName
        print(f"{tableNameDate : ^28}{'Zoom' : ^7}{'Meet' : ^24}{'Youtube' : ^7}")
        print(f"{'___________________________________________________________' : ^78}")

        #TableContents
        if "X" in Indicator:
            for data in range(0, len(Indicator)):
                print(f"{DatesData[data] : ^28}{ZoomData[data] : ^1}{MeetData[data] : ^25}{YoutubeData[data] : ^7}")
                space()
        else:
            print(f"{tableContentsText : ^78}")
            space()

        #Note
        space()
        if "X" in Indicator:
          print("         *Note: 1GB = 1000MB*")
        space()

        #Back
        back("         ",backText)

    #Section3
    def section3():
        #Title
        print(f"{section3Title : ^60}")
        space()

        #Developer
        print("   " + developerText)
        space()

        #Information
        print(infoText)
        space()

        #References
        print("   " + referencesTitleText)
        print("""   
   https://tinyurl.com/GoogleUsage
   https://tinyurl.com/YoutubeUsage   
   https://tinyurl.com/ZoomUsage
   https://www.w3schools.com/
        """)
        space()

        #Footer
        print("   V. 1.1.")
        print("   AnotherMelvin ©2021")
        space()

        #Back
        back("   ",backText)

    #Section4
    def section4():
        #Title
        print(f"{section4Title : ^60}")
        space()
    
        #LanguageInfo
        print("   " + languageText)
        print(languageChoiceText)
        print("   " + backText)
        space()

        #LanguageConfirmation
        LanguageConfirmation = str(input("   " + mainInputText + "(1/2): "))

        if LanguageConfirmation == "1":
            LanguageIndicator.clear()
            LanguageIndicator.append("English")
            with open('data/LanguageIndicator.txt', 'w') as filehandle:
                for Data in LanguageIndicator:
                    filehandle.write('%s\n' % Data)                   
            clear()
            mainSystem()
            
        elif LanguageConfirmation == "2":
            LanguageIndicator.clear()
            LanguageIndicator.append("Indonesia")
            with open('data/LanguageIndicator.txt', 'w') as filehandle:
                for Data in LanguageIndicator:
                    filehandle.write('%s\n' % Data)            
            clear()
            mainSystem()
            
        elif LanguageConfirmation == "":
            clear()
            mainSystem()
            
        else:
            error(errorText)
            section4()

    #Section5
    def section5():
        #ResetInfo
        print("   " + resetQuestionText)
        print(yesNoText)

        #ResetConfirmation
        ResetConfirmation = str(input("   " + mainInputText + "(1/2): "))

        if ResetConfirmation == "1":
            clear()
            AllData.clear()
            DatesData.clear()
            Indicator.clear()
            MeetData.clear()
            YoutubeData.clear()
            ZoomData.clear()
            saveData()    
            load(resetText)
            print(resetConfirmationText)
            wait(2)
            clear()
            mainSystem()
            
        elif ResetConfirmation == "2":
            clear()
            mainSystem()

        else:
            error(errorText)
            section5()

    #Section6
    def section6():
        #ConfirmationInfo
        print("   " + exitText)
        print(yesNoText)

        #Confirmation
        ExitConfirmation = str(input("   " + mainInputText + "(1/2): "))

        if ExitConfirmation == "1":
            clear()
            print(confirmationText)
            wait(2)
            clear()
            exit()

        elif ExitConfirmation == "2":
            clear()
            mainSystem()

        else:
            error(errorText)
            section6()

    #MainConditions
    while Section == 0:
        mainSystem()
    while Section == 1:
        section1()
        break
    while Section == 2:
        section2()
        break
    while Section == 3:
        section3()
        break
    while Section == 4:
        section4()
        break
    while Section == 5:
        section5()
        break
    while Section == 6:
        section6()
        break        

#Excecute
mainSystem()