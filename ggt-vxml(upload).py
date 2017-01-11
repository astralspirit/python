# $language = "python"
# $interface = "1.0"

def ggtVxmlUpload():    
    #把ggt.vxml文件从本地ftp到10.46.158.10服务器
    crt.Screen.Send("cd /Users/moyu/share/cvs-boss/Develop/SourceCode/UIG/hp/java/ggk_voice/WebRoot\r")
    crt.Screen.WaitForString("WebRoot moyu$")
    crt.Screen.Send("ftp 10.46.158.10\r")
    crt.Screen.WaitForString("Name (10.46.158.10:moyu):")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bi\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("put ggt.vxml\r")
    crt.Screen.WaitForString("ftp>")
    #crt.Screen.Send("lcd /Users/moyu/share/cvs-boss/Develop/SourceCode/UIG/hp/java/ggk_voice/WebRoot/common\r")
    #crt.Screen.WaitForString("ftp>")
    #crt.Screen.Send("put common_value.vxml\r")
    #crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bye\r")
    crt.Screen.WaitForString("WebRoot moyu$")
    #把ggt.vxml文件从10.46.158.10服务器ftp到10.46.152.56服务器
    crt.Screen.Send("telnet 10.46.158.10\r")
    crt.Screen.WaitForString("login:")    
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im")
    crt.Screen.Send("cd /bossapp1/im\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im")
    crt.Screen.Send("ftp 10.46.152.56\r")
    crt.Screen.WaitForString("Name (10.46.152.56:bossim1):")
    crt.Screen.Send("ipfile\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("ipfile\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("cd /newland/ggk_voice\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bi\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("put ggt.vxml\r")
    crt.Screen.WaitForString("ftp>")
    #crt.Screen.Send("cd /newland/ggk_voice/common\r")
    #crt.Screen.WaitForString("ftp>")
    #crt.Screen.Send("put common_value.vxml\r")
    #crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bye\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im$")
    crt.Screen.Send("exit\r")

def ggtVxmlLog():    
    #把ggt.vxml文件从本地ftp到10.46.158.10服务器
    crt.Screen.Send("cd /Users/moyu/desktop\r")
    crt.Screen.WaitForString("desktop moyu$")
    #把ggt.vxml文件从10.46.158.10服务器ftp到10.46.152.56服务器
    crt.Screen.Send("telnet 10.46.158.10\r")
    crt.Screen.WaitForString("login:")    
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im")
    crt.Screen.Send("cd /bossapp1/im\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im")
    crt.Screen.Send("telnet 10.46.152.56\r")
    crt.Screen.WaitForString("FJFZ-PS-CRMNGCC-SIP21 login:")
    crt.Screen.Send("zxinvxi\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("os10+ZTE\r")
    crt.Screen.WaitForString("zxinvxi@FJFZ-PS-CRMNGCC-SIP21:~>")
    crt.Screen.Send("cd /home/zxinvxi/log\r")
    crt.Screen.WaitForString("zxinvxi@FJFZ-PS-CRMNGCC-SIP21:~>")
    
#start run
dialogStr = "please choose operator type: \n\n" \
+ "1: ggt.vxml upload\n" \
+ "2: view zxggk_log\n"

while True :
  operatorType = crt.Dialog.Prompt(dialogStr, "ggt", "", False)
  if operatorType == "":
      break
  elif operatorType == "1":
      ggtVxmlUpload()
      break
  elif operatorType == "2":
      ggtVxmlLog()
      break
  else:
      continue
