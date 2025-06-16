class share
{   
    Runnable print()
    {   return ()->
        {System.out.println("Hello World !");};
        
    };
}
class Main
{
    public static void main (String [] args)
    {
        share s=new share();
        Thread t=new Thread(s.print());
        t.start();
    }
}