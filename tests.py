''' Unit tests for simpleGPyT '''

import unittest
from simpleGPyT.simpleGPyT import Conversation

class TestGPyT(unittest.TestCase):
    
    def test_default_object_creation(self):
        convo = Conversation("")
        self.assertIsNotNone(convo, "Object failed to instantiate.")
        self.assertEquals(len(convo.get_settings()), 0, "Default settings list not empty.")
        self.assertEquals(convo.get_max_tokens(), 100, "Incorrect default max_tokens.")
        self.assertEquals(convo.get_temperature(), 1, "Incorrect default temperature.")
        self.assertEquals(len(convo.get_messages()), 0, "Message list not empty.")


if __name__ == '__main__':
    unittest.main()