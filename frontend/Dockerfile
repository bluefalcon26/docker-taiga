##############################################################
##
##
##  Taiga-front
##
##
###############################################################

FROM nginx

RUN mkdir -p /taiga
WORKDIR /taiga

# checkout source code
RUN git clone https://github.com/taigaio/taiga-front-dist && git checkout stable

# copy configuation files
COPY conf.json /taiga/conf.json
COPY run.sh /taiga/run.sh
COPY nginx.conf /etc/nginx/nginx.conf
COPY taiga.conf /etc/nginx/conf.d/default.conf

RUN chmod -R 755 /taiga && chmod +x /taiga/run.sh

# run the server
CMD ["/taiga/run.sh"]
