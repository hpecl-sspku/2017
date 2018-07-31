

<?php
session_start();
if(!empty($_POST['content'])){
	$userid = $_SESSION['userid'];
	$content = $_POST['content']; //获取用户输入内容
	
	$systime = time();  //时间戳
	$mysqli = mysqli_connect('localhost','root','root','webchat');
	mysqli_query($mysqli,'set names utf8');
	$sql = "INSERT INTO `chat`(`userid`,`content`,`systime`) VALUES('$userid','$content','$systime')";
	mysqli_query($mysqli,$sql);  //执行插入数据库操作
	
	//php调用python返回的答案插入到数据库中，使用的是模型的绝对地址

	
	//转换字符串的格式
	$content1=iconv('UTF-8','GBK',$content);
	//使用的时候请修改：shell_exec('python.exe的绝对地址   udc_predict.py  '.$content1)注意udc_predict.py 后有空格
	$output = shell_exec('C:\MLDLlearning\Python\python.exe  C:\myphp_www\PHPTutorial\WWW\chat\udc_predict.py '.$content1);
	
	$arr= explode(']', $output);
    $all_arr = array ();
    foreach ( $arr as $v ) {
    if(empty($v)){
        continue;
    }
    $itemarr = explode ( '[', $v );
    if(count($itemarr) != 2){
        continue;
    }
    $all_arr [$itemarr[1]] = $itemarr[0];
	}
	krsort($all_arr);
	//print_r($all_arr);
	//echo "<br>";
	reset($all_arr);
	$answer=current($all_arr);
	$answert = iconv('GBK','UTF-8',$answer);
	//print_r($answer);
	$sql = "INSERT INTO `chat`(`userid`,`content`,`systime`) VALUES(1,'$answert','$systime')";
	mysqli_query($mysqli,$sql);  //执行插入数据库操作
	if(mysqli_affected_rows($mysqli)  && !empty($_SERVER['HTTP_X_REQUESTED_WITH'])){
		echo 1;
		exit;
	}




}
include('frame/send.html');
?>

