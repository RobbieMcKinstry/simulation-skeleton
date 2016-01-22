#!/usr/local/bin/python
from actors.SampleActor import Actor

def main():
    print('Hello Simulation')
    actor = Actor()
    actor.say_hello()


if __name__ == '__main__':
    main()
