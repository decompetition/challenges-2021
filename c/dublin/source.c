#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define XOR(a, b) ((uintptr_t) (a) ^ (uintptr_t) (b))

const char SUFFIXES[3][3] = {"st", "nd", "rd"};

typedef struct {
  uintptr_t ptr;
  int       val;
} Node;


Node* insert(int val, Node* l, Node* r) {
  Node* node = (Node*) malloc(sizeof(Node));
  node->ptr  = XOR(l, r);
  node->val  = val;

  if(l) l->ptr ^= XOR(node, r);
  if(r) r->ptr ^= XOR(node, l);
  return node;
}

void walk(Node* curr, const char* type) {
  Node* prev = NULL;

  for(int i = 1; curr; ++i) {
    const char* suffix = "th";
    if(i % 100 < 10 || i % 100 > 20) {
      int index = (i - 1) % 10;
      if(index < 3) {
        suffix = SUFFIXES[index];
      }
    }

    printf("%5d%s %s is %d\n", i, suffix, type, curr->val);

    Node* temp = prev;
    prev = curr;
    curr = (Node*) XOR(curr->ptr, temp);
  }
}

int main(int argc, char** argv) {
  Node* head = NULL;
  Node* tail = NULL;

  Node* l = NULL;
  Node* c = NULL;
  Node* r = NULL;

  while(1) {
    int val = 0;
    if(scanf("%d", &val) != 1) {
      break;
    }

    while(c && c->val > val) {
      r = c;
      c = l;
      if(l) l = (Node*) XOR(l->ptr, r);

      // printf("Moved L:  %18p %18p %18p\n", l, c, r);
    }

    while(c && c->val < val) {
      l = c;
      c = r;
      if(r) r = (Node*) XOR(r->ptr, l);

      // printf("Moved R:  %18p %18p %18p\n", l, c, r);
    }

    if(c) {
      if(c->val <= val) l = c;
      if(c->val >  val) r = c;
    }

    c = insert(val, l, r);
    if(!l) head = c;
    if(!r) tail = c;
  }

  if(head && tail) {
    printf("Forward:\n");
    walk(head, "smallest");

    printf("Reverse:\n");
    walk(tail, "largest");
  }

  return 0;
}
