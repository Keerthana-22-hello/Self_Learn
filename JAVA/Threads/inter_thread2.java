class SharedResource
{   int data;
    boolean available=false;
    void Producer(int value)
    {
        synchronized (this)
        {   int i;
            while(available)
            {
                try
                {
                    wait();
                }
                catch (InterruptedException e)
                {
                    System.out.println("Producer interrupted.");
                }
                
                
            }
            data=value;
            available=true;
            notify();
            System.out.println("Produced data : "+data);
        }
    }
    void Consumer()
    {
        synchronized (this)
        {
            while (!available)
            {
                try
                {
                    wait();
                }
                catch(InterruptedException e){
                    System.out.println("Consumer Interupted.");
                }
            }
            available=false;
            notify();
            System.out.println("Consumed data : "+data);
        }
    }

    Runnable consume()  // creating thread
    {
        return() ->
        { int i;
            for (i=1;i<=5;i++)
            {
                Consumer();
                try
                {
                    Thread.sleep(1000);
                }
                catch (InterruptedException e)
                {
                    System.out.println("Production interrupted");
                }
            }
        };
    };
    
    /*
    Runnable produce()  // thread creation
    {
        return() ->
        {   int j;
            for (j=1;j<=5;j++)
            {
                Producer(j);
                try{
                    Thread.sleep(1000);
                }
                catch (InterruptedException e)
                {
                    System.out.println("Production interrupted");
                }
            }
        };
    };*/
}


class Main
{
    public static void main (String [] args)
    {
        SharedResource sr=new SharedResource();
        
        Thread p = new Thread (() -> {
            int j;
            for(j=1;j<=5;j++)
            {
                sr.Producer(j);
                try
                {
                    Thread.sleep(1000);
                }
                catch (InterruptedException e)
                {
                    System.out.println("Production interrupted.");
                }
            }
        });
        Thread c = new Thread (sr.consume());
        p.start();c.start();
    }
}
