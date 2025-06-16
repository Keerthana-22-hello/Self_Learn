import java.io.*;

class Main
{
    public static void main (String [] args)
    {
          try
        {   FileInputStream fis = new FileInputStream("photo.png");
            FileOutputStream fos = new FileOutputStream("copied.png");
            int byteRead;
            while((byteRead = fis.read())!= -1)
            {
                fos.write(byteRead);
            }
            fis.close();
            fos.close();

            System.out.println("Data copied successfully...");
        }
    catch (Exception e)
    {
        System.out.println("Error occured while copying...");
    }
    }
}