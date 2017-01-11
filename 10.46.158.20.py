# $language = "python"
# $interface = "1.0"
def main():
    crt.Screen.Send("ftp 10.46.9.229\r")
    crt.Screen.WaitForString("Name (10.46.9.229:bossim1):")
    crt.Screen.Send("nldev\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("nldev\r")
    crt.Screen.WaitForString("ftp>")
main()
