<?php
if(!isset($_SESSION)) 
{ 
    session_start(); 
    session_regenerate_id();
} 

if(!isset($_SESSION['user']))      // if there is no valid session
{
    header("Location: index.php");
}
?>

<style>
    body {
    margin: 30px;
}
body {
    font-family: Arial;
}
h1 {
    font-weight:bold;
    font-size:16px;
}
p {
    margin:5px 0px 5px 0px;
}
li a {
    margin-left:5px;
}
    </style>
<div id="new-note">
     <h2>New Ghost!</h2>
    <form action="newnote.php" method="post">
        <input type="text" value="" placeholder="Ghosts name" id="ghostname" name="ghostname"/> <br>
        <select name="type" id="type">
  <option value=".txt">.txt</option>
  <option value=".png" disabled>.png</option>
  <option value=".gif" disabled>.gif</option>
  <option value=".jpg" disabled>.jpg</option>
</select> pleae note we can only get .txt ghosts for now! <br>
        <textarea id="textarea" name="textarea"></textarea> <br>
        <br>
        <button>Submit new ghost!</button>
    </form>
</div>
<h2>logout <a href="./logout.php">here</a></h2>
