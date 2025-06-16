import java.io.*;

class Main
{
    public static void main (String [] args)
    {   try
        {
            FileInputStream f=new FileInputStream ("three.txt");
            int i;
            System.out.println("Data read from file : ");
            while ((i=f.read())!=-1)
            {
                System.out.print((char)i);
            }
            f.close();
            System.out.println("\nData read successfully...");
        }
        catch (IOException e)
        {
            System.out.println("Error occured while reading...");
        }
    }
}