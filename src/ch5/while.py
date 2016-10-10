
def main():
    score = 0
    while score != -1:
        score = int(input('輸入分數:'))
        if score >= 90:
            print ('A')
        elif 90 > score >= 80:
            print ('B')
        elif 80 > score >= 70:
            print ('C')
        elif 70 > score >= 60:
            print ('D')
        else:
            print ('不及格')

if __name__ == "__main__":
    main()
