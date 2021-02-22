
class Track:

    def __init__(self, song, artiste):
        self.name = song
        self.artiste = artiste
        self.timesplayed = 0

    @property
    def get_name(self):
        return self.name

    @property
    def get_artiste(self):
        return self.artiste

    def play(self):
        self.timesplayed += 1
        return self

    def __str__(self):
        track = "{} {} {}".format(self.name, self.artiste, self.timesplayed)
        return track


class DLLNode:
    def __init__(self, previous_node=None, track=None, next_node=None):
        self.prev = previous_node
        self.track = track
        self.next = next_node

class Pytoonz:

    def __init__(self):
        self.pointer = None
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(self.head, None, None)
        self.head.next = self.tail
        self.size = 0

    def __str__(self):
        string = "Playlist: \n"
        node = self.head.next
        if self.size == 0:
            string += str(None)
            return string
        else:
            i = 0
            while i < self.size:
                if node == self.pointer:
                    string += "-->"
                string += str(node.track) + "\n"
                node = node.next
                i += 1
            return string

    def length(self):
        return self.size  # update the size when adding track

    def get_current(self):  # gets the song that the pointer is at
        if self.size == 0:
            return None
        else:
            return self.pointer.track

    def add_track(self, track):
        new_node = DLLNode(None, track, None)   # Creates a new node for the new song
        self.pointer = self.head.next           # pointer to the first song
        if self.head.next is self.tail:         #if there is nothing in the playlist then we add one
            new_node.prev = self.head
            new_node.next = self.tail
            self.head.next = new_node
            self.tail.prev = new_node
        else:
            current = self.head             # a pointer to get to the end of the list before the tail to be able to add to the end
            while current.next is not self.tail:
                current = current.next
            current.next = new_node         # create the new node in the list
            new_node.prev = current
            new_node.next = self.tail
        self.size += 1                      # add the size of the playlist by one

    def add_after(self, track, track_before):        # Need to fix - won't return the last song in the playlist after putting in new track
        current = self.head
        new_node = DLLNode(None, track, None)
        while current:
            if current.next is self.tail and current.track == track_before:
                self.add_track(track)
            elif current.track is track_before:
                after_node = current.next
                current.next = new_node
                new_node.next = after_node               # seems to not be adding the last song to the playlist
                new_node.prev = current
                after_node.prev = new_node
            current = current.next

    def next_track(self):                       #if we are at the last song then it will return the first song (wrap around)
        if self.pointer.next is self.tail:
            self.pointer = self.head.next
        else:
            self.pointer = self.pointer.next    # will move the pointer to the new song if not the case above

    def prev_track(self):                        # will also do a wrap around if the previous song is the head it will return the last song
        if self.pointer.prev is self.head:
            self.pointer = self.tail.prev
        else:
            self.pointer = self.pointer.prev    # will make the pointer go to the previous song

    def reset(self):                            # if the pointer is not at the first song, it will change it so it resets
        if self.pointer is not self.head.next:
            self.pointer = self.head.next

    def play(self):                              # if there is a song in the list than the song that the pointer is at will be played from class Track
        current = "Playing: "
        if self.size > 0:
            if self.pointer is not self.head or self.tail:
                return current + str(Track.play(self.pointer.track))
        else:
            print("There is no songs in your playlist to play")

    def remove_current(self):
        if self.size == 1:
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
        elif self.size > 1:
            if self.pointer.next is not self.tail:
                before_node = self.pointer.prev
                after_node = self.pointer.next
                before_node.next = after_node
                after_node.prev = before_node
                self.size -= 1
        elif self.pointer.next is self.tail:
            before_node = self.pointer.prev
            before_node.next = self.tail
            self.tail.prev = before_node
            self.size -= 1
        else:
            return None
        self.pointer = self.pointer.next



def main():
    DLL= Pytoonz()

    track1 = Track("positions", "Ariana Grande")
    track2 = Track("Diamonds", "Sam Smith")
    track3 = Track("Giants", "Dermot Kennedy")
    track4 = Track("you broke me first", "Tate McRae")
    track5 = Track("Holy", "Justin Bieber")
    track6 = Track("Take you Dancing", "Jason Derulo")
    track7 = Track("Fake Fine", "Robert Grace")

    Track.play(track1)
    Track.play(track1)
    Track.play(track1)
    Track.play(track2)
    Track.play(track2)
    Track.play(track3)
    Track.play(track3)
    Track.play(track4)
    Track.play(track5)
    Track.play(track6)
    Track.play(track7)
    #print(Track.play(track1))


    DLL.add_track(track1)
    DLL.add_track(track2)
    DLL.add_track(track3)
    DLL.add_track(track4)
    DLL.add_track(track5)
    DLL.add_track(track6)
    #
    print(DLL)
    # DLL.next_track()
    # print(DLL)
    # DLL.next_track()
    # print(DLL)
    # DLL.next_track()
    # print(DLL)
    # DLL.next_track()
    # print(DLL)
    DLL.prev_track()
    print(DLL)
    # DLL.reset()
    # print(DLL)
    #
    # print(DLL.play())
    # print(DLL)
    #
    # DLL.add_after(track6, track4)
    # # print(DLL)
    #
    #
    # print(DLL)
    DLL.next_track()
    print(DLL)
    DLL.next_track()
    print(DLL)
    # DLL.next_track()
    # print(DLL)
    # DLL.prev_track()
    # print(DLL)
    # DLL.remove_current()
    # print(DLL.length())



if __name__ == '__main__':
    main()
