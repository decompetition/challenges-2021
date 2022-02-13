#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  struct Node* parent;
  int count;
} Node;

typedef struct {
  Node* a;
  Node* b;
  char  w;
} Edge;

typedef struct {
  int    w;
  int    h;
  void** data;
} Grid;

typedef struct {
  Grid* rooms;
  Grid* hwalls;
  Grid* vwalls;
} Maze;

Node* node_new() {
  Node* node   = (Node*) malloc(sizeof(Node));
  node->parent = node;
  node->count  = 0;
  return node;
}


Edge* edge_new(Node* a, Node* b) {
  Edge* edge = (Edge*) malloc(sizeof(Edge));
  edge->a = a;
  edge->b = b;
  edge->w = 0;
  return edge;
}


Grid* grid_new(int w, int h) {
  // printf("New Grid: %d x %d\n", w, h);
  Grid* grid = (Grid*) malloc(sizeof(Grid));
  grid->data = calloc(w * h,  sizeof(void*));
  grid->w = w;
  grid->h = h;
  return grid;
}

void* grid_get(const Grid* grid, int x, int y) {
  if(x < 0 || x >= grid->w) return NULL;
  if(y < 0 || y >= grid->h) return NULL;
  return grid->data[grid->w * y + x];
}

void grid_set(Grid* grid, int x, int y, void* item) {
  // printf("Grid Set: (%d, %d)\n", x, y);
  if(x < 0 || x >= grid->w) abort();
  if(y < 0 || y >= grid->h) abort();
  grid->data[grid->w * y + x] = item;
}


void fys(void** data, int n) {
  while(n) {
    int i = rand() % n--;
    void* t = data[n];
    data[n] = data[i];
    data[i] = t;
  }
}

Node* fin(Node* node) {
  if(node->parent != node) {
    node->parent = fin(node->parent);
  }

  return node->parent;
}

char uni(Node* a, Node* b) {
  Node* pa = fin(a);
  Node* pb = fin(b);
  if(pa == pb) return 0;

  if(pa->count > pb->count) {
    pa->count += pb->count;
    pb->parent = pa;
  }
  else {
    pb->count += pa->count;
    pa->parent = pb;
  }

  return 1;
}


Maze* plan_new(int w, int h, int p) {
  // printf("New Maze: %d x %d\n", w, h);
  Maze* maze   = (Maze*) malloc(sizeof(Maze));
  maze->vwalls = grid_new(w, h - 1);
  maze->hwalls = grid_new(w - 1, h);
  maze->rooms  = grid_new(w, h);

  Edge** temp = malloc((2 * h * w - w - h) * sizeof(void*));
  int    ndex = 0;

  for(int y = 0; y < h; ++y) {
    for(int x = 0; x < w; ++x) {
      Node* room = node_new();
      grid_set(maze->rooms, x, y, room);

      if(x) {
        Edge* wall = edge_new(room, grid_get(maze->rooms, x - 1, y));
        grid_set(maze->hwalls, x - 1, y, wall);
        temp[ndex++] = wall;
      }
      if(y) {
        Edge* wall = edge_new(room, grid_get(maze->rooms, x, y - 1));
        grid_set(maze->vwalls, x, y - 1, wall);
        temp[ndex++] = wall;
      }
    }
  }

  // Randomize!
  fys((void**) temp, ndex);
  for(int i = 0; i < ndex; ++i) {
    Edge* edge = temp[i];
    if(uni(edge->a, edge->b) || rand() % 100 < p) {
      edge->w = 1;
    }
  }

  free(temp);
  return maze;
}

void plan_out(const Maze* maze) {
  int H = maze->rooms->h;
  int W = maze->rooms->w;

  for(int y = 0; y < H; ++y) {
    // Draw vertical walls...
    for(int x = 0; x < W; ++x) {
      Edge* n = grid_get(maze->hwalls, x - 1, y - 1);
      Edge* w = grid_get(maze->vwalls, x - 1, y - 1);
      Edge* s = grid_get(maze->hwalls, x - 1, y);
      Edge* e = grid_get(maze->vwalls, x, y - 1);

      int   open  = 0;
      if(n) open += n->w;
      if(w) open += w->w;
      if(s) open += s->w;
      if(e) open += e->w;

      putchar((open == 4)? ' ' : '+');
      putchar((e && e->w)? ' ' : '-');

    }
    printf("+\n");

    // Draw horizontal walls...
    for(int x = 0; x < W; ++x) {
      Edge* w = grid_get(maze->hwalls, x - 1, y);
      putchar((w && w->w)? ' ' : '|');
      putchar(' ');
    }
    printf("|\n");
  }

  // Draw bottom wall (with doors)...
  printf("+ ");
  for(int x = W-2; x > 0; --x) {
    printf("+-");
  }
  printf("+ +\n");
}


int main(int argc, char** argv) {
  int w = 20;
  int h = 10;
  int p = 20;
  int s = 76;

  if(argc > 1) w = atoi(argv[1]);
  if(argc > 2) h = atoi(argv[2]);
  if(argc > 3) p = atoi(argv[3]);
  if(argc > 4) s = atoi(argv[4]);

  if(w < 2 || h < 1) {
    fprintf(stderr, "You'll never fit a cow in there.\n");
    return 1;
  }

  srand(s);
  Maze* maze = plan_new(w, h, p);
  plan_out(maze);
  return 0;
}
