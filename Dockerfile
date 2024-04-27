FROM quay.io/centos/centos:stream9
RUN yum install -y sudo
RUN yum install -y epel-release
RUN yum install -y python
RUN yum install -y libreoffice-core.aarch64
COPY libreoffice-filters-7.1.8.1-11.el9.aarch64.rpm .
COPY libreoffice-xsltfilter-7.1.8.1-11.el9.aarch64.rpm .
RUN yum install -y libreoffice-xsltfilter-7.1.8.1-11.el9.aarch64.rpm
RUN yum install -y libreoffice-filters-7.1.8.1-11.el9.aarch64.rpm
RUN rm libreoffice-xsltfilter-7.1.8.1-11.el9.aarch64.rpm
RUN rm libreoffice-filters-7.1.8.1-11.el9.aarch64.rpm
RUN yum clean all
WORKDIR /app
RUN chmod 777 /app
RUN python -m venv /opt/venv
COPY requirements.txt .
RUN /opt/venv/bin/pip install -r requirements.txt
COPY app.py .
COPY gunicorn.py .
COPY .env .
CMD /opt/venv/bin/gunicorn -c gunicorn.py app:app
