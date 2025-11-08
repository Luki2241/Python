message = input("Enter your message to encode: ")
part1 = message[::2]
part2 = message[1::2]
encodedmsg = part1 + part2

print(encodedmsg)