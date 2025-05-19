import java.io.*;
import java.net.*;

class Client {
    public static void main(String[] args) {
        Socket sock = null;
        DataInputStream dis = null;
        PrintStream ps = null;

        System.out.println("Trying to connect...");

        try {
            // Connect to localhost at port 4000 (Server.PORT)
            sock = new Socket(InetAddress.getLocalHost(), Server.PORT);

            // Send a message to the server
            ps = new PrintStream(sock.getOutputStream());
            ps.println("Hi from client");

            // Read the response from the server
            DataInputStream is = new DataInputStream(sock.getInputStream());
            System.out.println(is.readLine());

            // Close input stream
            is.close();

        } catch (SocketException e) {
            System.out.println("SocketException: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("IOException: " + e.getMessage());
        } finally {
            try {
                if (ps != null) ps.close();
                if (sock != null) sock.close();
            } catch (IOException ie) {
                System.out.println("Close Error: " + ie.getMessage());
            }
        }
    }
}
