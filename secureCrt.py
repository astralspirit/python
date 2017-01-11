# $language = "python"
# $interface = "1.0"
def main():
    crt.Screen.Send("cd /boss/uig/UnionPayV2\r")
    crt.Screen.WaitForString("test02:/boss/uig/UnionPayV2")
    crt.Screen.Send("gmake\r")
    crt.Screen.WaitForString("test02:/boss/uig/UnionPayV2")
    crt.Screen.Send("cd /boss/uig/IntfUtil\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfUtil")
    crt.Screen.Send("gmake\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfUtil")
    crt.Screen.Send("cd /boss/uig/UnionPaySvcMgtV2\r")
    crt.Screen.WaitForString("test02:/boss/uig/UnionPaySvcMgtV2")
    crt.Screen.Send("gmake\r")
    crt.Screen.WaitForString("test02:/boss/uig/UnionPaySvcMgtV2")
    crt.Screen.Send("cd /boss/uig/IntfUaspDaemon\r")
    crt.Screen.Send("rm DA_IM_UNIONPAY_IN\r")
    crt.Screen.Send("gmake -f uig_unionpay_in.mk\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfUaspDaemon")
    crt.Screen.Send("telnet 10.46.158.10\r")
    crt.Screen.WaitForString("login:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im$")
    crt.Screen.Send("kill `ps -ef|grep DA_IM_FZUNIONPAY_IN|grep -v grep|awk '{print $2}'`\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im$")
    crt.Screen.Send("kill `ps -ef|grep DA_IM_BC_IN|grep -v grep|grep -v log|awk '{print $2}'`\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im$")
    crt.Screen.Send("exit\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfUaspDaemon$")
    crt.Screen.Send("ftp 10.46.158.10\r")
    crt.Screen.WaitForString("Name (10.46.158.10:uig):")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("cd /boss/bossapp1/prg/bin\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bi\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("put DA_IM_UNIONPAY_IN DA_IM_FZUNIONPAY_IN\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("put DA_IM_UNIONPAY_IN DA_IM_BC_IN\r")
    crt.Screen.WaitForString("ftp>")
    crt.Screen.Send("bye\r")
    crt.Screen.Send("telnet 10.46.158.10\r")
    crt.Screen.WaitForString("login:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("Password:")
    crt.Screen.Send("bossim1\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/im$")
    crt.Screen.Send("cd /bossapp1/prg/bin\r")
    crt.Screen.WaitForString("t-as-js:/bossapp1/prg/bin$")
    crt.Screen.Send("DA_IM_FZUNIONPAY_IN.start\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfUaspDaemon$",3)
    crt.Screen.Send("DA_IM_BC_IN.start\r")
    crt.Screen.WaitForString("test02:/boss/uig/IntfUaspDaemon$",3)
    crt.Screen.Send("exit\r")
main()

#def main():
	# Send the unix "date" command and wait for the prompt that
	# indicating that it completed. In general we want to be in
	# synchronous mode before doing send/wait operations.
	#
	#crt.Screen.Synchronous = True
	#crt.Screen.Send("date\r")

	#promptString = "linux$"
	#crt.Screen.WaitForString(promptString)

	# When we get here the cursor should be one line below the output of
	# the 'date' command. Subtract one line and use that value to read a
	# chunk of text (1 row, 40 characters) from the screen.
	# 
	#screenrow = crt.Screen.CurrentRow - 1
	#result = crt.Screen.Get(screenrow, 1, screenrow, 40)

	# Get() reads a fixed size of the screen. So you may need to use a
	# regular expression function or the str.split() method to do some
	# simple parsing if necessary. Just print it out here.
	#
	#crt.Dialog.MessageBox(result)
	#crt.Screen.Synchronous = False

#main()