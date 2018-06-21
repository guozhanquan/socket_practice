package java_socket;

import java.text.SimpleDateFormat;
import java.util.Date;
//工具类
class GetDate {  
    /** 
     * 时间格式到秒 
     */  
    private static SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH-mm-ss");  
    public static String getDate(){  
        return df.format(new Date());  
    }    
} 