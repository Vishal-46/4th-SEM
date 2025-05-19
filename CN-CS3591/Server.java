import java.net.*;
import java.io.*;

public class Server {
    public static final int PORT = 4000;

    public static void main(String[] args) {
        ServerSocket sersock = null;
        Socket sock = null;

        try {
            sersock = new ServerSocket(PORT);
            System.out.println("Server Started: " + sersock);

            try {
                sock = sersock.accept();
                System.out.println("Client Connected: " + sock);

                DataInputStream ins = new DataInputStream(sock.getInputStream());
                System.out.println(ins.readLine());

                PrintStream ios = new PrintStream(sock.getOutputStream());
                ios.println("Hello from server");

                ios.close();
                ins.close();
                sock.close();
            } catch (SocketException se) {
                System.out.println("Server Socket problem: " + se.getMessage());
            }

        } catch (Exception e) {
            System.out.println("Couldn't start: " + e.getMessage());
        }

        if (sock != null) {
            System.out.println("Connection from: " + sock.getInetAddress());
        }
    }
}
