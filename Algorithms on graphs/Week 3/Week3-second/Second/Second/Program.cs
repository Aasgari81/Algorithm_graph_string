using System;
using System.Collections.Generic;

class Reachability
{

    public static void Main(string[] args)
    {
        Reachability q = new Reachability();
        string[] s = Console.ReadLine().Split();
        int n = int.Parse(s[0]);
        int m = int.Parse(s[1]);
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++)
        {
            adj[i] = new List<int>();
        }
        for (int i = 0; i < m; i++)
        {
            string[] input = Console.ReadLine().Split();
            int x = int.Parse(input[0]) - 1;
            int y = int.Parse(input[1]) - 1;
            adj[x].Add(y);
            adj[y].Add(x);
        }
        Console.WriteLine(q.reach(adj, 1, 0));


    }
    public int reach(List<int>[] adj, int start, int end)
    {
        Queue<int> q = new Queue<int>();
        Dictionary<int, string> Coloring = new Dictionary<int, string>();
        if (adj.Length == 1) return 1;
        for (int j = 0; j <= adj.Length; j++)
        {
            Coloring[j] = "None";
        }
        
        q.Enqueue(start);
        string current_color = "Red";
        Coloring[start] = "Red";
        while (q.Count > 0)
        {

            int k = q.Dequeue();

            if (Coloring[k] == "Red")
            {
                current_color = "Blue";
            }
            else if (Coloring[k] == "Blue")
            {
                current_color = "Red";
            }



            foreach (int o in adj[k])
            {
                if (Coloring[o] == "None")
                {
                    q.Enqueue(o);
                    Coloring[o] = current_color;
                }
                else
                {
                    if (Coloring[o] == Coloring[k])
                    {
                        int f = o;
                        int m = k;
                        return 0;
                    }
                }
            }
            

        }
        return 1;

    }

}
