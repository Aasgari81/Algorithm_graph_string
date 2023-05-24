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
            int x = int.Parse(input[0]) -1;
            int y = int.Parse(input[1]) -1;
            adj[x].Add(y);
            adj[y].Add(x);
        }
        string[] xy = Console.ReadLine().Split();
        int start = int.Parse(xy[0]) - 1;
        int end = int.Parse(xy[1]) -1;
        Console.WriteLine(q.reach(adj, start, end));
        
        
    }
    public int reach(List<int>[] adj, int start, int end)
    {
        Queue<int> q = new Queue<int>();
        Dictionary<int, bool> check = new Dictionary<int, bool>();
        int[] dist = new int[adj.Length];
        for (int i = 0; i < dist.Length; i++)
        {
            dist[i] = 2147483647;
        }

        for (int j = 0; j <= adj.Length;j++)
        {
            check[j] = false;
        }
        if (start == end)
        {
            return 0;
        }
        dist[start] = 0;
        q.Enqueue(start);
        while (q.Count > 0)
        {

            int k = q.Dequeue();
            check[k] = true;
            foreach (int o in adj[k])
            {
                if (check[o] == false)
                {
                    q.Enqueue(o);
                    dist[o] = dist[k] + 1;
                }
                check[o] = true;
            }


        }
        if (dist[end] == 2147483647)
        {
            return -1;
        }
        return dist[end];

        
       
    }

}