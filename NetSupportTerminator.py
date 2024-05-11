import psutil
import time
import os
import sys
import keyboard
import threading
import ctypes
import locale

languages = {
    "en": {
        #   MAIN LANGUAGE
        "welcome": "Welcome!",
        "goodbye": "Goodbye!",
        "error": "An error occurred.",
        "process being terminated": "process being terminated",
        "process named is not working": "process named is not working",
        "Powered by - SyroGen": "Powered by - SyroGen",
        "Version": "Version",
        "Commands": "Commands",
        "kill": "kill",
        "Kill netsupport and its child processes": "Kill netsupport and its child processes",
        "connect": "connect",
        "Connect to netsupport back": "Connect to netsupport back",
        "kill permanently": "kill permanently",
        "Kill netsupport and its child processes and delete the files": "Kill netsupport and its child processes and delete the files",
        "connection established": "connection established",
        "connection failled": "connection failled",
        "named file deleted successfully": "named file deleted successfully",
        "named file already unavaliable": "named file already unavaliable",
        "All processes have been terminated": "All processes have been terminated",
        "Something went wrong": "Something went wrong",
        "named command not found": "named command not found",
        "Type '?' to see commands": "Type '?' to see commands",
        "Select language": "Select language",
        "Supported languages": "Supported languages",
        "New Language": "New Language",
        "Please enter a valid language code": "Please enter a valid language code",
        "language": "language",
        "Language swapped succesfully": "Language swapped succesfully",
        "Language will be changed to": "Language will be changed to",
        "Are you sure": "Are you sure",
        "Transaction canceled": "Transaction canceled",

        "AgreeKey": "Y",
        "DenyKey": "N",
        "TR": "Turkish",
        "EN": "English",

        "Turkish": "Turkish",
        "English": "English",
    },
    "tr": {
        "process being terminated": "İşlem sonlandırıldı",
        "process named is not working": "adlı işlem çalışmıyor",
        "Powered by - SyroGen": "SyroGen tarafından geliştirildi",
        "Version": "Versiyon",
        "Commands": "Komutlar",
        "kill": "kill",
        "Kill netsupport and its child processes": "Netsupport ve alt işlemlerini sonlandır",
        "connect": "connect",
        "Connect to netsupport back": "Netsupporta geri bağlan",
        "kill permanently": "kill permanently",
        "Kill netsupport and its child processes and delete the files": "Netsupport ve alt işlemlerini sonlandır ve Netsupport dosyalarını sil",
        "connection established": "bağlantı başarıyla kuruldu",
        "connection failled": "bağlanılamadı",
        "named file deleted successfully": "adlı dosya başarıyla silindi",
        "named file already unavaliable": "adlı dosya mevcut değil",
        "All processes have been terminated": "Bütün işlemler sonlandırıldı",
        "Something went wrong": "Birşeyler yanlış gitti",
        "named command not found": "adlı komut bulunamadı",
        "Type '?' to see commands": "Komutları görmek için '?' yaz",
        "Select language": "dili değiştir",
        "Supported languages": "Desteklenen Diller",
        "New Language": "Kullanılacak Yeni Dil",
        "Please enter a valid language code": "Lütfen geçerli bir ülke kodu girin",
        "language": "language",
        "Language swapped succesfully": "Dil başarıyla değiştirildi",
        "Language will be changed to": "Yeni dil",
        "Are you sure": "Emin misin",
        "Transaction canceled": "İşlem iptal edildi",

        "AgreeKey": "E",
        "DenyKey": "H",
        "TR": "Türkçe",
        "EN": "İngilizce",

        "Turkish": "Türkçe",
        "English": "İngilizce",
    },
    #   OTHER LANGUAGES
}

processesToTerminate = [
    "client32.exe",
    "LoopbackUnblocker.dll",
    "msvcr100.dll",
    "nssres.dll",
    "PCIAPPCTRL.DLL",
    "pciappctrl64.dll",
    "pciapi.DLL",
    "PCICHEK.DLL",
    "PCIHOOKS.DLL",
    "PCIRES.dll",
    "PluginDevicesModule.dll",
    "PluginDevicesModule64.dll",
    "plugineModule.DLL",
    "pluginprintmanmodule.dll",
    "pluginprintmanmodule64.dll",
    "pluginsoftwaremodule.dll",
    "pluginsoftwaremodule64.dll",
    "pluginsoftwaremodule.DLL",
    "pluginSoftwareModule64.dll",
    "runplugin.exe",
    "Runplugin64.exe",
    "shfolder.dll",
    "StoreSoftwareCtl64.dll",
    "StudentUI.exe",
    "TCCTL32.DLL",
    "VolumeControlWVI.DLL",
]


def get_windows_language():
    windll = ctypes.windll.kernel32
    windll.GetUserDefaultUILanguage()
    return (locale.windows_locale[windll.GetUserDefaultUILanguage()])[:2]



def printEffect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print()


def quitThread():
    while True:
        time.sleep(0.2)
        if keyboard.is_pressed("q"):
            for process in processesToTerminate:
                terminate_process(process)


def terminate_process(process_name):
    while True:
        found = False
        for proc in psutil.process_iter(["pid", "name"]):
            if proc.info["name"] == process_name:
                found = True
                print(
                    f"{languages[lang]['process being terminated']} {proc.info['pid']} - {proc.info['name']}"
                )
                proc.terminate()
        if not found:
            print(f"{process_name} {languages[lang]['process named is not working']}")
            break
        time.sleep(0.5)


lang = get_windows_language()

if lang not in languages:
    lang = "en" # defult
    


printEffect(
    f"{languages[lang]['Powered by - SyroGen']}.\n{languages[lang]['Version']} - MK-1"
)
# quit_thread = threading.Thread(target=quitThread)
# quit_thread.daemon = True  # Set the thread as a daemon so it will exit when the main program exits
# quit_thread.start()

while True:
    result = input(">>>").lower()

    if result == "?":
        print(
            f"""
        {languages[lang]['Commands']} >>>
        
        {languages[lang]['kill']} ---> {languages[lang]['Kill netsupport and its child processes']}.

        {languages[lang]['connect']} ---> {languages[lang]['Connect to netsupport back']}.
        
        {languages[lang]['kill permanently']} ---> {languages[lang]['Kill netsupport and its child processes and delete the files']}.
        
        {languages[lang]['language']} ---> {languages[lang]['Select language']}
        
        """
        )
    elif result == "kill":
        for process in processesToTerminate:
            terminate_process(process)

    elif result == "connect":
        try:
            os.startfile(
                r"C:\Program Files (x86)\NetSupport\NetSupport School\client32.exe"
            )
            print(f"{languages[lang]['connection established']}.")
        except Exception as e:
            print(f"{languages[lang]['connection failled']}: {e}")
    elif result == "kill permanently":
        try:
            for process in processesToTerminate:
                terminate_process(process)
                file_path = (
                    rf"C:\Program Files (x86)\NetSupport\NetSupport School\{process}"
                )
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(
                        f"{file_path} {languages[lang]['named file deleted successfully']}."
                    )
                else:
                    print(
                        f"{file_path} {languages[lang]['named file already unavaliable']}."
                    )
            print(f"\n{languages[lang]['All processes have been terminated']}.\n")
        except Exception as e:
            print(f"{languages[lang]['Something went wrong']}: {e}")
    elif result == "language":
        print(
            f"""
              
    {languages[lang]['Supported languages']}:

    {languages[lang]['Turkish']} ---> TR

    {languages[lang]['English']} ---> EN
              
              """
        )
        result = input(f"{languages[lang]['New Language']}: ").lower()

        while True:
            if result in languages:

                print(f"\n{languages[lang]['Language will be changed to']}: {languages[lang][result.upper()]} ")
                
                approval = input(f"{languages[lang]['Are you sure']}? {languages[lang]['AgreeKey']} / {languages[lang]['DenyKey']}: ").upper()

                if(approval == languages[lang]['AgreeKey']):
                    lang = result
                else:
                    print(f"\n{languages[lang]['Transaction canceled']}.")

                print(f"\n{languages[lang]['Language swapped succesfully']}.\n")
                break
            else:
                print(f"\n{languages[lang]['Please enter a valid language code']}\n")

                result = input(f"{languages[lang]['New Language']}: ").lower()

    else:
        print(
            f"[{result}] {languages[lang]['named command not found']}.\n{languages[lang]['''Type '?' to see commands''']}."
        )
