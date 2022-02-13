#! /bin/sh
set -e

if [ $# -lt 2 ]; then
  echo "USAGE: $0 source binary [options]"
  exit 1
fi

source="$1"
binary="$2"
shift 2

# Linking with lld (instead of bfd) gives a 10x speedup!?
rustc -C "link-arg=-fuse-ld=lld" "$@" -o "$binary" "$source"
