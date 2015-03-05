
.SUFFIXES: .c .o
INSTALL=/usr/bin/install -c
bindir="$(PREFIX)/bin"
etcdir="$(PREFIX)/etc"
installdir="$(DESTDIR)"
INC=./
LIBS=
CFLAGS+=-Wall -DPREFIX=\"$(PREFIX)\"
OBJS=memps.o

TARGET=memps

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $@ $(OBJS) $(LIBS)

clean:
	rm -rf $(OBJS) $(TARGET)

distclean: clean
	

install:
	$(INSTALL) -d $(installdir)$(bindir) 
	$(INSTALL) memps $(installdir)$(bindir)

memps.o: memps.c
