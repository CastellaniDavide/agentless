prefix = /usr/local

all:
	$(CC) -o agentless agentless.c

install:
	gcc -o agentless agentless.c
	echo $(DESTDIR)
	echo $(prefix)
	install agentless $(DESTDIR)$(prefix)/bin
	install agentless.1 $(DESTDIR)$(prefix)/share/man/man1

clean:
	rm -f agentless
