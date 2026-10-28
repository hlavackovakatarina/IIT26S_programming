#print ("Rank    Name    Ski jump points Start time  Style scores\n")
import random
everyone= []
def ski_Jump_point(kPoint):
    for i in range (5):
        lenght = random.randint(0,200)
        points = (lenght - kPoint)*2 + 60
        Name = input ("Name: ")
        scores = random.randint (16.00, 20.00, 0.5)
        everyone.append((Name,lenght,points,scores))
    return everyone
def main():
    kPoint = int(input("For 60 points they need to jump this many meters:"))
    ski_Jump_point(kPoint)
    print(everyone)
main()