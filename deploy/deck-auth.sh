#!/bin/sh
# Builds the nginx config from DECK_PASSWORD (runs before nginx starts).
set -e

if [ -n "$DECK_PASSWORD" ]; then
    TOKEN=$(printf 'vbui:%s' "$DECK_PASSWORD" | sha256sum | cut -d' ' -f1)
    echo "deck-auth: password protection enabled"
else
    # No password set: lock the deck with a random token nobody can match.
    TOKEN=$(head -c 32 /dev/urandom | sha256sum | cut -d' ' -f1)
    echo "deck-auth: WARNING DECK_PASSWORD is not set - the deck is locked"
fi

sed "s/__AUTH_TOKEN__/$TOKEN/" /etc/nginx/deck.conf.template > /etc/nginx/conf.d/default.conf
