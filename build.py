# $language = "python"
# $interface = "1.0"
def main():
    crt.Screen.Send("cd /home/build/Develop/SourceCode/UIG/hp/ServiceMgt\r")
    crt.Screen.Send("gmake\r")
    crt.Screen.WaitForString("/home/build/Develop/SourceCode/UIG/hp/ServiceMgt")
    crt.Screen.Send("cd /home/build/Develop/SourceCode/UIG/hp/IntfFcgiApp\r")
    crt.Screen.Send("rm FC_IM_interboss\r")
    crt.Screen.WaitForString("/home/build/Develop/SourceCode/UIG/hp/IntfFcgiApp")
    crt.Screen.Send("gmake -f FC_IM_interboss.mk FC_IM_interboss\r")
    crt.Screen.WaitForString("/home/build/Develop/SourceCode/UIG/hp/IntfFcgiApp")
    crt.Screen.Send("ftp 10.46.180.97\r")
    crt.Screen.WaitForString("Name (10.46.180.97:build):")
    crt.Screen.Send("bossia1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossia1\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("cd /bossapp1/prg/bin\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bi\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("put FC_IM_interboss\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bye\r")


#    crt.Screen.WaitForString("[bossia1@boss01 bin]$")
#    crt.Screen.Send("kill `ps -ef|grep DA_IM_bc_deductfile_req |awk '{print $2}'`\r")
#    crt.Screen.WaitForString("[bossia1@boss01 bin]$")
#    crt.Screen.Send("telnet 10.1.0.183\r")
#    crt.Screen.WaitForString("login:")
#    crt.Screen.Send("ia64\r")
#    crt.Screen.WaitForString("Password:")
#    crt.Screen.Send("ia64\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia$")
#    crt.Screen.Send("cd /home/ia/UIG\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG")
#    crt.Screen.Send(". ./Env\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG")
#    crt.Screen.Send("cd /home/ia/UIG/FileMgrV2\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG/FileMgrV2")
#    crt.Screen.Send("gmake\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG/FileMgrV2")
#    crt.Screen.Send("cd /home/ia/UIG/FileMgtV2\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG/FileMgtV2")
#    crt.Screen.Send("gmake\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG/FileMgtV2")
#    crt.Screen.Send("cd /home/ia/UIG/IntfDaemon\r")
#    crt.Screen.Send("rm DA_IM_bc_deductfile_req\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG/IntfDaemon")
#    crt.Screen.Send("gmake -f uig_file_expV2.mk DA_IM_bc_deductfile_req\r")
#    crt.Screen.WaitForString("ia64@boss-qydb:/home/ia/UIG/IntfDaemon")
#    crt.Screen.Send("exit\r")
#    crt.Screen.WaitForString("[bossia1@boss01 bin]$")
#    crt.Screen.Send("ftp 10.1.0.183\r")
#    crt.Screen.WaitForString("Name (10.1.0.183:bossia1):")
#    crt.Screen.WaitForString("[bossia1@boss01 bin]")
#    crt.Screen.Send("DA_IM_bc_deductfile_req -start 30075413 ../conf/DA_IM_BC_deductfile_req.cfg\r")
#    crt.Screen.WaitForString("[bossia1@boss01 bin]")
main()
