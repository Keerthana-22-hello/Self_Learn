import java.io.*;

class Main{
    public static void main (String [] args)
    {   try
        {
            BufferedReader r= new BufferedReader(new FileReader("two.txt"));
            String line;
            while((line=r.readLine())!=null)
            {
                System.out.println(line);
            }
            r.close();
            System.out.println("File read successfully...");
        }
        catch (Exception e)
        {
            System.out.println("Error occured while reading file...");
        }
    }
}