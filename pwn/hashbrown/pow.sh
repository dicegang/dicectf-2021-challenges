#!/bin/sh

set -eu

bits=${HASHCASH_BITS}

nonce=$(head -c12 /dev/urandom | base64)

cat <<EOF
Send the output of: hashcash -mb${bits} ${nonce}
EOF

if head -n1 | hashcash -cqb${bits} -df /dev/null -r "${nonce}"; then
	exec /app/run.sh
else
	echo stamp verification failed
fi
