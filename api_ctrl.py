#API Controller algorithm 
#Made by AdrielHigor

import requests
from requests.auth import HTTPBasicAuth

class Api_endpoint():
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url', None)
        self.token = kwargs.get('token', None)
        self.user = kwargs.get('user', None)
        self.password = kwargs.get('password', None)

class Api_ctrl():
    def __init__(self, *args, **kwargs):
        self.sender = kwargs.get('sender', None)
        self.receiver = kwargs.get('receiver', None)

    def data_request(self): 
        try:
            if (self.receiver.url != None):
                if (self.receiver.user != None and self.receiver.password != None):
                    receiver_data = (requests.get(self.receiver.url, auth=HTTPBasicAuth(self.receiver.user, self.receiver.password))).json()
                elif (self.receiver.token != None):
                    receiver_data = (requests.get(self.receiver.url, headers={'Authorization': 'token {}'}.format(self.receiver.token))).json()
                else:
                    receiver_data = (requests.get(self.receiver.url)).json()
                return receiver_data
            else:
                print('Erro inesperado: Nenhum url foi definido')
        except AttributeError:
            print('Erro inesperado: Nenhum atributo foi definido')






 






    


# class Contador(object):
#         def __init__(self, total):
#             self.total = total

#         def remains(self, done):
#                 left = (100 * done)/self.total
#                 return ("%.2f" % left)

# #Simple request on suap's API.
# api_request = requests.get('https://suap.ifpb.edu.br/api/ensino/alunos/v1/', auth=HTTPBasicAuth('suap_login', 'suap_password') )

# #Getting response from 'api_request' as a json file.
# response_init = api_request.json()

# #API_ENDPOINT, show us where we are going to post our data responses in this case 'name', 'course', 'status', 'registration'
# API_ENDPOINT = ("http://localhost:8000/api/students/")

# #pagination varset
# offset = 0

# #Post count
# student_count = 0

# bytes = ((response_init["count"]))

# porcentagem = Contador(bytes)
# #A loop to pick all the responses from  the API and do the pagination based on the pages count of our API
# for page in range (((response_init["count"])//100)+1):
    
#     #Dinamic page request
#     offset_request = requests.get('https://suap.ifpb.edu.br/api/ensino/alunos/v1/?offset={}'.format(offset), auth=HTTPBasicAuth('suap_login', 'suap_password'))
    
#     #Response handler
#     response = offset_request.json()

#     #Data storage and post into the API_ENDPOINT
#     for student in response["results"]:
        
#         if "Cajazeiras" in student["curso"]["nome"]:
#             student_count +=1
#             data = {
#                 'name': student["nome"], 
#                 'course':student["curso"]["nome"], 
#                 'status':student["situacao"], 
#                 'registration':student["matricula"]
#                 }

#             student_post = requests.post(url = API_ENDPOINT, data=data, headers = {'Authorization': 'token access_token_here'}) 

#     offset += 100
#     print('Page: ', offset)
#     print('Registred students: ', student_count)
#     print(porcentagem.remains(offset),'% complete;')
#     print('==============================================================')

# # name 
# # course
# # status
# # registration