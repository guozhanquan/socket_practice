package java_socket;

import java.text.SimpleDateFormat;
import java.util.Date;
//������
class GetDate {  
    /** 
     * ʱ���ʽ���� 
     */  
    private static SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH-mm-ss");  
    public static String getDate(){  
        return df.format(new Date());  
    }    
} 