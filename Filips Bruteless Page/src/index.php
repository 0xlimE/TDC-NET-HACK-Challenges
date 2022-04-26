<?php 
/*
error_reporting(E_ALL);
ini_set ('display_errors', 'on');
ini_set ('log_errors', 'on');
ini_set ('display_startup_errors', 'on');
ini_set ('error_reporting', E_ALL);
*/
?>

<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title></title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>

<?php
function verify_password( string $username , string $password ){

  $user = "adminman";
  $hash = "5918a63916ac8c1ef59a817fff6e9344"; //florianismasterofallhashes
  $password_hash = md5($password);
  $length = max(strlen($username),strlen($user))-1;
  for ($i = 1; $i <= $length; $i++) {
    if ($username[$i] !== $user[$i]){return false;}
  }
  for ($i = 1; $i <= $length; $i++) {
    if ($hash[$i] !== $password_hash[$i]) {return false;}
  }
  return true;
}
?>


<div id="bg">Bruteless login page</div>

<form method="post" action="" name="login">
  <div class="form-field">
    <input placeholder="username" name="username" required/>
  </div>
  
  <div class="form-field">
    <input type="password" placeholder="password" name="password" required/>                         </div>
  
  <div class="form-field">
    <button class="btn" type="submit">Log in</button>
  </div>

  <?php
    $msg = 'Welcome to my lovely page, user.';
    if (isset($_POST['username']) && !empty($_POST['username']) 
        && !empty($_POST['password'])) {

        if (verify_password($_POST['username'],$_POST['password'])) {         
          $msg = 'TDC{n0p455w02dc24ck1n9w4523qu123d!!}';
        }else {
          $msg = 'Wrong username or password';
        }
    }
  ?>
  <div class="form-field">

<div class="notice">
   <?= $msg?>
  </div>
  </div>
</form>
  
</body>
</html>
