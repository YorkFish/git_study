main: main.cpp
	g++ -Wall -g -std=c++11 main.cpp helper.cpp -o main

clean:
	del main.exe *.o

run:
	mingw32-make && start cmd /c "main & pause"
