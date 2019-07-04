class Song(object):

    def __init__(self,lyrics):
        self.lyrics=lyrics


    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



happy_bday=Song(['happy bierthday to you,',
                 'i dont want to get sued',
                 'so i will stop roght there'])


bulls_on_parade=Song(['they really aroung the family',
                      'with pockets full of shells'])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
