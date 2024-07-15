
import sys
import requests #type: ignore

def getArg(idx: int,detail):
    if len(sys.argv) > idx:
        return sys.argv[idx]
    else:
        print(f"wttr {detail["command"]} ****")
        print(f"expected argument where{" "*abs(int(len(detail["command"])-16))}^^ ")
        print(f"reason:\n{detail["reason"]}")
        sys.exit(1)

def Usage():
    print("Usage: wttr [command]? [args*]?")
    sys.exit(1)

def Failed(text: str):
    print(text)
    sys.exit(1)

BASE = "https://wttr.in"

if len(sys.argv) < 1:
    Usage()

command = getArg(1,{"command":"[command]","reason":"require a command to run!"})

match command:
    case "place" | "where" | "domain" | "location" | "in":
        response = requests.get(BASE+"/"+getArg(2,{"command":"'place' | 'where' | 'domain' | 'location' | 'in'","reason":"require a location or a domain"}))
        if response.ok:
            print(response.text)
        else:
            Failed(response.reason)
    case "help" | "-help":
        print("Unofficial wttr.in cli tool")
        Usage()
    case _:
        response = requests.get(BASE+"/"+getArg(2,{"command":"","reason":"require a location or a domain"}))
        if response.ok:
            print(response.text)
        else:
            Failed(response.reason)

