from linkedin_helper import Linkedin

# Authenticate using any Linkedin user account credentials
api = Linkedin(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

# GET a profile
profile = api.get_profile( 'harshinikovur')

# GET a profiles contact info
contact_info = api.get_profile_contact_info( 'harshinikovur')

# GET Ist degree connections of a givén profile
connections = api.get_profile_connections('1234ascip304')  # If this is an ID or string


print (profile)