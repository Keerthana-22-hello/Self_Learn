import java.io.FileReader;
import java.io.IOException;

class Main
{
    public static void main (String [] args)
    {
        try
        {
            FileReader read = new FileReader ("one.txt");
            int ch;
            while((ch=read.read()) != -1)
            {
                System.out.print((char) ch);
            }
        }
        catch (IOException e)
        {
            System.out.println("Error occured. File not found.");
        }
    }
}