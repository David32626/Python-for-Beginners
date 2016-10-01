import re
import turtle

def test():
    string='abc 123 cde'
    pat='..c'
    match = re.search(pat, string)
    print (match.group())

    match = re.findall(pat, string)
    print (match)

    match = re.match(pat, string)
    print (match.group())

    pat1 = 'abc'
    match = re.match(pat1, string)
    print (type(match))
    #print (match.group())    


def testsearchandmatch():
    s1="helloworld, i am 30 !"
  
    w1 = "world"
    m1 =  re.search(w1, s1)
    if m1:
        print("find : %s" % m1.group())
    
    if re.match(w1, s1) == None:
        print("cannot match")
    
    w2 = "helloworld"
    m2 = re.match(w2, s1)
    if m2:
        print("match : %s" % m2.group())

def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(50)

    window.exitonclick()

def main():
    draw()
    #test()
    #testsearchandmatch()

if __name__ == '__main__':
    main()