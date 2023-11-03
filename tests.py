''' Unit tests for simpleGPyT '''

import unittest
from simpleGPyT.simpleGPyT import Conversation

class TestGPyT(unittest.TestCase):
    
    def test_default_object_creation(self):
        ''' Testing that the object instanitates with correct default values '''
        convo = Conversation("")
        self.assertIsNotNone(convo, "Object failed to instantiate.")
        self.assertEquals(len(convo.get_settings()), 0, "Default settings list not empty.")
        self.assertEquals(convo.get_max_tokens(), 100, "Incorrect default max_tokens.")
        self.assertEquals(convo.get_temperature(), 1, "Incorrect default temperature.")
        self.assertEquals(len(convo), 0, "Chat not empty.")
    
    def test_custom_object_creation(self):
        ''' Check that the custom traits are instantiated correctly. '''
        user = "Adam"
        assistant = "Eve"
        version = "gpt-3.5"
        settings = ["Friendly", "Funny"]
        temperature = 0.8
        max_tokens = 50
        convo = Conversation("", user, assistant, version, settings, temperature, max_tokens)
        self.assertIsNotNone(convo, "Object failed to instantiate.")
        
        self.assertEquals(len(convo.get_settings()), len(settings), "Settings list wrong length.")
        for i in range(len(settings)):
            self.assertEquals(settings[i], convo.get_settings()[i], "Settings list populated incorrectly.")
            
        self.assertEquals(convo.get_max_tokens(), max_tokens, "Incorrect max_tokens.")
        self.assertEquals(convo.get_temperature(), temperature, "Incorrect temperature.")
        self.assertEquals(len(convo), 0, "Chat not empty.")
    
    def test_settings(self):
        ''' Check that added and removing settings works as intended '''
        convo = Conversation("")
        self.assertEquals(len(convo.get_settings()), 0, "Default settings list not empty.")
        
        setting1 = "Happy"
        convo.add_setting(setting1)
        self.assertEquals(len(convo.get_settings()), 1, "Settings list wrong length.")
        self.assertEquals(convo.get_settings()[-1], setting1, "Setting not added correctly.")
        
        setting2 = "Talks like a pirate"
        convo.add_setting(setting2)
        self.assertEquals(len(convo.get_settings()), 2, "Settings list wrong length.")
        self.assertEquals(convo.get_settings()[-1], setting2, "Setting not added correctly.")
        
        convo.pop_setting()
        self.assertEquals(len(convo.get_settings()), 1, "Setting not removed.")
        self.assertEquals(convo.get_settings()[-1], setting1, "Wrong setting removed.")
        
        convo.add_setting(setting2)
        convo.add_setting(setting2)
        convo.pop_setting(0)
        self.assertEquals(len(convo.get_settings()), 2, "Setting not removed.")
        self.assertEquals(convo.get_settings()[0], setting2, "Wrong setting removed.")
        
        convo.clear_settings()
        self.assertEquals(len(convo.get_settings()), 0, "Settings not cleared.")


if __name__ == '__main__':
    unittest.main()