# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#



#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(CV, job_title):
    usernames = []
    for user in CV:
        if(job_title in user['jobs']):
            usernames.append(user['user'])
    return usernames


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(CV):
    job_all=[]
    for user in CV:
        job_all = job_all + user['jobs']
    job_unique = list(set(job_all))
    dictionary = {}
    for title in job_unique:
        dictionary[title] = job_all.count(title)
    
    return dictionary

#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

def most_popular_job(CV):
    j_count = job_counts(CV)
    most_popular = ['',0]
    for x in j_count:
        if(j_count[x]>most_popular[1]):
            most_popular[1] = j_count[x]
            most_popular[0] = x
    return tuple(most_popular)