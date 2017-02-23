# we need /usr/bin/pyrcc5 and /usr/bin/pyuic5
# from python-qt5-devel
pushd subdownloader/client/gui/
make clean
make
popd
