<?php
  $led0 = ""; $led1 = ""; $led2 = ""; $led3 = "";
  $led4 = ""; $led5 = ""; $led6 = ""; $led7 = "";
  if(isset($_GET["smit"]))
  {
    $buf = '';
    if(isset($_GET["led0"]))
    {
      $led0 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led0 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led1"]))
    {
      $led1 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led1 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led2"]))
    {
      $led2 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led2 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led3"]))
    {
      $led3 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led3 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led4"]))
    {
      $led4 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led4 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led5"]))
    {
      $led5 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led5 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led6"]))
    {
      $led6 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led6 = '';
      $buf = $buf.'0';
    }
    if(isset($_GET["led7"]))
    {
      $led7 = "checked='on'";
      $buf = $buf.'1';
    }
    else
    {
      $led7 = '';
      $buf = $buf.'0';
    }

    $datfile = fopen("./status.dat", "w");
    fwrite($datfile, $buf);
    fclose($datfile);    
  }
?>
<html lang="en">
<head>
  <title>Raspberry Pi Iot Service</title>
</head>
<body>
<form action="index.php">
  <input type="checkbox" name="led0" <?=$led0?>>LED0 + Relay 0<br />
  <input type="checkbox" name="led1" <?=$led1?>>LED1 + Relay 1<br />
  <input type="checkbox" name="led2" <?=$led2?>>LED2<br />
  <input type="checkbox" name="led3" <?=$led3?>>LED3<br />
  <input type="checkbox" name="led4" <?=$led4?>>LED4<br />
  <input type="checkbox" name="led5" <?=$led5?>>LED5<br />
  <input type="checkbox" name="led6" <?=$led6?>>LED6<br />
  <input type="checkbox" name="led7" <?=$led7?>>LED7<br />
  <input type="hidden" name="smit"><br />
  <br />
  <input type="submit" value="전송">
</form>
</body>
</html>
