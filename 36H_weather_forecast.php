<?php
// ※ URL：https://opendata.cwb.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={apikey}&format={format}                
// {dataid} 為資料編號 (參照：資料清單)  ex.F-C0032-001                
// {apikey} 為會員帳號對應之授權碼  ex.CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678
// {format} 為回傳資料格式  ex.XML、JSON(預設)                
// ※ 範例：https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678&format=JSON
// 三十六小時天氣預報

$source_url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=";
$source_key = "CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678";
$source_json = "&format=JSON";

$AA = $source_url.$source_key.$source_json;
$json0_AA = file_get_contents($AA);

$json0_AA1= json_decode($json0_AA);
$zz=0;
for($zz;$zz<22;$zz++)
{
    $success = $json0_AA1 -> success;
    $datasetDescription = $json0_AA1 -> records -> datasetDescription;
    $locationName = $json0_AA1 -> records -> location[$zz] ->locationName;

    $hwf01 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> elementName;

    $hwf02 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[0] -> startTime;
    $hwf03 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[0] -> endTime;
    $hwf04 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[0] -> parameter ->parameterName ;
    $hwf05 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[0] -> parameter ->parameterValue ;

    $hwf06 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[1] -> startTime;
    $hwf07 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[1] -> endTime;
    $hwf08 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[1] -> parameter ->parameterName ;
    $hwf09 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[1] -> parameter ->parameterValue ;

    $hwf10 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[2] -> startTime;
    $hwf11 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[2] -> endTime;
    $hwf12 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[2] -> parameter ->parameterName ;
    $hwf13 = $json0_AA1 -> records -> location[$zz] -> weatherElement[0] -> time[2] -> parameter ->parameterValue ;

    $hwf14 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> elementName;

    $hwf15 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[0] -> startTime;
    $hwf16 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[0] -> endTime;
    $hwf17 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[0] -> parameter ->parameterName ;
    $hwf18 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[0] -> parameter ->parameterUnit ;

    $hwf19 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[1] -> startTime;
    $hwf20 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[1] -> endTime;
    $hwf21 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[1] -> parameter ->parameterName ;
    $hwf22 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[1] -> parameter ->parameterUnit ;

    $hwf23 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[2] -> startTime;
    $hwf24 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[2] -> endTime;
    $hwf25 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[2] -> parameter ->parameterName ;
    $hwf26 = $json0_AA1 -> records -> location[$zz] -> weatherElement[1] -> time[2] -> parameter ->parameterUnit ;

    $hwf27 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> elementName;
    $hwf28 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[0] -> startTime;
    $hwf29 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[0] -> endTime;
    $hwf30 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[0] -> parameter ->parameterName ;
    $hwf31 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[0] -> parameter ->parameterUnit ;
    $hwf32 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[1] -> startTime;
    $hwf33 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[1] -> endTime;
    $hwf34 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[1] -> parameter ->parameterName ;
    $hwf35 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[1] -> parameter ->parameterUnit ;
    $hwf36 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[2] -> startTime;
    $hwf37 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[2] -> endTime;
    $hwf38 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[2] -> parameter ->parameterName ;
    $hwf39 = $json0_AA1 -> records -> location[$zz] -> weatherElement[2] -> time[2] -> parameter ->parameterUnit ;

    $hwf40 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> elementName;
    $hwf41 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[0] -> startTime;
    $hwf42 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[0] -> endTime;
    $hwf43 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[0] -> parameter ->parameterName ;

    $hwf44 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[1] -> startTime;
    $hwf45 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[1] -> endTime;
    $hwf46 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[1] -> parameter ->parameterName ;

    $hwf47 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[2] -> startTime;
    $hwf48 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[2] -> endTime;
    $hwf49 = $json0_AA1 -> records -> location[$zz] -> weatherElement[3] -> time[2] -> parameter ->parameterName ;

    $hwf50 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> elementName;
    $hwf51 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[0] -> startTime;
    $hwf52 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[0] -> endTime;
    $hwf53 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[0] -> parameter ->parameterName ;
    $hwf54 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[0] -> parameter ->parameterUnit ;
    $hwf55 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[1] -> startTime;
    $hwf56 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[1] -> endTime;
    $hwf57 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[1] -> parameter ->parameterName ;
    $hwf58 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[1] -> parameter ->parameterUnit ;
    $hwf59 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[2] -> startTime;
    $hwf60 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[2] -> endTime;
    $hwf61 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[2] -> parameter ->parameterName ;
    $hwf62 = $json0_AA1 -> records -> location[$zz] -> weatherElement[4] -> time[2] -> parameter ->parameterUnit ;

    $server = '127.0.0.1';
    $dbuser = 'root';
    $dbpassword = '';
    $dbname = 'cwb';
    $link = mysqli_connect($server,$dbuser,$dbpassword,$dbname,3306);
    if(!$link){
    echo "資料庫連接失敗";
    exit();
    }
    else{
    mysqli_query( $link, "SET NAMES 'utf8'");

    $sql_log="INSERT INTO thirty_six_hour_weather_forecast 
    (locationName,36hwf01,36hwf02,36hwf03,36hwf04,36hwf05,36hwf06,36hwf07,36hwf08,36hwf09,36hwf10,
    36hwf11,36hwf12,36hwf13,36hwf14,36hwf15,36hwf16,36hwf17,36hwf18,36hwf19,36hwf20,36hwf21,36hwf22,36hwf23,36hwf24,36hwf25,36hwf26,36hwf27,36hwf28,36hwf29
    ,36hwf30,36hwf31,36hwf32,36hwf33,36hwf34,36hwf35,36hwf36,36hwf37,36hwf38,36hwf39,36hwf40,36hwf41,36hwf42,36hwf43,36hwf44,36hwf45,36hwf46,36hwf47,36hwf48
    ,36hwf49,36hwf50,36hwf51,36hwf52,36hwf53,36hwf54,36hwf55,36hwf56,36hwf57,36hwf58,36hwf59,36hwf60,36hwf61,36hwf62)
    value ('$locationName','$hwf01','$hwf02','$hwf03','$hwf04','$hwf05','$hwf06','$hwf07','$hwf08','$hwf09','$hwf10',
    '$hwf11','$hwf12','$hwf13','$hwf14','$hwf15','$hwf16','$hwf17','$hwf18','$hwf19','$hwf20','$hwf21','$hwf22','$hwf23','$hwf24','$hwf25','$hwf26','$hwf27','$hwf28','$hwf29'
    ,'$hwf30','$hwf31','$hwf32','$hwf33','$hwf34','$hwf35','$hwf36','$hwf37','$hwf38','$hwf39','$hwf40','$hwf41','$hwf42','$hwf43','$hwf44','$hwf45','$hwf46','$hwf47','$hwf48'
    ,'$hwf49','$hwf50','$hwf51','$hwf52','$hwf53','$hwf54','$hwf55','$hwf56','$hwf57','$hwf58','$hwf59','$hwf60','$hwf61','$hwf62'
    )";
        if ($link->query($sql_log) === TRUE) {
            echo "新增資料成功";
        } else {
            echo "新增資料失敗: " . $link->error;
                }
        }

}

?>