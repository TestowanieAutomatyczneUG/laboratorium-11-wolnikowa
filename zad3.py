import unittest
from unittest.mock import MagicMock

class Friendships:

    fr = {
        "Bessman": ["Kowalski", "Nowak", "Wolnik"],
        "Kowalski": ["Bessman", "Nowak"],
        "Nowak": ["Bessman", "Kowalski", "Wolnik"],
        "Wolnik": ["Bessman", "Nowak"],
    }

    def makeFriends(self, person1, person2):
        id = self.fr[person1].index(person2)
        id2 = self.fr[person2].index(person1)
        if id < 0 and id2 < 0:
            self.fr[person1].append(person2)
            self.fr[person2].append(person1)
        else:
            print(f"{person1} and {person2} are already friends")

    def getFriendsList(self, person):
        return self.fr[person]

    def areFriends(self, person1, person2):
        id = self.fr[person1].index(person2)
        if id >= 0:
            return True
        else:
            return False

    def addFriend(self, person, friend):
        id = self.fr[person].index(friend)
        if id < 0:
            self.fr[person].append(friend)
        else:
            print(f"{friend} is already in {person} friend list")

class TestFriendships(unittest.TestCase):

    def setUp(self):
        self.temp = Friendships()

    def test_get_friends_list_nowak(self):
        frListNowak = ["Bessman", "Kowalski", "Wolnik"]
        self.assertEqual(self.temp.getFriendsList("Nowak"), frListNowak)

    def test_get_friends_list_kowalski(self):
        frListKowalski = ["Bessman", "Nowak"]
        self.assertEqual(self.temp.getFriendsList("Kowalski"), frListKowalski)

    def test_get_friends_list_kowalski_called_once(self):
        mock = Friendships()
        mock.getFriendsList = MagicMock()
        mock.getFriendsList("Kowalski")
        mock.getFriendsList.assert_called_once_with("Kowalski")

    def test_are_friends_nowak_kowalski(self):
        mock = Friendships()
        mock.areFriends = MagicMock()
        mock.areFriends("Nowak", "Kowalski")
        mock.areFriends.assert_called_once_with("Nowak", "Kowalski")

    def test_add_friend_nowak(self):
        mock = Friendships()
        mock.addFriend = MagicMock()
        mock.addFriend("Nowak", "Kowalska")
        mock.addFriend.assert_called_once_with("Nowak", "Kowalska")

    def test_make_friends_kowalski_bobkowska(self):
        mock = Friendships()
        mock.makeFriends = MagicMock()
        mock.makeFriends("Kowalski", "Wolnik")
        mock.makeFriends.assert_called_once_with("Kowalski", "Wolnik")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()