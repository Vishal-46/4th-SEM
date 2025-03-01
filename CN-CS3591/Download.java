import java.io.*;
import java.net.URL;

public class Download {
    public static void main(String[] args) throws Exception {
        try {
            String fileName = "digital_image_processing.jpg";
            String website = "http://tutorialspoint.com/java_dip/images/" + fileName;

            System.out.println("Downloading File From: " + website);
            
            URL url = new URL(website);
            InputStream inputStream = url.openStream();
            OutputStream outputStream = new FileOutputStream(fileName);

            byte[] buffer = new byte[2048];
            int length = 0;

            while ((length = inputStream.read(buffer)) != -1) {
                System.out.println("Buffer Read of length: " + length);
                outputStream.write(buffer, 0, length);
            }

            inputStream.close();
            outputStream.close();
        } 
        catch (Exception e) {
            System.out.println("Exception: " + e.getMessage());
        }
    }
}
