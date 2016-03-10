import os

class RequirementTrace(object):
    req_text = ""
    def __init__(self, text):
        self.req_text = text
        self.func_name = []

class JobSotryTrace(object):
    JobStory_text = ""
    def __init__(self, text):
        self.JobStory_text = text
        self.func_name = []

Requirements = {}
JobStories = []

def requirements(req_list):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for req in req_list:
                if req not in Requirements.keys():
                    raise Exception('Requirement {0} not defined'.format(req))
                Requirements[req].func_name.append(func.__name__)
            return func(*args, **kwargs)

        return add_req_and_call
    return wrapper

def JobStory(story):
    def wrapper(func):
        def add_req_and_call(*args, **kwargs):
            for js in JobStories:
                print js.JobStory_text
                print story
                if story == js.JobStory_text:
                    js.func_name.append(func.__name__)
                    break
            else:
                raise Exception("Story not found in the list")
            return func(*args, **kwargs)

        return add_req_and_call

    return wrapper

# with open('C:\\Users\\Hatim\\Documents\\GitHub\\HatimP\\cst236_lab1\\Lab_Requirements.txt') as f:
with open(os.getcwd() + "\Lab_Requirements.txt") as f:

    for line in f.readlines():
        if '#0' in line:
            req_id, desc = line.split(' ', 1)
            Requirements[req_id] = RequirementTrace(desc)
        elif line.startswith("*"):
            garbage, text = line.split(' ', 1)
            JobStories.append(JobSotryTrace(text.strip()))



