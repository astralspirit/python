# $language = "python"
# $interface = "1.0"
def main():
    crt.Screen.Send("cd /boss/uig/UnionPayV2\r")
    crt.Screen.Send("gmake\r")
    crt.Screen.WaitForString("test02:/boss/uig/UnionPayV2")
    crt.Screen.Send("cd /boss/uig/IntfDaemon\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfDaemon")
    crt.Screen.Send("kill `ps -ef|grep DA_IM_SocketClientDaemon|grep -v grep|awk '{print $2}'`\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfDaemon")
    crt.Screen.Send("rm DA_IM_SocketClientDaemon\r")
    crt.Screen.Send("gmake -f SocketClientDaemon.mk\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfDaemon")
    crt.Screen.Send("DA_IM_SocketClientDaemon -start 30076032 ../conf/DA_IM_SocketClientDaemon.cfg 1\r")
main()
