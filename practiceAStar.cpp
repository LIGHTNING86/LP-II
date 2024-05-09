#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

class Node
{
public:
    int x, y;
    int f, g, h;
    bool obstacle;
    bool closed;
    Node *parent;

    Node(int x, int y, bool obstacle = false) : x(x), y(y), obstacle(obstacle), closed(false), parent(nullptr)
    {
    }

    bool isObstacle() const
    {
        return obstacle;
    }
};

int heuristic(Node *start, Node *end)
{
    return abs(start->x - end->x) + abs(start->y - end->y);
}

vector<Node *> aSitara(vector<vector<Node>> &grid, Node *start, Node *end)
{
    auto compareNodes = [](Node *a, Node *b)
    {
        return a->f > b->f;
    };

    priority_queue<Node *, vector<Node *>, decltype(compareNodes)> openList(compareNodes);

    set<Node *> openSet;

    start->g = 0;
    start->h = heuristic(start, end);
    start->f = start->g + start->h;
    openList.push(start);
    openSet.insert(start);

    while (!openList.empty())
    {
        Node *current = openList.top();
        openList.pop();

        if (current == end)
        {
            vector<Node *> path;
            while (current != nullptr)
            {
                path.push_back(current);
                current = current->parent;
            }

            reverse(path.begin(), path.end());
            return path;
        }

        current->closed = true;

        for (int dx = -1; dx <= 1; dx++)
        {
            for (int dy = -1; dy <= 1; dy++)
            {
                if (dx == 0 && dy == 0)
                    continue;

                int x = current->x + dx;
                int y = current->y + dy;

                if (x >= 0 && x < grid.size() && y >= 0 && y < grid[0].size())
                {
                    Node *child = &grid[x][y];

                    if (!child->isObstacle() && !child->closed)
                    {
                        int g = current->g + 1;
                        int h = heuristic(child, end);
                        int f = g + h;

                        if (openSet.find(child) != openSet.end() && g >= child->g)
                            continue;

                        child->parent = current;
                        child->g = g;
                        child->h = h;
                        child->f = f;

                        openList.push(child);
                        openSet.insert(child);
                    }
                }
            }
        }
    }
    return {};
}

void displayGrid(vector<vector<Node>> &grid)
{
    vector<Node> obstacles;
    for (const auto row : grid)
    {
        for (const auto node : row)
        {
            if (node.obstacle)
            {
                cout << "0 ";
                obstacles.push_back(node);
            }
            else
                cout << "1 ";
        }
        cout << endl;
    }
    cout << endl;

    for (auto &node : obstacles)
    {
        cout << "Obstacle at: (" << node.x << ", " << node.y << ")\n";
    }
    cout << endl;
}

void displayGridWithPath(const vector<vector<Node>> &grid, const vector<Node *> &path)
{
    for (int i = 0; i < grid.size(); i++)
    {
        for (int j = 0; j < grid[i].size(); j++)
        {
            if (grid[i][j].obstacle)
            {
                cout << "0 ";
            }
            else if (find(path.begin(), path.end(), &grid[i][j]) != path.end())
            {
                cout << "# ";
            }
            else
                cout << "1 ";
        }
        cout << endl;
    }
    cout << endl;
}

int main()
{

    vector<vector<Node>> grid(10, vector<Node>(10, Node(0, 0)));

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            grid[i][j] = Node(i, j);
        }
    }

    int obstacleCount;
    cout << "Enter the Number of Obstacles: ";
    cin >> obstacleCount;

    cout << "Enter the Positions of Obstacles:";
    for (int i = 0; i < obstacleCount; i++)
    {
        int row, col;
        cout << "Obstacle " << i + 1 << " : ";
        cin >> row >> col;
        grid[row][col].obstacle = true;
    }

    Node *start;
    Node *end;

    cout << "\n1. Keep Start Position as (0, 0) and Destination Position as (9, 9)";
    cout << "\n2. Input New Start and Destination Co-ordinates\n";
    int choice;
    cout << "\nEnter Your Choice: ";
    cin >> choice;

    if (choice == 1)
    {
        start = &grid[0][0];
        end = &grid[9][9];
    }
    else if (choice == 2)
    {
        int start_x, start_y, end_x, end_y;
        cout << "\nEnter Co-ordinates for Start Position: ";
        cin >> start_x >> start_y;

        cout << "\nEnter Co-ordinates for Destination Position: ";
        cin >> end_x >> end_y;

        start = &grid[start_x][start_y];
        end = &grid[end_x][end_y];
    }

    vector<Node *> path = aSitara(grid, start, end);
    displayGrid(grid);

    if (!path.empty())
    {
        cout << "Path Found: \n";
        for (Node *node : path)
        {
            cout << "( " << node->x << ", " << node->y << " )" << endl;
            cout << "f = " << node->f << ", g = " << node->g << ", h = " << node->h << endl;
        }
    }
    else
        cout << "No Path Found!!!";

    displayGridWithPath(grid, path);

    return 0;
}