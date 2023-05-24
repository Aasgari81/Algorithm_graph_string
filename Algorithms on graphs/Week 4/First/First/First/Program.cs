using System;
using System.Buffers.Text;
using System.Collections.Generic;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.ExceptionServices;
using static MainClass;

public class MainClass
{

    
    public static void Main()
    {
        int n, m;
        string[] input = Console.ReadLine().Split();
        n = int.Parse(input[0]);
        m = int.Parse(input[1]);
        List<List<int>> adj = new List<List<int>>(n);
        List<List<int>> cost = new List<List<int>>(n);
        for (int i = 0; i < n; i++)
        {
            adj.Add(new List<int>());
            cost.Add(new List<int>());
        }
        for (int i = 0; i < m; i++)
        {
            input = Console.ReadLine().Split();
            int x = int.Parse(input[0]) - 1;
            int y = int.Parse(input[1]) - 1;
            int w = int.Parse(input[2]);
            adj[x].Add(y);
            cost[x].Add(w);
        }
        input = Console.ReadLine().Split();
        int s = int.Parse(input[0]) - 1;
        int t = int.Parse(input[1]) - 1;
        Console.WriteLine(Distance(adj, cost, s, t));
    }

    public static long Distance(List<List<int>> adj, List<List<int>> cost, int s, int t)
    {   
        int VertexNumbers = adj.Count;
        int[] prev = new int[VertexNumbers];
        //          vertex cost
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
        int[] dist = new int[VertexNumbers];
        for (int i =0;i < VertexNumbers; i++)
        {
            dist[i] = 2147483647;
        }
        dist[s] = 0;
        prev[s] = s;
        pq.Enqueue(s, 0);
        for (int i = 0; i < VertexNumbers; i++)
        {
            pq.Enqueue(i, dist[i]);
        }
        while (pq.Count > 0)
        {
            int u = pq.Dequeue();
            for (int i = 0; i < adj[u].Count;i++)
            {
                int v = adj[u][i];
                if (dist[v] > dist[u] + cost[u][i])
                {
                    pq.ChangePriority(v, dist[u] + cost[u][i]);
                    pq.Remove(v);
                    dist[v] = dist[u] + cost[u][i];
                    prev[v] = u;
                }
            }
        }


        return dist[t];


    }
}
