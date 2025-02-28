Download.java
import java.io.*;
import java.net.URL;
public class Download
{
public static void main(String[] args) throws Exception
{
try
{
String fileName = "digital_image_processing.jpg";
String website = "https://upload.wikimedia.org/wikipedia/commons/7/77/Digital_image_processing.jpg"; 
System.out.println(&quot;Downloading File From: &quot; + website);
URL url = new URL(website);
InputStream inputStream = url.openStream();
OutputStream outputStream = new FileOutputStream(fileName);
byte[] buffer = new byte[2048];
int length = 0;
while ((length = inputStream.read(buffer)) != -1)
{

System.out.println(&quot;Buffer Read of length: &quot; + length);
outputStream.write(buffer, 0, length);
}
inputStream.close();
outputStream.close();
}
catch(Exception e)
{
System.out.println(&quot;Exception: &quot; + e.getMessage());
}
}
}