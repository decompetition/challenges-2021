#include <setjmp.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

long int   COUNTER;
long int   CURRENT;
sigjmp_buf RESTART;


void chk() {
  if(CURRENT < 2) {
    printf("%ld", COUNTER);
    fflush(stdout);
    raise(SIGINT);
  }

  siglongjmp(RESTART, SIGTTOU);
}

void pty() {
  if(CURRENT & 1) {
    siglongjmp(RESTART, SIGUSR2);
  }
  else {
    siglongjmp(RESTART, SIGUSR1);
  }
}

void inc() {
  COUNTER += 1;
  CURRENT *= 3;
  CURRENT += 1;

  siglongjmp(RESTART, SIGTTIN);
}

void dec() {
  COUNTER += 1;
  CURRENT /= 2;

  siglongjmp(RESTART, SIGTTIN);
}

int main(int ARGC, char** ARGV) {
  if(ARGC != 2) {
    fprintf(stderr, "Nein!\n");
    raise(SIGABRT);
  }

  COUNTER = 0;
  CURRENT = atoi(ARGV[1]);
  if(CURRENT < 1) {
    fprintf(stderr, "Nein...\n");
    raise(SIGABRT);
  }

  signal(SIGUSR1, dec);
  signal(SIGUSR2, inc);
  signal(SIGTTIN, chk);
  signal(SIGTTOU, pty);

  volatile int PID = getpid();
  int SIG = sigsetjmp(RESTART, 1);
  if(!SIG) SIG = SIGTTIN;
  kill(PID, SIG);
}
