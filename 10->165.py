# $language = "python"
# $interface = "1.0"
    
def stopProgram(in_dictPro):
    crt.Screen.Send("cd /bossapp1/prg/bin\r")
    crt.Screen.Send("pwd\r")
    crt.Screen.WaitForString("/bossapp1/prg/bin")
    crt.Screen.Send("kill -9 `ps -ef|grep " + in_dictPro['name'] + " |grep -v log|awk '{print $2}'`\r")
    crt.Screen.Send("ps -ef|grep " + in_dictPro['name'] + " |grep -v log|grep -v grep|wc -l\r")
    crt.Screen.WaitForString("0")
    
def makeProgram(in_dictPro):
    crt.Screen.Send("telnet 10.1.0.165\r")
    crt.Screen.WaitForString("login:")
    crt.Screen.Send("uig\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("Uig_2016\r")
    crt.Screen.WaitForString("test02:/boss/uig")
    crt.Screen.Send("cd " + in_dictPro['path'] + "/\r")
    crt.Screen.Send("rm " + in_dictPro['name'] + "\r")
    crt.Screen.WaitForString("test02:" + in_dictPro['path'])
    crt.Screen.Send("gmake -f " + in_dictPro['make'] + "\r")
    crt.Screen.WaitForString("test02:" + in_dictPro['path'])
    crt.Screen.Send("exit\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/prg/bin$")
    
def sftpProgram(in_dictPro):
    crt.Screen.Send("ftp 10.1.0.165\r")
    crt.Screen.WaitForString("Name (10.1.0.165:bossim1):")
    crt.Screen.Send("uig\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("Uig_2016\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("cd " + in_dictPro['path'] + "\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("get " + in_dictPro['name'] + "\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bye\r")
    
def startProgram(in_dictPro):
    crt.Screen.Send("cd /bossapp1/tools/\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/tools$")
    crt.Screen.Send(in_dictPro['name'] + ".start\r")
    
#start run
dialogStr = "please choose operator type: \n\n" \
+ "1:  DA_IM_SocketClientDaemon\n" \
+ "2:  DA_IM_nxs_deduct_file_req\n" \
+ "3:  DA_IM_Sms_Receiver\n" \
+ "4:  DA_IM_Bank_Recon\n" 

while True :
  operatorType = crt.Dialog.Prompt(dialogStr, "program", "", False)
  if operatorType == "":
      break
  elif operatorType == "1":
      dictPro = {'name': 'DA_IM_SocketClientDaemon', 'make': 'SocketClientDaemon.mk', 'path': '/boss/uig/IntfDaemon'} 
  elif operatorType == "2":
      dictPro = {'name': 'DA_IM_nxs_deduct_file_req', 'make': 'uig_file_expV2.mk DA_IM_nxs_deduct_file_req', 'path': '/home/ia64/hp/IntfDaemon'} 
  elif operatorType == "3":
      dictPro = {'name': 'DA_IM_Sms_Receiver', 'make': 'uig_sms_receiver.mk', 'path': '/home/ia64/hp/IntfDaemon'} 
  elif operatorType == "4":
      dictPro = {'name': 'DA_IM_Bank_Recon', 'make': 'DA_IM_Bank_Recon.mk DA_IM_Bank_Recon', 'path': '/home/ia64/hp/IntfDaemon'} 
  elif operatorType == "5":
      dictPro = {'name': 'DA_IM_IBDataSync_SupByDB', 'make': 'DA_IM_IBDataSync_supplements.mk', 'path': '/home/ia64/hp/IntfUaspDaemon'} 
  else:
      continue
  
  stopProgram(dictPro)      
  makeProgram(dictPro) 
  sftpProgram(dictPro)
  startProgram(dictPro)
  break