import os

if __name__ == '__main__':

    if os.listdir('npy'):
        print('\nStart identifying process...')
        os.system('python FacesIdentifier.py')
    else:
        print('\nDownloading users from VK: ')
        os.system('python UsersLoader.py')

        print('\nStart downloading photos from VK...')
        os.system('python PhotosLoader.py')

        print('\nStart collecting face descriptors from photos...')
        os.system('python FacesDescriptorCollector.py')
