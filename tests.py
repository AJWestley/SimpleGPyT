''' Unit tests for simpleGPyT '''

import unittest
from simpleGPyT.simpleGPyT import Conversation

class TestGPyT(unittest.TestCase):
    
    def test_default_object_creation(self):
        ''' Testing that the object instanitates with correct default values '''
        convo = Conversation("")
        self.assertIsNotNone(convo, "Object failed to instantiate.")
        self.assertEqual(len(convo.get_settings()), 0, "Default settings list not empty.")
        self.assertEqual(convo.get_max_tokens(), 100, "Incorrect default max tokens.")
        self.assertEqual(convo.get_temperature(), 1, "Incorrect default temperature.")
        self.assertEqual(len(convo), 0, "Chat not empty.")
    
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
        
        self.assertEqual(len(convo.get_settings()), len(settings), "Settings list wrong length.")
        self.assertListEqual(settings, convo.get_settings())
            
        self.assertEqual(convo.get_max_tokens(), max_tokens, "Incorrect max tokens.")
        self.assertEqual(convo.get_temperature(), temperature, "Incorrect temperature.")
        self.assertEqual(len(convo), 0, "Chat not empty.")
    
    def test_settings(self):
        ''' Check that added and removing settings works as intended '''
        convo = Conversation("")
        self.assertEqual(len(convo.get_settings()), 0, "Default settings list not empty.")
        
        setting1 = "Happy"
        convo.add_setting(setting1)
        self.assertEqual(len(convo.get_settings()), 1, "Settings list wrong length.")
        self.assertEqual(convo.get_settings()[-1], setting1, "Setting not added correctly.")
        
        setting2 = "Talks like a pirate"
        convo.add_setting(setting2)
        self.assertEqual(len(convo.get_settings()), 2, "Settings list wrong length.")
        self.assertEqual(convo.get_settings()[-1], setting2, "Setting not added correctly.")
        
        convo.pop_setting()
        self.assertEqual(len(convo.get_settings()), 1, "Setting not removed.")
        self.assertEqual(convo.get_settings()[-1], setting1, "Wrong setting removed.")
        
        convo.add_setting(setting2)
        convo.add_setting(setting2)
        convo.pop_setting(0)
        self.assertEqual(len(convo.get_settings()), 2, "Setting not removed.")
        self.assertEqual(convo.get_settings()[0], setting2, "Wrong setting removed.")
        
        convo.clear_settings()
        self.assertEqual(len(convo.get_settings()), 0, "Settings not cleared.")
        
    def test_max_tokens(self):
        convo = Conversation("")
        self.assertEqual(convo.get_max_tokens(), 100, "Incorrect default max tokens.")
        
        mt = 20
        convo.set_max_tokens(mt)
        self.assertEqual(convo.get_max_tokens(), mt, "Max tokens not updated.")
    
    def test_temperature(self):
        convo = Conversation("")
        self.assertEqual(convo.get_temperature(), 1, "Incorrect default temperature.")
        
        temp = 0.5
        convo.set_temperature(temp)
        self.assertEqual(convo.get_temperature(), temp, "Temperature not updated.")
    
    # TODO: 
    # Tests to add:
    # - __str__
    # - reset
    # - clear_messages
    # - get_messages
    # - last_response
    # - say


if __name__ == '__main__':
    unittest.main()