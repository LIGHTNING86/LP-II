#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

const int INF = 1e9;

typedef pair<int, int> pii;        // Pair of vertex and distance
typedef vector<vector<pii>> Graph; // Adjacency list representation of graph

// Dijkstra's algorithm implementation
vector<int> dijkstra(const Graph &graph, int source)
{
    int n = graph.size();                              // Number of vertices
    vector<int> dist(n, INF);                          // Initialize distances to all vertices as INF
    priority_queue<pii, vector<pii>, greater<pii>> pq; // Min-heap for efficient retrieval of minimum distance

    dist[source] = 0;     // Distance from source to itself is 0
    pq.push({0, source}); // Push the source vertex with distance 0 into the priority queue

    while (!pq.empty())
    {
        int u = pq.top().second; // Get the vertex with the smallest distance
        int d = pq.top().first;  // Get the corresponding distance
        pq.pop();                // Remove the vertex from the priority queue

        // If the distance to u from source is greater than the current minimum distance, skip it
        if (d > dist[u])
            continue;

        // Traverse through all neighbors of vertex u
        for (auto &edge : graph[u])
        {
            int v = edge.first;  // Neighbor vertex
            int w = edge.second; // Weight of edge (u, v)

            // Relaxation step: If a shorter path to v is found through u, update the distance to v
            if (dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w; // Update the distance to v
                pq.push({dist[v], v}); // Push v with its updated distance into the priority queue
            }
        }
    }

    return dist; // Return the shortest distances from source to all vertices
}

int main()
{
    int n, m;
    cout << "Enter the Number of Routers and Paths: ";
    cin >> n >> m;

    Graph graph(n);             // Initialize the graph with n vertices
    map<char, int> vertexIndex; // Map to store the index of vertices by their labels

    cout << "Enter Router Name for " << n << " Nodes: ";
    for (int i = 0; i < n; ++i)
    {
        char label;
        cin >> label;
        vertexIndex[label] = i; // Map the label to its corresponding index
    }

    cout << "Enter Path - (From To Weight):" << endl;
    for (int i = 0; i < m; ++i)
    {
        char from, to;
        int weight;
        cin >> from >> to >> weight;
        graph[vertexIndex[from]].push_back({vertexIndex[to], weight}); // Add the edge to the adjacency list
    }

    char sourceLabel, destinationLabel;
    cout << "Enter Source Router Label: ";
    cin >> sourceLabel;
    int source = vertexIndex[sourceLabel]; // Get the index of the source vertex

    vector<int> distances = dijkstra(graph, source); // Compute the shortest distances from the source

    cout << "Do you want to calculate the Shortest Path to a specific destination? (Y/N): ";
    char choice;
    cin >> choice;

    if (toupper(choice) == 'Y')
    {
        cout << "Enter Destination Router Label: ";
        cin >> destinationLabel;
        int destination = vertexIndex[destinationLabel]; // Get the index of the destination vertex

        cout << "Shortest Distance from Router " << sourceLabel << " to Router " << destinationLabel << " is: ";
        if (distances[destination] == INF)
        {
            cout << "INF" << endl; // If no path exists, print INF
        }
        else
        {
            cout << distances[destination] << endl; // Print the shortest distance to the destination vertex
        }
    }
    else
    {
        cout << "Shortest Distances from Router " << sourceLabel << ":" << endl;
        for (const auto &pair : vertexIndex)
        {
            char label = pair.first;
            int index = pair.second;
            cout << "Router " << label << ": ";
            if (distances[index] == INF)
            {
                cout << "INF" << endl; // If no path exists, print INF
            }
            else
            {
                cout << distances[index] << endl; // Print the shortest distance to the vertex
            }
        }
    }

    return 0;
}