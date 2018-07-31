

<?php
   
	$content = "机器学习"; //获取用户输入内容
	print_r($content);
	echo "<br>";
	echo  iconv('UTF-8','GBK',$content);
	echo "<br>";
	
	$systime = time();  //时间戳
	$mysqli = mysqli_connect('localhost','root','root','webchat');
	mysqli_query($mysqli,'set names utf8');
	$sql = "INSERT INTO `chat`(`userid`,`content`,`systime`) VALUES('3','$content','$systime')";
	mysqli_query($mysqli,$sql);  //执行插入数据库操作
	$content1=iconv('UTF-8','GBK',$content);
	
	
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
	print_r($all_arr);
	echo "<br>";
	reset($all_arr);
	$answer=current($all_arr);
	$answert = iconv('GBK','UTF-8',$answer);
	print_r($answer);
?>

