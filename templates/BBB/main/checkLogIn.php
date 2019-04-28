<?
include("base/head.php");
?>
<h3><i class="icon-user"></i>Login Status</h3></div>
<div class="box-content ">
<?php
if ($_REQUEST['Clinmed_User'] ) 
{
    session_name($_REQUEST['Clinmed_User']);
}
session_start();
include('config.php');
session_name('Clinmed_User');

$email=$_POST['email'];
$pass=$_POST['passwd'];
	$activation = 0;
	$type=$_POST["type"];
	if($email || $pass)
	{
	if($type=="author")$type="user";
	$t_sql="SELECT * FROM ".$type."s WHERE email = '$email' && password = '$pass'";
	if($type=="user")$type="author";
	$result = mysqli_query($con,$t_sql) or die("");
	if(mysqli_num_rows($result)>0)
	{
	$row=mysqli_fetch_array($result);
	$User_ID=$row["User_ID"];
	$username=$row["fname"]." ".$row["lname"];
	$activation=$row["activation"];
	if($activation=='0')die("<h3>Please activate your account</h3>");
	else
		{
		if($row['User_Type']==$_POST["type"]){$_SESSION['type']=$type;}
			$_SESSION['type'] = $row['User_Type'];
			$_SESSION['username'] = $username;
			$_SESSION['email']=$row['email'];
			$_SESSION['country']=$row['country'];
			$_SESSION['user_id']=$row['User_ID'];
			echo "<script>window.location = 'index.php'</script>";
		}
	}
	else{echo "<h4>Please Check your credentials</h4>";}
	}
	

/*

			
			if ($row['activation'] == 1)
					{
						$activation=1;
						$user = $row['username'];
						$id = $row['user_id'];
						$_SESSION['views']=1;
						$_SESSION['username'] =  $row['username'];//Adminstrator
						$_SESSION['id'] = $id;
						$_SESSION['hid'] = $Shid;
						$_SESSION['admin'] = $row['admin'];
						$_SESSION['user_id'] = $row['user_id'];
						$_SESSION['type'] = $row['type'];
						if($row['type']=="admin"){$_SESSION['username'] =  "Administrator";}
						echo "<script>window.location = 'index.php'</script>";
					}
					else
					{
$msg = "<h4 style='color:red'>Your account is not activated. Please check your mail and enter the activation code here</h4>";
echo $msg;
?>
							
<?php

					}
				}
			}
			
		
}
?>

*/


include("base/tail.php");
?>
