FROM lambdalinux/baseimage-amzn:2017.03-004

RUN yum update -y && yum upgrade -y
RUN yum install -y python36-devel python36-pip gcc gcc-c++
RUN yum install zip unzip
RUN yum clean all

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# install system libraries
RUN yum makecache fast
RUN yum install -y cmake automake glib2-devel
RUN yum install -y wget tar unzip zip bzip2 gzip findutils yum-utils openssl-devel
RUN yum install -y zlib-devel curl-devel libcurl-devel libjpeg-devel libpng-devel liblzma-dev libmpc-devel mpfr-devel gmp-devel
RUN yum clean all

# Install GDAL and deps
ENV APP_DIR /tmp/src
RUN mkdir $APP_DIR

# versions of packages
ENV \
  PKGCONFIG_VERSION=0.29.2 \
  PROJ_VERSION=5.1.0 \
  GEOS_VERSION=3.6.2 \
  OPENJPEG_VERSION=2.3.0 \
  WEBP_VERSION=1.0.0 \
  ZSTD_VERSION=1.3.4 \
  GDAL_VERSION=2.4.0

# pkg-config
RUN cd $APP_DIR \
   && wget -q https://pkg-config.freedesktop.org/releases/pkg-config-$PKGCONFIG_VERSION.tar.gz \
   && tar xvf pkg-config-$PKGCONFIG_VERSION.tar.gz \
   && cd pkg-config-$PKGCONFIG_VERSION \
   && ./configure CFLAGS="-O2 -Wl,-S" --prefix=$APP_DIR/local \
   && make -j4 --quiet && make install --quiet && make clean --quiet \
   && rm -rf $APP_DIR/pkg-config-$PKGCONFIG_VERSION.tar.gz $APP_DIR/pkg-config-$PKGCONFIG_VERSION

# PROJ
RUN cd $APP_DIR \
   && wget -q http://download.osgeo.org/proj/proj-$PROJ_VERSION.tar.gz \
   && tar -zvxf proj-$PROJ_VERSION.tar.gz \
   && cd proj-$PROJ_VERSION \
   && ./configure CFLAGS="-O2 -Wl,-S" --prefix=$APP_DIR/local \
   && make -j4 --quiet && make install --quiet && make clean --quiet \
   && rm -rf $APP_DIR/proj-$PROJ_VERSION.tar.gz $APP_DIR/proj-$PROJ_VERSION

# GEOS
RUN cd $APP_DIR \
  && wget -q http://download.osgeo.org/geos/geos-$GEOS_VERSION.tar.bz2 \
  && tar jxf geos-$GEOS_VERSION.tar.bz2 \
  && cd geos-$GEOS_VERSION \
  && CFLAGS="-O2 -Wl,-S" CXXFLAGS="-O2 -Wl,-S" ./configure --prefix=$APP_DIR/local \
  && make -j4 --quiet && make install --quiet && make clean --quiet \
  && rm -rf $APP_DIR/geos-$GEOS_VERSION $APP_DIR/geos-$GEOS_VERSION.tar.bz2

# OPENJPEG
RUN cd $APP_DIR \
  && wget -q https://github.com/uclouvain/openjpeg/archive/v$OPENJPEG_VERSION.tar.gz \
  && tar -zvxf v$OPENJPEG_VERSION.tar.gz \
  && cd openjpeg-$OPENJPEG_VERSION/ \
  && mkdir build \
  && cd build \
  && cmake .. -DBUILD_THIRDPARTY:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$APP_DIR/local \
  && make install --quiet && make clean --quiet \
  && rm -rf $APP_DIR/openjpeg-$OPENJPEG_VERSION $APP_DIR/v$OPENJPEG_VERSION.tar.gz

# WEBP
RUN cd $APP_DIR\
    && wget -q https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${WEBP_VERSION}.tar.gz \
    && tar xzf libwebp-${WEBP_VERSION}.tar.gz \
    && cd libwebp-${WEBP_VERSION} \
    && CFLAGS="-O2 -Wl,-S" ./configure --prefix=$APP_DIR/local/ \
    && make -j4 && make install --quiet && make clean --quiet \
    && rm -rf $APP_DIR/libwebp-${WEBP_VERSION} $APP_DIR/libwebp-${WEBP_VERSION}.tar.gz

# ZSTD
RUN cd $APP_DIR \
  && wget -q https://github.com/facebook/zstd/archive/v${ZSTD_VERSION}.tar.gz \
  && tar -zvxf v${ZSTD_VERSION}.tar.gz \
  && cd zstd-${ZSTD_VERSION} \
  && make -j4 --quiet PREFIX=$APP_DIR/local/ ZSTD_LEGACY_SUPPORT=0 CFLAGS=-O1 \
  && make install --quiet PREFIX=$APP_DIR/local/ ZSTD_LEGACY_SUPPORT=0 CFLAGS=-O1 \
  && make clean --quiet \
  && rm -rf $APP_DIR/v${ZSTD_VERSION}.tar.gz $APP_DIR/zstd-${ZSTD_VERSION}

ENV LD_LIBRARY_PATH=$APP_DIR/local/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH=$APP_DIR/local/lib/pkgconfig/

RUN cd $APP_DIR \
  && wget -q https://github.com/osgeo/gdal/archive/master.zip \
  && unzip master.zip \
  && cd gdal-master/gdal \
  && CFLAGS="-O2 -Wl,-S" CXXFLAGS="-O2 -Wl,-S" ./configure \
      --prefix=$APP_DIR/local \
      --with-proj=$APP_DIR/local \
      --with-geos=$APP_DIR/local/bin/geos-config \
      --with-openjpeg \
      --with-webp=$APP_DIR/local \
      --with-zstd=$APP_DIR/local \
      --with-threads \
      --disable-debug \
      --with-jpeg \
      --with-hide-internal-symbols \
      --with-curl \
      --without-bsb \
      --without-cfitsio \
      --without-cryptopp \
      --without-ecw \
      --without-expat \
      --without-fme \
      --without-freexl \
      --without-gif \
      --without-gif \
      --without-gnm \
      --without-grass \
      --without-grib \
      --without-hdf4 \
      --without-hdf5 \
      --without-idb \
      --without-ingres \
      --without-jasper \
      --without-jp2mrsid \
      --without-kakadu \
      --without-libgrass \
      --without-libkml \
      --without-libtool \
      --without-mrf \
      --without-mrsid \
      --without-mysql \
      --without-netcdf \
      --without-odbc \
      --without-ogdi \
      --without-pcidsk \
      --without-pcraster \
      --without-pcre \
      --without-perl \
      --without-pg \
      --without-png \
      --without-python \
      --without-qhull \
      --without-sde \
      --without-sqlite3 \
      --without-xerces \
      --without-xml2 \
    && make -j4 --quiet && make install --quiet && make clean --quiet \
    && rm -rf $APP_DIR/master.zip $APP_DIR/gdal-master

ENV GDAL_DATA=$APP_DIR/local/share/gdal
ENV PROJ_LIB=$APP_DIR/local/share/proj
ENV GDAL_CONFIG=$APP_DIR/local/bin/gdal-config
ENV GEOS_CONFIG=$APP_DIR/local/bin/geos-config

RUN pip-3.6 install pip -U

RUN pip3 install numpy --no-binary numpy

################################################################################
# Install Python dependencies
COPY pyskel /tmp/app/pyskel
COPY README.rst /tmp/app/README.rst
COPY setup.py /tmp/app/setup.py

RUN pip3 install /tmp/app/ -t /tmp/vendored --no-binary numpy,rasterio -U
################################################################################

RUN du -sh /tmp/vendored

# This is the list of available modules on AWS lambda Python 3
# ['boto3', 'botocore', 'docutils', 'jmespath', 'pip', 'python-dateutil', 's3transfer', 'setuptools', 'six']
RUN find /tmp/vendored -name "*-info" -type d -exec rm -rdf {} +
RUN rm -rdf /tmp/vendored/boto3/
RUN rm -rdf /tmp/vendored/botocore/
RUN rm -rdf /tmp/vendored/docutils/
RUN rm -rdf /tmp/vendored/dateutil/
RUN rm -rdf /tmp/vendored/jmespath/
RUN rm -rdf /tmp/vendored/s3transfer/
RUN rm -rdf /tmp/vendored/numpy/doc/

# Leave module precompiles for faster Lambda startup
RUN find /tmp/vendored -type f -name '*.pyc' | while read f; do n=$(echo $f | sed 's/__pycache__\///' | sed 's/.cpython-36//'); cp $f $n; done;
RUN find /tmp/vendored -type d -a -name '__pycache__' -print0 | xargs -0 rm -rf
RUN find /tmp/vendored -type f -a -name '*.py' -print0 | xargs -0 rm -f

RUN du -sh /tmp/vendored

# Create archive
RUN cd /tmp/vendored && zip -r9q /tmp/package.zip *
RUN cd $APP_DIR/local && zip -r9q --symlinks /tmp/package.zip lib/*.so*
RUN cd $APP_DIR/local && zip -r9q /tmp/package.zip share

# Cleanup
RUN rm -rf /tmp/vendored/
