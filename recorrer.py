from asyncio.proactor_events import _ProactorBaseWritePipeTransport


def run ():
    # name = input("Add your name: ")
    # for counter in name:
    #     print(counter)

    phrase = input("Input your phrase: ")
    for character in phrase:
        print(character.upper())

if __name__== '__main__':
    run()
