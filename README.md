<h1 align="center">💬 SimpleGPyT 💬</h1>
<p align="center">A simplified object-oriented interface for OpenAI's chat completion API.</p> </br>

![](https://github.com/AJWestley/SimpleGPyT/actions/workflows/ubuntu.yml/badge.svg)
![](https://github.com/AJWestley/SimpleGPyT/actions/workflows/windows.yml/badge.svg)
![](https://github.com/AJWestley/SimpleGPyT/actions/workflows/macos.yml/badge.svg)
[![GitHub](https://img.shields.io/github/license/AJWestley/SimpleGPyT)](https://github.com/AJWestley/SimpleGPyT)
[![PyPI](https://img.shields.io/pypi/v/SimpleGPyT?logo=pypi)](https://pypi.org/project/SimpleGPyT)

## Installation

Ensure you have Python 3.10 or newer. Python 3.7.1 and up should work as well, but these are untested. </br>
To install the package, run:

```bash
pip install simpleGPyT
```

To use the package, import it at the top of the file.

```python
from simpleGPyT import Conversation
```

## Usage

### Creating a chat

This library relies on a valid OpenAI API key. 
To create a chat, just call the constructor with your API key as the `api_key` parameter.

```python
chat = Conversation("sk-...")
```
</br>

### Chatting to your assistant
You converse with your assistant via the `say()` method.

```python
chat = Conversation("sk-...")
response = chat.say("hello")
print(response)
```
</br>

You can also see the last response you received from your assistant with `last_response()`. </br>
Here is an equivalent of the above code using the `last_response` method

```python
chat = Conversation("sk-...")
chat.say("hello")
print(chat.last_response())
```
</br>

### Settings
You can add settings to your assistant by putting a list of settings as the `settings` argument in the constructor.

```python
s = ["Keep answers concise", "Speak like a pirate", "Have opinions on topics"]
chat = Conversation("sk-...", settings=s)
```
</br>

Settings can also be removed, added and cleared after construction.

```python
s = ["Keep answers concise", "Speak like a pirate", "Have opinions on topics"]
chat = Conversation("sk-...", settings=s)
print(chat.get_settings())

chat.pop_setting()
print(chat.get_settings())

chat.clear_settings()
print(chat.get_settings())
```
</br>

### Viewing and resetting your chat

Messages can be viewed and reset during the chat, leaving settings intact

```python
s = ["Keep answers concise", "Speak like a pirate", "Have opinions on topics"]
chat = Conversation("sk-...", settings=s)

chat.say("hello")
chat.say("write me a poem")

chat.clear_messages()
print(chat.get_messages())
print(chat.get_settings())
```
</br>

The entire chat (settings included) can also be reset.

```python
s = ["Keep answers concise", "Speak like a pirate", "Have opinions on topics"]
chat = Conversation("sk-...", settings=s)

chat.say("hello")
chat.say("write me a poem")

chat.reset()
print(chat.get_messages())
print(chat.get_settings())
```











