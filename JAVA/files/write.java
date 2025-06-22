import java.io.FileWriter;
import java.io.IOException;

class Main
{
    public static void main (String [] args)
    {   try
        {
            FileWriter f=new FileWriter("one.txt");
            f.write("Hello World\n");
            f.write("This is my first program in filewriter.");
            f.close();
            System.out.println("File written successfully.");
        }
        catch (IOException e)
        {
            System.out.println("Error occured.");
        }
    }
}