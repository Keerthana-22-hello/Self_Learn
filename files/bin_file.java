import java.io.*;

class Main 
{
    public static void main (String [] args)
    {
        try
        {
            FileOutputStream f =new FileOutputStream("three.txt");
            String data = "Hello Love, this is binary file handling..";
            byte [] byteData = data.getBytes();
            f.write(byteData);
            f.close();
            System.out.println("Data written successfully...");
        }
        catch(IOException e)
        {
            System.out.println("Error occured while writing file");
        }
    }
}