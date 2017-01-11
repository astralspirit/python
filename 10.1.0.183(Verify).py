# $language = "python"
# $interface = "1.0"
def main():
    crt.Screen.Send("cd /bossapp1/prg/bin\r")
    crt.Screen.WaitForString("bossia1@boss01:[/bossapp1/prg/bin]$")
    crt.Screen.Send("kill -9 `ps -ef|grep DA_IM_ccb_verify_rsp |grep -v log|awk '{print $2}'`\r")
    crt.Screen.WaitForString("bossia1@boss01:[/bossapp1/prg/bin]$")
    crt.Screen.Send("ssh -l ia64  10.1.0.183\r")
    crt.Screen.WaitForString("password:")
    crt.Screen.Send("ia64\r")
    crt.Screen.WaitForString("[/home/ia64]")
    crt.Screen.Send("cd /home/ia64/hp\r")
    crt.Screen.WaitForString("[/home/ia64/hp]")
    crt.Screen.Send(". ./Env\r")
    crt.Screen.WaitForString("[/home/ia64/hp]")
    crt.Screen.Send("cd ServiceMgt\r")
    crt.Screen.WaitForString("[/home/ia64/hp/ServiceMgt]")
    crt.Screen.Send("gmake\r")
    crt.Screen.WaitForString("[/home/ia64/hp/ServiceMgt]")
    crt.Screen.Send("cd ../IntfDaemon/\r")
    crt.Screen.Send("rm DA_IM_ccb_verify_rsp\r")
    crt.Screen.WaitForString("[/home/ia64/hp/IntfDaemon]")
    crt.Screen.Send("gmake -f uig_file_imp.mk DA_IM_ccb_verify_rsp\r")
    crt.Screen.WaitForString("[/home/ia64/hp/IntfDaemon]")
    crt.Screen.Send("exit\r")
    crt.Screen.WaitForString("bossia1@boss01:[/bossapp1/prg/bin]$")
    sftp183()
    crt.Screen.WaitForString("bossia1@boss01:[/bossapp1/prg/bin]$")
    crt.Screen.Send("DA_IM_ccb_verify_rsp -start 30075257 ../conf/DA_IM_ccb_verify_rsp.cfg\r")
    crt.Screen.WaitForString("bossia1@boss01:[/bossapp1/prg/bin]$")
    
def sftp183():
    crt.Screen.Send("sftp ia64@10.1.0.183\r")
    crt.Screen.WaitForString("ia64@10.1.0.183's password:")
    crt.Screen.Send("ia64\r")
    crt.Screen.WaitForString("sftp>")
    crt.Screen.Send("cd /home/ia64/hp/IntfDaemon/\r")
    crt.Screen.WaitForString("sftp>")
    crt.Screen.Send("get DA_IM_ccb_verify_rsp\r")
    crt.Screen.WaitForString("sftp>")
    crt.Screen.Send("bye\r")
main()

      