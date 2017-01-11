# $language = "python"
# $interface = "1.0"
    
def stopProgram(in_dictPro):
    crt.Screen.Send("cd /bossapp1/prg/bin\r")
    crt.Screen.Send("pwd\r")
    crt.Screen.WaitForString("bossia1@boss02 bin")
    crt.Screen.Send("kill -9 `ps -ef|grep " + in_dictPro['name'] + " |grep -v log|awk '{print $2}'`\r")
    crt.Screen.Send("tesvrdown -n " + in_dictPro['name'] + " \r")
    crt.Screen.Send("ps -ef|grep " + in_dictPro['name'] + " |grep -v log|grep -v grep|wc -l\r")
    crt.Screen.WaitForString("0")
    
def makeProgram(in_dictPro):
    crt.Screen.Send("ssh -l ia64  10.1.0.183\r")
    crt.Screen.WaitForString("password:")
    crt.Screen.Send("ia64_2016\r")
    crt.Screen.WaitForString("[/home/ia64]")
    crt.Screen.Send("cd /home/ia64/hp\r")
    crt.Screen.WaitForString("[/home/ia64/hp]")
    crt.Screen.Send(". ./Env\r")
    crt.Screen.WaitForString("[/home/ia64/hp]")
    crt.Screen.Send("cd " + in_dictPro['path'] + "/\r")
    crt.Screen.Send("rm " + in_dictPro['name'] + "\r")
    crt.Screen.WaitForString("[" + in_dictPro['path'] + "]")
    crt.Screen.Send("gmake -f " + in_dictPro['make'] + " " + in_dictPro['name'] +"\r")
    crt.Screen.WaitForString("[" + in_dictPro['path'] + "]")
    crt.Screen.Send("exit\r")
    crt.Screen.WaitForString("bossia1@boss02 bin")
    
def sftpProgram(in_dictPro):
    crt.Screen.Send("sftp ia64@10.1.0.183\r")
    crt.Screen.WaitForString("ia64@10.1.0.183's password:")
    crt.Screen.Send("ia64_2016\r")
    crt.Screen.WaitForString("sftp>")
    crt.Screen.Send("cd " + in_dictPro['path'] + "\r")
    crt.Screen.WaitForString("sftp>")
    crt.Screen.Send("get " + in_dictPro['name'] + "\r")
    crt.Screen.WaitForString("sftp>")
    crt.Screen.Send("bye\r")
    
def startProgram(in_dictPro):
    crt.Screen.Send("cd /bossapp1/tools/\r")
    crt.Screen.WaitForString("bossia1@boss02 bin")
    crt.Screen.Send(in_dictPro['name'] + ".start\r")
    
#start run
dialogStr = "please choose operator type: \n\n" \
+ "1: reflesh FC_IM_IBAPI_SERVICE\n" \
+ "2: reflesh FC_IM_SMS_SERVICE\n" \
+ "3: reflesh FC_IM_PAYMENT_SERVICE\n" \
+ "4: reflesh FC_IM_UIG_SERVICE\n" \
+ "5: reflesh FC_IM_XMMOBILE_OUT\n" \
+ "6: reflesh FC_IM_XMBANK_OUT\n" \
+ "7: reflesh FC_IM_CCBCMPAY\n" \
+ "8: reflesh DA_IM_XMUNIONPAY_IN\n" \
+ "9: reflesh DA_IM_AutoDeductUndo\n" \
+ "10: DA_IM_FZUNIONPAY_IN\n" \
+ "11: reflesh TE_IM_1_GGK\n"      

while True :
  operatorType = crt.Dialog.Prompt(dialogStr, "program", "", False)
  if operatorType == "":
      break
  elif operatorType == "1":
      dictPro = {'name': 'FC_IM_IBAPI_SERVICE', 'make': 'fcgi_uig_svr.mk', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "2":
      dictPro = {'name': 'FC_IM_SMS_SERVICE', 'make': 'fcgi_uig_svr.mk', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "3":
      dictPro = {'name': 'FC_IM_PAYMENT_SERVICE', 'make': 'fcgi_uig_svr.mk', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "4":
      dictPro = {'name': 'FC_IM_UIG_SERVICE', 'make': 'fcgi_uig_svr.mk', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "5":
      dictPro = {'name': 'FC_IM_XMMOBILE_OUT', 'make': 'fcgi_unionpay_out.mk FC_IM_XMMOBILE_OUT', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "6":
      dictPro = {'name': 'FC_IM_XMBANK_OUT', 'make': 'fcgi_unionpay_out.mk FC_IM_XMBANK_OUT', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "7":
      dictPro = {'name': 'FC_IM_CCBCMPAY', 'make': 'fcgi_unionpay_out.mk FC_IM_CCBCMPAY', 'path': '/home/ia64/hp/IntfFcgiApp'} 
  elif operatorType == "8":
      dictPro = {'name': 'DA_IM_XMUNIONPAY_IN', 'make': 'uig_unionpay_in.mk DA_IM_XMUNIONPAY_IN', 'path': '/home/ia64/hp/IntfUaspDaemon'} 
  elif operatorType == "9":
      dictPro = {'name': 'DA_IM_AutoDeductUndo', 'make': 'DA_IM_AutoDeduct.mk DA_IM_AutoDeductUndo', 'path': '/home/ia64/hp/IntfDaemon'} 
  elif operatorType == "10":
      dictPro = {'name': 'DA_IM_FZUNIONPAY_IN', 'make': 'uig_unionpay_in.mk DA_IM_FZUNIONPAY_IN', 'path': '/home/ia64/hp/IntfUaspDaemon'} 
  elif operatorType == "11":
      dictPro = {'name': 'TE_IM_1_GGK', 'make': 'TE_IM_1_GGK.mk', 'path': '/home/ia64/hp/tong'} 
  else:
      continue
  
  stopProgram(dictPro)      
  makeProgram(dictPro) 
  sftpProgram(dictPro)
  startProgram(dictPro)
  break