<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php 
 	set_include_path(get_include_path() . PATH_SEPARATOR . 'phpseclib/');
    include('Net/SSH2.php');
    include('Crypt/RSA.php');

    //if rsa exist **use
    //*********************************
 	echo '<p>Hello World</p>'; 
 	$key = new Crypt_RSA();
	$ssh = new Net_SSH2('192.168.1.10',22);
	/****************************

	// for no rsa auth
	//*****************************************
	/*if (!$ssh->login('pi', 'raspberry')) {
    	exit('Login Failed');
	}*/
	//******************************************


	//if rsa exist **use
    //*********************************
	$key->loadKey(file_get_contents('sshpri.ppk'));
	if (!$ssh->login('pi', $key)) {
    exit('Login Failed');
	}
	//***********************************
	/*function packet_handler($str)
	{
    	echo $str;
	}
	
	echo $ssh->exec('ping 192.168.1.1','packet_handler');*/
//**** can send this command to run this code in rasp pi and it still run with ssh write and another is with exec we haven't test
	
	//$ssh->exec("python /home/pi/Desktop/comongo.py \n"); // note the "\n"// exec can execute continue now use this command only python program 
	//echo $ssh->read('pi@raspberrypi:~$');
	/*echo $ssh->exec("echo raspberry | sudo /usr/local/bin/snort -Q -c /etc/snort/snort.conf -i eth0:eth1 | sudo idstools-u2json --snort-conf /etc/snort.conf  --directory /var/log/snort  --prefix snort.u2  --output /var/log/snort/alerts4.json  --follow  -S /etc/snort/sid-msg.map  -G /etc/snort/gen-msg.map  -C /etc/snort/classification.config \n");*/
	 // run type when you need to input your password with sudo command but this is not secure

	echo $ssh->exec("echo raspberry | sudo systemctl start snort| sudo idstools-u2json --snort-conf /etc/snort.conf  --directory /var/log/snort  --prefix snort.u2  --output /var/log/snort/alerts4.json  --follow  -S /etc/snort/sid-msg.map  -G /etc/snort/gen-msg.map  -C /etc/snort/classification.config | sudo python mongocomplete.py \n")
	//echo $ssh->exec("echo raspberry | sudo systemctl start snort \n")
 ?> 
 </body>
</html>