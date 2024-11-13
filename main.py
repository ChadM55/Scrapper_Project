from bs4 import BeautifulSoup

#allows that we can open file and read its content
#params: file name, read or write
#as html_file is a variable that will get used inside block
with open('home.html', 'r') as html_file:
    #content gets content of read file
    content = html_file.read()

    #create an instance of soup variable
    #lxml is a parcer method, content is what we want to scrape
    soup = BeautifulSoup(content, 'lxml')
    '''
    #searchs only for first element
    #tags = soup.find('h5')
    tags = soup.find_all('h5')
    courses_html_tags = soup.find_all('h5')

    #courses_html_tags is a list so use for loop
    for course in courses_html_tags:
        print(course.text)
    '''
    #div is html tag class_ must have _ to seperate it from key word
    #'card' is html styling class
    #div is entire block of elements for styling
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        #.split() splits strings into substrings based on white space.
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')



