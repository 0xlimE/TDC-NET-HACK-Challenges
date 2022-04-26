<tt style="white-space: pre-wrap">
<?php
   $file = $_GET['file'];
   $bad = array("../",".php");
   if(isset($file))
   {
    foreach ($bad as &$value) {
        $file = str_replace($value,"",$file);
    }
    echo($file);
    echo("<br>");
    echo(file_get_contents("ghosts/$file"));
   }
?>
</tt>