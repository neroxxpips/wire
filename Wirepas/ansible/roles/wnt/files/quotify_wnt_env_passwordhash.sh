#!/usr/bin/env bash

set -euo pipefail

input="wnt.env"
while IFS= read -r line
do
  if echo "$line" | grep -q "^WNT_.*_PASSWORD_HASH"; then
    if echo "$line" | grep -q "='"; then
      echo "$line"
    else
      echo "${line//=/=\'}'"
    fi
    else
      echo "$line"
  fi
done < "$input"
