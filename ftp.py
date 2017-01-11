# $language = "python"
# $interface = "1.0"
def main():
    crt.Screen.Send("ftp 10.46.158.20\r")
    crt.Screen.WaitForString("Name (10.46.158.20:bossim1):")
    crt.Screen.Send("nl_dev\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("nl_dev\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bi\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("cd BOSS1.5/71611-1-34\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("get DA_IM_Bank_Recon\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bye\r")
main()

      