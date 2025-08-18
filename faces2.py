def  main():
    t = input("make a face: ")
    convert(t)

def convert(t):
    t = t.replace(":)", "🙂" ).replace(":(", "🙁" ).replace(":v", "🥠")
    print(t)

main()
