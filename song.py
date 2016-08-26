import cmd
import finder

class Finder(cmd.Cmd):
    """Finder Command Processor"""
    intro = "Welcome To Song finder! \n(Type help to get started!)"
    
    def do_find(self, song):
        '''
        The Command View enables the user to view a number of
        songs, based on the search parameters he/she inputs.
        It takes(Artist_Name, Track_Name or Part of the Lyrics).
        Example >>> view cheap thrills by sia

        '''
        if(song == ""):
            print('"Sorry, You did not input a search parameter!"')
        else:
            print (finder.find_my_song(song))

    def do_view(self, song):
        '''
        The Command view enables the user to view the Lyrics of a particular song
        based on the Track ID of the song: to get the Track ID first do view.
        it takes use of get_lyrics method and first checks if the lyrics are in your
        local database
        Example >>> view 99521950

        '''
        if(song == ""):
            print('"Sorry, You did not input a search parameter!"')
        else:
            print (finder.get_lyrics(song))
    def do_save(self, song):
        '''
        The Command save allows a user to save the lyrics of a particular song using its Track_ID
        into the local database, It's tied with the get_lyrics function to make sure you do
        not save duplicates.
        Example >>> save 99521950

        '''
        if(song == ""):
            print('"Sorry, Your Song is either already in the database or no song found"')
        else:
            (finder.get_lyrics(song, save = True))
            print("Success! Song saved.")
    def do_clear(self, line):
        '''
        The Command Clear deletes your entire Local songs database.
        Bored by your Current Songs?
        do >>> clear
        '''
        finder.clear_songs()
        print("Done! Songs cleared.")
    
    def do_EOF(self, line):
        '''
        Opsy! House keeping to exit the program.
        
        '''
        return True


if __name__ == '__main__':
    Finder().cmdloop()