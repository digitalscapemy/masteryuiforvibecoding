FROM nginx:1.27-alpine

# Password gate: set DECK_PASSWORD in the container environment.
COPY deploy/nginx.conf.template /etc/nginx/deck.conf.template
COPY deploy/deck-auth.sh /docker-entrypoint.d/30-deck-auth.sh
RUN sed -i 's/\r$//' /docker-entrypoint.d/30-deck-auth.sh /etc/nginx/deck.conf.template \
 && chmod +x /docker-entrypoint.d/30-deck-auth.sh \
 && rm -f /etc/nginx/conf.d/default.conf

COPY index.html login.html /usr/share/nginx/html/
COPY slides /usr/share/nginx/html/slides
EXPOSE 80
