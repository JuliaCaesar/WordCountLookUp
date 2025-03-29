'''
WELCOME to version 1 of Word Count Lookup!!!!
I hope you will stay awhile, please enjoy your stay!
<3

Author: JuliaCaesar
Date: 3/2025
'''
from colorama import Fore, Back, Style

# https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def UserInput():
    q = True
    while q is True:
        userInput = 5
        value = input(f"\nPlease enter the word count you would like to look up\nPress {Fore.CYAN}0{Style.RESET_ALL} to terminate.\nWord count: ")
        if value == 0:
            return
        try:
            if value.__contains__(",") or value.__contains__("."):
                if len(value) > 4:
                    tempStr = str(value).strip()
                    tempStr = tempStr.replace(",", "")
                    tempStr = tempStr.replace(".", "")
                    userInput = int(tempStr)
                else:
                    print("no")
                    continue
            else:
                userInput = int(value)
        except:
            print("what in gods name did you do???")
            break

        if userInput == 0:
            q = False
        else:
            LookUp(userInput)

def LookUp(userInput):
    userInput = int(userInput)
    temp = userInput

    #region hardcoded dicts cause fuck you thats why
    wordCountList = {
        1177   : "The Raven",
        1374   : "Sleeping Beauty",
        1694   : "Rapunzel",
        2763   : "Cinderella",
        2947   : "Hansel and Gretel",
        3173   : "Snow White",
        5500   : "The Art of War",
        77325  : "Harry Potter and the Philosopher's Stone",  
        84799  : "Harry Potter and the Chamber of Secrets",
        106821 : "Harry Potter and the Prisoner of Azkaban",
        190858 : "Harry Potter and the Goblet of Fire",
        257154 : "Harry Potter and the Order of the Pheonix",
        169441 : "Harry Potter and the Half Blood Prince",
        198227 : "Harry Potter and the Deathly Hallows",
        95022  : "The Hobbit",
        455125 : "The Lord of the Rings",
        187790 : "The Lord of the Rings: The Fellowship of the Ring",
        143436 : "The Lord of the Rings: The Two Towers",
        134462 : "The Lord of the Rings: The Return of the King",
        36363  : "Lion The Witch and the Wardrobe",
        46118  : "Fahrenheit 451",
        47094  : "The Great Gatsby",
        48523  : "The Outsiders",
        59900  : "Lord of the Flies",
        82762  : "Anne Frank: The Diary of a Young Girl",
        100388 : "To Kill a Mockingbird",
        298000 : "A Game of Thrones: A Song of Ice and Fire",
        165581 : "The Shining",
        56583  : "The Dark Tower: Gunslinger",
        142664 : "Pet Semetary",
        445134 : "It",
        206052 : "Moby Dick",
        187790 : "Dune",
        118875 : "Twilight",
        99750  : "The Hunger Games",
        29160  : "Of Mice and Men",
        27500  : "Alice in Wonderland",
        783137 : "The King James Bible",
        770430 : "The New King James Bible",
        800000 : "The New American Bible",
        5000   : "A Piece of Yellow Soap",
        7000   : "The Secret Life of Walter Mitty",
        8000   : "The Little Engine that Could",
        11000  : "The Tale of Mr.Tod",
        13000  : "The Cask of Amontillado",
        14000  : "The Death of Ivan Ilyich",
        16000  : "James and the Giant Peach",
        18000  : "The Giver",
        20000  : "The Call of the Wild",
        21000  : "The Metamorphosis",
        24000  : "The Time Machine",
        4058   : "The Tale of Peter Rabbit",
        6535   : "A Modest Proposal",
        9555   : "Ion",
        9105   : "The Yellow Wallpaper",
        10610  : "As a Man Thinketh",
        12709  : "Southern Horrors - Lunch Law in All its Phases",
        15800  : "The Prophet",
        17121  : "The Little Prince",
        17101  : "A Pickle for the Knowing Ones",
        19489  : "The Happy Prince and Other Tales",
        22239  : "Anthem",
        23760  : "The Importance of Being Ernest, a Trivial Comedy for Serious People",
        25033  : "Common Sense",
        26000  : "Breakfast at Tiffanys",
        354098 : "The Brothers",
        353250 : "Anna Karenina",
        311155 : "The Decameron",
        568751 : "Les Miserables",
        567246 : "War and Peace",
        600000 : "Jerusalem",
    }
    extraInfoDict = {
        1177   : "Written by Edgar Allan Poe with 3-5 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/72402900-the-raven-by-edgar-allan-poe?from_search=true&from_srp=true&qid=3kX2YdX8dB&rank=1 \n", 
        1374   : "Written by the Brothers Grimm with roughly 3-5 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/564312.Sleeping_Beauty?from_search=true&from_srp=true&qid=LtWnuMB8mm&rank=1 \n",
        1694   : "Written by the Brothers Grimm with roughly 3-5 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/17160901-rapunzel?from_search=true&from_srp=true&qid=aszEnjzSog&rank=3 \n",
        2763   : "Written by the Brothers Grimm with roughly 6 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/17169149-cinderella?from_search=true&from_srp=true&qid=8I8KgNWVxU&rank=1 \n",
        2947   : "Written by the Brothers Grimm with roughly 6-12 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/3329122-hansel-and-gretel?from_search=true&from_srp=true&qid=6Kp2RdcmcE&rank=2 \n",
        3173   : "Written by the Brothers Grimm with roughly 7-13 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/60523273-snow-white-and-other-grimms-fairy-tales?from_search=true&from_srp=true&qid=PhHgeheoKI&rank=3 \n",        
        5500   : "Written by Sun Tzu with roughly 99 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/10534.The_Art_of_War?from_search=true&from_srp=true&qid=WvNLKQ3PdQ&rank=1 \n",
        77325  : "Written by J.K. Rowling with roughly 309 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/72193.Harry_Potter_and_the_Philosopher_s_Stone?from_search=true&from_srp=true&qid=ZKlTWt1jtC&rank=1 \n",
        84799  : "Written by J.K. Rowling with roughly 341 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/15881.Harry_Potter_and_the_Chamber_of_Secrets?from_search=true&from_srp=true&qid=bs9wFy36H2&rank=1 \n",
        106821 : "Written by J.K. Rowling with roughly 435 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/5.Harry_Potter_and_the_Prisoner_of_Azkaban?from_search=true&from_srp=true&qid=333zk2wd1g&rank=1 \n",
        190858 : "Written by J.K. Rowling with roughly 734 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/58613424-harry-potter-and-the-goblet-of-fire?from_search=true&from_srp=true&qid=G8xVGnfYxs&rank=1 \n",
        257154 : "Written by J.K. Rowling with roughly 870 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/161435800-harry-potter-amp-the-order-of-the-pheonix?from_search=true&from_srp=true&qid=GcjGXj3C3p&rank=1 \n",
        169441 : "Written by J.K. Rowling with roughly 652 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/58613345-harry-potter-and-the-half-blood-prince?from_search=true&from_srp=true&qid=CbE7yfSawU&rank=1 \n",
        198227 : "Written by J.K. Rowling with roughly 759 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/58613224-harry-potter-and-the-deathly-hallows?from_search=true&from_srp=true&qid=gKcIRsSaBU&rank=1 \n",
        95022  : "Written by J.R.R. Tolkien with roughly 300 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/5907.The_Hobbit_or_There_and_Back_Again?from_search=true&from_srp=true&qid=beiIs09K03&rank=1 \n",
        455125 : "Written by J.R.R. Tolkien with roughly 1021 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/33.The_Lord_of_the_Rings?from_search=true&from_srp=true&qid=Xfi6gZEAhK&rank=2 \n",
        187790 : "Written by J.R.R. Tolkien with roughly 395 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/61215351-the-fellowship-of-the-ring?from_search=true&from_srp=true&qid=Xfi6gZEAhK&rank=1 \n",
        143436 : "Written by J.R.R. Tolkien with roughly 333 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/61215372-the-two-towers?from_search=true&from_srp=true&qid=Xfi6gZEAhK&rank=3 \n",
        134462 : "Written by J.R.R. Tolkien with roughly 293 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/61215384-the-return-of-the-king?from_search=true&from_srp=true&qid=Xfi6gZEAhK&rank=4 \n",
        36363  : "Written by C.S. Lewis with roughly 172 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/132080146-the-lion-the-witch-and-the-wardrobe?from_search=true&from_srp=true&qid=gMHrXQs7Je&rank=1 \n",
        46118  : "Written by Ray Bradbury with roughly 249 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/13079982-fahrenheit-451?from_search=true&from_srp=true&qid=VZnVUvnb10&rank=1 \n",
        47094  : "Written by F. Scott Fitzgerald with roughly 200 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/41733839-the-great-gatsby?from_search=true&from_srp=true&qid=D8S1i7RsvI&rank=1 \n",
        48523  : "Written by S.E. Hinton with roughly 192 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/192566704-the-outsiders?from_search=true&from_srp=true&qid=8ehDOQDpaO&rank=1 \n",
        59900  : "Written by William Golding with roughly 224 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/7624.Lord_of_the_Flies?from_search=true&from_srp=true&qid=TpfBz4Hkfz&rank=1 \n",
        82762  : "Written by Anne Frank with roughly 352 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/179096.Anne_Frank?from_search=true&from_srp=true&qid=m28zSIRVhM&rank=2 \n",
        100388 : "Written by Harper Lee with roughly 324 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/56916837-to-kill-a-mockingbird?from_search=true&from_srp=true&qid=oMT1vdN0Sw&rank=1 \n",
        298000 : "Written by George R.R. Martin with roughly 835 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/13496.A_Game_of_Thrones?from_search=true&from_srp=true&qid=k6Ce6Osx6S&rank=1 \n",
        165581 : "Written by Stephen King with roughly 447 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/11588.The_Shining?from_search=true&from_srp=true&qid=3cf3EMsFNB&rank=1 \n",
        56583  : "Written by Stephen King with roughly 224 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/43615.The_Gunslinger?from_search=true&from_srp=true&qid=PBf7LNMUk6&rank=4 \n",
        142664 : "Written by Stephen King with roughly 374 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/134483612-friedhof-der-kuscheltiere?from_search=true&from_srp=true&qid=It5ALRG3v3&rank=1 \n",
        445134 : "Written by Stephen King with roughly 1,104 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/830502.It?from_search=true&from_srp=true&qid=GyEoZkB8BK&rank=1 \n",
        206052 : "Written by Herman Melville with roughly 635 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/153747.Moby_Dick_or_The_Whale?from_search=true&from_srp=true&qid=ddFf8PF6Ax&rank=1 \n",
        187790 : "Written by Frank Herbert with roughly 896 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/44767458-dune?from_search=true&from_srp=true&qid=q8d4ngrZPV&rank=1 \n",
        118875 : "Written by Stephenie Meyer with roughly 498 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/41865.Twilight?from_search=true&from_srp=true&qid=acCsIenPFF&rank=1 \n",
        99750  : "Written by Suzanne Collins with roughly 400 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/2767052-the-hunger-games?from_search=true&from_srp=true&qid=oG27YGyd3Z&rank=1 \n",
        29160  : "Written by John Steinbeck with roughly 120 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/890.Of_Mice_and_Men?from_search=true&from_srp=true&qid=I9j5Q8Mvgt&rank=1 \n",
        27500  : "Written by Lewis Carroll with roughly 112 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/60671823-alice-s-adventures-in-wonderland?from_search=true&from_srp=true&qid=kmFVHpvxfM&rank=4 \n",
        783137 : "Written by various authors with roughly 1,300 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/1923820.The_Holy_Bible?from_search=true&from_srp=true&qid=5m3ApYJluu&rank=5 \n",
        770430 : "Written by various authors with roughly 1,300 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/38466282-the-new-king-james-bible?from_search=true&from_srp=true&qid=ZD2FbfNi0w&rank=1 \n",
        800000 : "Written by various authors with roughly 1,300 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/115929.The_New_American_Bible?from_search=true&from_srp=true&qid=QeL2MEslWz&rank=1 \n",
        5000   : "Written by John Galsworthy with roughly 11 pages!\nYou can visit this site for more information: https://www.scribd.com/document/620648612/A-piece-of-yellow-soap \n",
        7000   : "Written by James Thurber with roughly 15 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/3120995-the-secret-life-of-walter-mitty?from_search=true&from_srp=true&qid=sTTirFaUCQ&rank=1 \n",
        8000   : "Written by Watty Piper with roughly 17 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/824204.The_Little_Engine_That_Could?from_search=true&from_srp=true&qid=LFWExtm50s&rank=1 \n",
        11000  : "Written by Beatrix Potter with roughly 24 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/24973156-the-tale-of-mr-tod-illustrated-children-books-by-beatrix-potter?from_search=true&from_srp=true&qid=Y7JsGzOplm&rank=1 \n",
        13000  : "Written by Edgar Allan Poe with roughly 28 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/261240.The_Cask_of_Amontillado?from_search=true&from_srp=true&qid=4OY7QFuNDV&rank=1 \n",
        14000  : "Written by Leo Tolstoy with roughly 31 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/17575112-the-death-of-ivan-ilyich-and-confession?from_search=true&from_srp=true&qid=zGTmfrZYHa&rank=1 \n",
        16000  : "Written by Roald Dahl with roughly 35 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/6689.James_and_the_Giant_Peach?ref=nav_sb_noss_l_25 \n",
        18000  : "Written by Lois Lowry with roughly 40 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/3636.The_Giver?from_search=true&from_srp=true&qid=3jo9fNtyql&rank=1 \n",
        20000  : "Written by Jack London with roughly 44 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/1852.The_Call_of_the_Wild?from_search=true&from_srp=true&qid=4avpLzgZMw&rank=1 \n",
        21000  : "Written by Franz Kafka with roughly 46 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/485894.The_Metamorphosis?from_search=true&from_srp=true&qid=XVFSWEJDci&rank=1 \n",
        24000  : "Written by H.G. Wells with roughly 53 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/2493.The_Time_Machine?from_search=true&from_srp=true&qid=VyfMp0c6jA&rank=1 \n",
        4058   : "Written by Beatrix Potter with roughly 9 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/19321.The_Tale_of_Peter_Rabbit?from_search=true&from_srp=true&qid=R7C4JtbSTk&rank=1 \n",
        6535   : "Written by Jonathan Swift with roughly 14 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/5206937-a-modest-proposal?from_search=true&from_srp=true&qid=7L2a0bdX4C&rank=2 \n",
        9555   : "Written by Plato with roughly 21 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/97541790-ion?from_search=true&from_srp=true&qid=7wjd2kOScN&rank=3 \n",
        9105   : "Written by Charlotte Perkins Gilman with roughly 20 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/775616.The_Yellow_Wallpaper?from_search=true&from_srp=true&qid=vFv5CbdiLf&rank=5 \n",
        10610  : "Written by James Allen with roughly 23 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/81959.As_a_Man_Thinketh?from_search=true&from_srp=true&qid=9cxZCBjb5f&rank=1 \n",
        12709  : "Written by Ida B. Wells-Barnett with roughly 28 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/6970597-southern-horrors?from_search=true&from_srp=true&qid=xAX1eqfeuW&rank=1 \n",
        15800  : "Written by Kahlil Gibran with roughly 35 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/2547.The_Prophet?from_search=true&from_srp=true&qid=TPJMtO0PAY&rank=1 \n",
        17121  : "Written by Antoine de Saint-Exupery with roughly 38 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/157993.The_Little_Prince?from_search=true&from_srp=true&qid=QdREMLPBjD&rank=1 \n",
        17101  : "Written by Timoth Dexter with roughly 38 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/301282.A_Pickle_for_the_Knowing_Ones_or_Plain_Truths_in_a_Homespun_Dress?from_search=true&from_srp=true&qid=OiL19aVr1E&rank=1 \n",
        19489  : "Written by Oscar Wilde with roughly 43 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/779021.The_Happy_Prince_and_Other_Tales?from_search=true&from_srp=true&qid=ZOQTQLjsLa&rank=2 \n",
        22239  : "Written by Ayn Rand with roughly 49 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/667.Anthem?from_search=true&from_srp=true&qid=dicNnTjto7&rank=1 \n",
        23760  : "Written by Oscar Wilde with roughly 52 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/8679340-the-importance-of-being-ernest-a-trivial-comedy-for-serious-people?from_search=true&from_srp=true&qid=3AHCjHyRsT&rank=1 \n",
        25033  : "Written by Thomas Paine with roughly 55 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/161744.Common_Sense?from_search=true&from_srp=true&qid=KtgdhJOSSs&rank=1 \n",
        26000  : "Written by Truman Capote with roughly 57 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/251688.Breakfast_at_Tiffany_s_and_Three_Stories?from_search=true&from_srp=true&qid=LeQgvdMvAz&rank=1 \n",
        354098 : "Written by Fyodor Dostoyevsky with roughly 786 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/4934.The_Brothers_Karamazov?from_search=true&from_srp=true&qid=d2Oc4h7kWw&rank=1 \n",
        353250 : "Written by Leo Tolstoy with roughly 785 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/15823480-anna-karenina?from_search=true&from_srp=true&qid=lD5MNheEtL&rank=1 \n",
        311155 : "Written by Giovanni Boccaccio with roughly 691 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/51799.The_Decameron?from_search=true&from_srp=true&qid=vsKwtIezcs&rank=1 \n",
        568751 : "Written by Victor Hugo with roughly 1,263 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/36377471-les-miserables?from_search=true&from_srp=true&qid=zv3w228mVU&rank=1 \n",
        567246 : "Written by Leo Tolstoy with roughly 1,260 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/656.War_and_Peace?from_search=true&from_srp=true&qid=XZIrcfKqfC&rank=1 \n",
        600000 : "Written by Alan Moore with roughly 1,333 pages!\nYou can visit this site for more information: https://www.goodreads.com/book/show/38246560-jerusalem?from_search=true&from_srp=true&qid=kP64DsXGwT&rank=1 \n",
    }
    #endregion 

    findNumber = min(wordCountList, key=lambda x:abs(x-userInput))

    bookName = wordCountList[findNumber]
    addComma = "{:,}".format(findNumber) 

    print(f"\nYour word count is closest to the book: {Fore.RED}{bookName}{Style.RESET_ALL}")
    print(f"\nWith roughly {Fore.RED}{addComma}{Style.RESET_ALL} words!")
    userInput = input(f"\nPress {Fore.CYAN}1{Style.RESET_ALL} to learn more, {Fore.CYAN}2{Style.RESET_ALL} for " +
                      f"estimated read time, or {Fore.CYAN}any key{Style.RESET_ALL} to go back: ").strip()

    if userInput == "1":
        print(f"\nSure! Here's more information about the book: ")
        print(f"\n{Fore.GREEN}{extraInfoDict[findNumber]}{Style.RESET_ALL}")
        while True:
            userInput = input(f"\nEnter {Fore.CYAN}2{Style.RESET_ALL} for further information, or {Fore.CYAN}any key{Style.RESET_ALL} to go back: ").strip()
            if userInput == "2":
                wordsToMinutes(temp)
                break
            else:
                break
    elif userInput == "2":
        wordsToMinutes(temp)
        while True:
            userInput = input(f"\nEnter {Fore.CYAN}1{Style.RESET_ALL} for book information, or {Fore.CYAN}any key{Style.RESET_ALL} to go back: ").strip()
            if userInput == "1":
                print(f"\n{Fore.GREEN}{extraInfoDict[findNumber]}{Style.RESET_ALL}")
                break
            else:
                break
    else:
        print(f"\n--------------------------------------------------")

def wordsToMinutes(wordCount):
    # 1500 ~= 10 minutes
    if wordCount < 0:
        print(f"\nERROR!!! PANIC!!!")
    elif wordCount > 0:
        resultMinutes = (wordCount / 1500) * 10
        if resultMinutes < 59: # minutes
            roundResultMinutes = int(resultMinutes)
            print(f"\n--------------------------------------------------")
            print(f"\nIt has taken you {Fore.GREEN}{roundResultMinutes} minutes{Style.RESET_ALL} to read your word count!")
            print(f"\n--------------------------------------------------")
        elif resultMinutes >= 60: # hours
            rawResult = resultMinutes / 60
            resultHours = int(rawResult)
            roundDecimal = round(rawResult, 1)
            getDecimal = roundDecimal % 1
            decimalToMinutes = getDecimal * 60
            resultMinutes = int(decimalToMinutes)
            
            print(f"\n--------------------------------------------------")
            print(f"\nIt has taken you {Fore.GREEN}{resultHours} hour(s){Style.RESET_ALL} and {Fore.GREEN}{resultMinutes} minutes{Style.RESET_ALL} to read your word count!")
            print(f"\n--------------------------------------------------")
    else:
        print(f"\nwoops")

def main():
    introText = "WELCOME TO THE WORD COUNT LOOK UP!"
    centerIntroText = introText.center(50)
    print("--------------------------------------------------")
    print(centerIntroText)
    print("--------------------------------------------------")
    UserInput()
 
if __name__=="__main__":
    main()
