import csv
with open('The Beatles.csv', 'w', newline='') as csvfile:#file creation
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)#dictionary conversion
    writer.writeheader()
    writer.writerow({'Song': 'Please Please Me',
                     'Year': '1963'})
    writer.writerow({'Song': 'With the Beatles ',
                     'Year': '1963'})
    writer.writerow({'Song': "A Hard Day's Night",
                     'Year': '1964'})
    writer.writerow({'Song': 'Beatles for Sale',
                     'Year': '1964'})
    writer.writerow({'Song': 'Help!',
                     'Year': '1965'})
    writer.writerow({'Song': 'Rubber Soul',
                     'Year': '1965'})
    writer.writerow({'Song': 'Revolver',
                     'Year': '1966'})
    writer.writerow({'Song': 'Magical Mystery Tour',
                     'Year': '1967'})
    writer.writerow({'Song': 'The Beatles',
                     'Year': '1968'})
with open('The Beatles.csv', newline='') as csvfile:#open file
    print(csvfile.name)
    print('------------------------------')
    beatles = csv.DictReader(csvfile)#reading the dictionary
    for heading in beatles.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for song_year in beatles:
        print(song_year['Song'], song_year['Year'])