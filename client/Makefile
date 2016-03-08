# Piweb Client Makefile script
# Purpose: Make Piweb Client
# By: Drake Song, 2016.
#
 
# Set up basic variables:
CC = g++
CFLAGS = -c -Wall
LDFLAGS =
 
# List of sources:
SOURCES = client.cc
OBJECTS = $(SOURCES:.cc=.o)
 
# Name of executable target:
EXECUTABLE = client
CFLAGS +=
LDFLAGS += -lcurl -lpifacedigital -lmcp23s17
 
all: $(SOURCES) $(EXECUTABLE)
 
$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@ $(LDFLAGS)
 
.cpp.o:
	$(CC) $(CFLAGS) $< -o $@
 
clean:
	rm $(OBJECTS) $(EXECUTABLE)
