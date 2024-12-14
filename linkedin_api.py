from linkedin_api import Linkedin
# Authenticate using any Linkedin user account credentials
api = Linkedin('keerthisurisetty11@gmail.com', 'LifeISgood18!!')

# GET a profile
profile = api get_profile( 'keerthi-surisetty')

# GET a profiles contact info
contact info = api.get profile_contact_info( 'keerthi-surisetty')

# GET Ist degree connections of a givén profile
connections = api.get_profile_connections 1234ascip304*0

print (profile)