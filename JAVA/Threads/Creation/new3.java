class Main
{
    public static void main (String [] args)
    {
        Thread t=new Thread (new Runnable()
        {
            public void run()
            {
                System.out.println("Hello World!");
            }
        });
        Thread t2 = new Thread (new Runnable()
        {
            public void run()
            {
                System.out.println("Hello Wrold 2 ");
            }
        });
        t.start(); t2.start();
    }
}