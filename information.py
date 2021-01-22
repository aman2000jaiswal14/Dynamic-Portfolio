import json
from datetime import datetime,timedelta
class Person:
    def __init__(self):
        self.name = ""
        self.image_file = r"static\images\avataaars.svg"
        self.about = ""
        self.resume = "/"
        self.skills = []
        self.projects = []
        self.email_id = ""
        self.password ="123456"
        try:
            self.load_data()
        except:
            pass
    def first_time_login(self):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            self.name = data["name"]
            self.email_id = data["email"]
            self.password = data["password"]
            return False
        except:
            return True

    def reset_all(self):
        self.name = ""
        self.image_file = r"static\images\avataaars.svg"
        self.about = ""
        self.resume = "/"
        self.skills = []
        self.projects = []
        self.email_id = ""
        self.password = "123456"
        data = {"reset":True}
        with open('client_data.json', 'w') as f:
            json.dump(data,f)

    def reset_user(self,name,email,password):
        try:
            new_data = {
                "name": name,
                "email": email,
                "password": password,
                "about": "",
                "resume": "/",
                "image_file": r"static\images\avataaars.svg",
                "skills": [],
                "projects": [],
            }
            with open('client_data.json', 'w') as f:
                json.dump(new_data,f,indent=2)

        except:
            pass

    def load_data(self):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            self.name = data["name"]
            self.email_id = data["email"]
            self.password = data["password"]
            try:
                self.image_file = data["image_file"]
            except:
                pass
            try:
                self.about = data["about"]
            except:
                pass
            try:
                self.resume = data["resume"]
            except:
                pass
            try:
                self.skills = data["skills"]
            except:
                pass
            try:
                self.projects = data["projects"]
            except:
                pass

        except:
            pass



    def replace_name(self,name):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            data["name"] = name
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass


    def replace_image(self,image):
        self.image_file = image

    def replace_about(self,about):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            data["about"] = about
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def replace_resume(self,resume):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            data["resume"] = resume
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def add_skill(self,skill,star):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)

            s = []
            for i in range(star):
                s.append('s')
            s = ''.join(s)
            sk = {"skill": skill, 'star': s}
            data["skills"].append(sk)
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def remove_skill(self,skill_name):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            temp = data
            for n,skill in enumerate(temp["skills"]):
                if(skill["skill"]==skill_name):
                    temp["skills"].pop(n)
                    break
            print(data)
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(e)
            pass
    def add_project(self,new_project):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            data["projects"].append(new_project)
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass


    def remove_project(self,title):
        try:
            with open('client_data.json', 'r') as f:
                data = json.load(f)
            temp = data
            for n, project in enumerate(temp["projects"]):
                if (project["title"] == title):
                    data["projects"].pop(n)
                    break
            with open('client_data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass

    def add_emai(self,email):
        self.email_id = email

    def change_password(self,old,new):
        if(self.password==old):
            self.password = new
            return True
        return False


class Messages:
    def __init__(self):
        self.message = []
        try:
            self.load_message()
        except:
            self.reset_message()

    def load_message(self):
        try:
            with open('feedback.json', 'r') as f:
                data = json.load(f)

            for mess in data["messages_list"]:
                self.message.append(mess)

        except:
            pass

    def reset_message(self):
        try:
            data = {"messages_list":[]}
            with open('feedback.json', 'w') as f:
                json.dump(data,f,indent=2)
        except:
            pass

    def send_message(self,mess):
        try:
            try:
                with open('feedback.json', 'r') as f:
                    data = json.load(f)

            except:
                self.reset_message()
                with open('feedback.json', 'r') as f:
                    data = json.load(f)
            if(mess["name"]=="" and mess["email"]=="" and mess["content"]==""):
                return
            data["messages_list"].append(mess)
            with open('feedback.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass

class TimeDate:
    def __init__(self):
        self.timedate = "2021-01-22 12:29:47.118432"
        self.interval = timedelta(minutes =15)
        self.timesub = 15

    def set_datetime(self):
        data = datetime.now()
        data = {"timedate":data.strftime('%Y-%m-%d %H:%M:%S.%f')}
        try:
            with open('datetime.json','w') as f:
                json.dump(data,f)
        except:
            pass

    def get_datetime(self):
        try:
            with open('datetime.json','r') as f:
                data = json.load(f)
            data =  datetime.strptime(data["timedate"], '%Y-%m-%d %H:%M:%S.%f')
            return data
        except:
            pass

    def reset_datetime(self):
        data = {
                "timedate": "2021-01-22 12:29:47.118432"
                }
        try:
            with open('datetime.json','w') as f:
                json.dump(data,f)
        except:
            pass

    def passtime(self):
        curr = datetime.now()
        old = self.get_datetime()
        if(curr-old > self.interval):
            return True
        else:
            return False
    def get_lefttime(self):
        curr = datetime.now()
        old = self.get_datetime()
        interval = curr-old
        interval = interval.seconds
        interval = self.timesub - interval//60
        return interval
