import java.io.*;

class Main
{
    public static void main (String [] args)
    {   try
        {
            BufferedWriter w=new BufferedWriter (new FileWriter("two.txt"));
            w.write("Hello World!\n");
            w.write("This is buffered written file.");
            w.newLine();
            w.close();
            System.out.println("File written successfully");
        }
        catch (Exception e)
        {
            System.out.println("Error occured while writing...");
        }
    }
}