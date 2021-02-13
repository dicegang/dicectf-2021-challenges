#!/bin/sh
cat <<EOF >> $nsjail_cfg
mount {
  src: "/app/usr/share/seabios"
  dst: "/usr/share/seabios"
  is_bind: true
}
mount {
  src: "/app/usr/lib/ipxe"
  dst: "/usr/lib/ipxe"
  is_bind: true
}
EOF
