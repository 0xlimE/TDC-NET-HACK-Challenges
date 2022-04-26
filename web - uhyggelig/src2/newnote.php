<?php

if (!function_exists('str_contains')) { //str_contains for php 7
    function str_contains(string $haystack, string $needle): bool
    {
        return '' === $needle || false !== strpos($haystack, $needle);
    }
}


$ghostpath = "/var/www/ghosts/";
$dangerous = array(".php", ".php2", ".php3", ".php4", ".php5", ".php6", ".php7", ".phps", ".phps", ".pht", ".phtm", ".phtml", ".pgif", ".shtml", ".htaccess", ".phar", ".inc");
if(!isset($_SESSION)) 
{ 
    session_start(); 
    session_regenerate_id();
} 

if(!isset($_SESSION['user']))      // if there is no valid session
{
    header("Location: index.php");
}
if( isset($_POST['ghostname']) && isset($_POST['textarea']) && isset($_POST['type']) )
{
    foreach($dangerous as $danger){
        if(str_contains($danger,strtolower($_POST['type']))){
            die("THATS DANGEROUS! YO!");
        }
    }
    $ghostfile = $_POST['ghostname'].$_POST['type'];

    if(strlen($ghostfile) > 15)
    {
        die("too long ghostname :(");
    }

    file_put_contents($ghostpath."ghosts/".$ghostfile,$_POST['textarea']);

    $myfile = fopen($ghostpath."index.php", "a") or die("Unable to open file!");
    fwrite($myfile, "\n". '<br><a href="./file.php?file='.$ghostfile.'">'.$_POST['ghostname'].'<a>');
    fclose($myfile);

    echo("<h1>Yes!! the ghost was put there succesfully!, you should see it on the main site now :D</h1>");
}
?>
