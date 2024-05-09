#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef pair<int, int> pii;
typedef vector<vector<pii>> Graph;
const int INF = 1e9;

vector<int> dijkstras(const Graph &graph, int source)
{
    int n = graph.size();
    vector<int> dist(n, INF);
    priority_queue<pii, vector<pii>, greater<pii>> pq;

    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty())
    {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();

        if (d < dist[u])
            continue;

        for (auto &edge : graph[u])
        {
            int v = edge.first;
            int w = edge.second;

            if (dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

vector<pair<pair<int, int>, int>> primsMST(const Graph &graph, int source)
{
    int n = graph.size();
    vector<bool> visited(n, false);
    vector<int> parent(n, -1);
    vector<int> weight(n, INF);

    vector<pair<pair<int, int>, int>> mstEdges;

    weight[source] = 0;
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, source});

    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();

        if (visited[u])
            continue;

        visited[u] = true;

        if (parent[u] != -1)
            mstEdges.push_back({{parent[u], u}, weight[u]});

        for (const auto &edge : graph[u])
        {
            int v = edge.first;
            int w = edge.second;

            if (!visited[v] && w < weight[v])
            {
                weight[v] = w;
                parent[v] = u;
                pq.push({w, v});
            }
        }
    }
    return mstEdges;
}

int main()
{
    int n, m;
    cout << "Enter the Number of Vertex: ";
    cin >> n;

    cout << "\nEnter the Number of Edges: ";
    cin >> m;

    map<char, int> vertexIndex;
    Graph graph(n);

    cout << "Enter the Labels for Routers: ";
    for (int i = 0; i < n; i++)
    {
        char label;
        cin >> label;
        vertexIndex[label] = i;
    }

    cout << "Enter the Links and Weights (From To Weight): ";
    for (int i = 0; i < m; i++)
    {
        char from, to;
        int weight;
        cin >> from >> to >> weight;
        graph[vertexIndex[from]].push_back({vertexIndex[to], weight});
        graph[vertexIndex[to]].push_back({vertexIndex[from], weight});
    }

    char sourceLabel, destinationLabel;
    cout << "Enter the Source Node: ";
    cin >> sourceLabel;
    int source = vertexIndex[sourceLabel];

    vector<pair<pair<int, int>, int>> mstEdges = primsMST(graph, source);

    cout << "Minimum Spanning Tree Nodes: \n";

    for (const auto &edge : mstEdges)
    {
        char from = edge.first.first + 'A';
        char to = edge.first.second + 'A';
        int weight = edge.second;

        cout << from << to << weight << endl;
    }

    return 0;
}