'''
Simple setup of dev projects for your favorite editor

Created on 27 Jul 2021

@author: metastable
@see: https://docs.python.org/3/library/argparse.html
@see: https://docs.python.org/3/howto/argparse.html
@see: https://python-redmine.com/installation.html
'''

import argparse, getpass
from redminelib import Redmine

editors=['eclipse']
def_editor='eclipse'
def_home='https://redmine.inuits.eu'

def main():
    parse_args()

def usage():
    print('usage')

def parse_args():
    parser = argparse.ArgumentParser(description='Setup a project in your favorite editor.')
    
    #group = parser.add_mutually_exclusive_group()
    parser.add_argument('-p', '--project',
                       help='a redmine project to setup')
    parser.add_argument('-g', '--gits',
                        action='store_true',
                        help='a file containing git repositories to setup')
    parser.add_argument('-cu', '--username',
                        help='your redmine username')
    parser.add_argument('-cp', '--password',
                        help='your redmine password')
    
    # Informative output
    parser.add_argument('-le', '--editors',
                       action='store_true',
                       help='list implemented editors')
    
    # Project relevant arguments
    parser.add_argument('-rh', '--home',
                        default=def_home,
                        help='redmine home')
    parser.add_argument('-e', '--editor',
                        default=def_editor,
                        help='something that identifies your editor')
    
    
    args = parser.parse_args()
    
    if args.editors:
        print('Implemented editors:')
        for editor in editors:
            print('- ' + editor + (' (default)' if editor == def_editor else ''))
    
    if args.gits:
        with open(args.gits, 'r') as f:
            gits = f.readLines()
            print(gits)
    elif args.project:
        username, password = request_credentials(args.username, args.password)
        
        redmine = Redmine(args.home, username = username, password = password)
        project = redmine.project.get(args.project)
        
        print(project)
        
        print(project.settings)
        
        #password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        #password_mgr.add_password(None, project_home, username, password)
        #handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        #opener = urllib.request.build_opener(handler)
        #with opener.open(project_home) as url:
        #    data = json.loads(url.read().decode())
        #    print(data)

def request_credentials(username, password):
    if not username:
        username = input('Username: ')
    if not password:
        password = getpass.getpass(prompt='Password: ', stream=None)
    
    return username, password

if __name__ == '__main__':
    main()
