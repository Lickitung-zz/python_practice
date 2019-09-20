# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

dictionary = {"Obama": ["Python Basics", "JavaScript Basics", "HTML/CSS", "GoLang"],
              "Trump": ["jQuery Basics", "node.js basics", "EmojiCode"],
              "Kennedy": ["C# Basics", "UNIX"]}

def num_teachers(dict):
    return len(dict.keys())

def num_courses(dict):
    num_of_courses = 0
    courses = [*dict.values()]
    for course in courses:
        num_of_courses += len(course)
    return num_of_courses

def courses(dict):
    course_list = []
    courses = [*dict.values()]
    for course in courses:
        course_list.extend(course)
    return course_list

def most_courses(dict):
    max_count = 0
    longest_teacher = ''
    for teacher in dict:
        if len(dict[teacher]) > max_count:
            max_count = len(dict[teacher])
            longest_teacher = teacher
    return longest_teacher

def stats(dict):
    num_courses = 0
    new_list = []
    for teacher in dict:
        num_courses = len(dict[teacher])
        new_list += [[teacher, num_courses]]
    return print(new_list)

print(stats(dictionary))