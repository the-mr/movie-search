#Title : Movie Search
#Name : Heriberto Ramirez
#Date : SEP 18 2021
#Description : Search for movies

#Recommended Ad Blocker for MSEDGE : https://microsoftedge.microsoft.com/addons/detail/adblock-%E2%80%94-best-ad-blocker/ndcileolkflehcjpmjnfbnaibdcgglog

import requests
import sys


def getMovieName() :

    arguments = sys.argv
    #print(arguments)

###### NEW FEATURE - put space in movie name to make one - NOT ACTIVE #####
    #x = -1
    #z = ''

    #for arg in arguments :
    #    z += arg+' '
    #    print(arg)
    #    x += 1
    #print(x)
    #print(z)

    #if x > 1 :
        #try :
            #movieName += arguments[x]

##############################################################################

    try :
        movieName = arguments[1]
        print('Searching For Movie :', movieName)
        print()
    except IndexError:
        movieName = input('Movie Name : ')
        print('Searching For Movie :', movieName)
        print()

    searchMovies(movieName)


def searchMovies(movieName) :
    try :
        resp = requests.get(('https://api.gdriveplayer.us/v1/movie/search?title=%s&limit=100' % movieName))
        resp = resp.json()

        if resp == None:
            print('Move Name Invalid... Try Again\n')
            getMovieName()

        x = 0

        try:
            for option in resp:
                movieTitle = option['title'].upper()
                print(('%s)' % x), movieTitle)
                x += 1
            try :
                num = int(input('\nChoose Movie (number) : '))
                getImdb(num, resp)
            except ValueError:
                print('\nInvalid Choice! Try Again\n')
                searchMovies(movieName)

        except TypeError:
            num = 0
            getImdb(num, resp)

    except Exception as err:
        print('Error :', err)
        print('Maybe Check Your Network Connection! Exiting ..')
        exit()


def getImdb(num, resp) :
    try:
        imdb = resp[num]['imdb']
        getMovie(imdb)
    except:
        print('\nsomething went wrong')


def getMovie(imdb) :
    apiMovie = 'https://database.gdriveplayer.us/player.php?imdb='
    movieLocation = apiMovie + imdb

    try:
        resp = requests.get(movieLocation)
        httpCode = resp.status_code
        #print(httpCode)

        if httpCode != 200:
            print('Link Does Not Work')
            print('But Here It Is :', movieLocation)

        print('\nMovie :', movieLocation)

    except Exception as err:
        print('Error :', err)
        print('\nMaybe Check Your Network Connection! Exiting ..')
        exit()


getMovieName()

