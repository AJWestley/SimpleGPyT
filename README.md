<h1 align="center">💬 SimpleChat 💬</h1>
A simplified object-oriented interface for OpenAI's chat completion API.

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










