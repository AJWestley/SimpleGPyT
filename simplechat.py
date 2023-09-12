import openai

class Conversation:
    
    def __init__(
        self, 
        api_key: str,
        user_name: str = "user",
        assistant_name: str = "assistant",
        model: str = "gpt-3.5-turbo", 
        settings: list[str] = None, 
        temperature: float = 1,
        max_tokens: int = 100
        ) -> None:
        
        openai.api_key = api_key
        
        self.__model = model
        self.__temperature = None
        self.__max_tokens = None
        self.__messages = []
        self.__user = user_name
        self.__assistant = assistant_name
        self.__settings = []
        
        self.set_temperature(temperature)
        self.set_max_tokens(max_tokens)
        
        if settings is None:
            settings = []
        for setting in settings:
            self.add_setting(setting)
    
    
    # Chat
    
    def say(self, message: str) -> str:
        self.__messages.append({"role": "user", "content": message})
        messages = self.__settings + self.__messages
        response = openai.ChatCompletion.create(
            model=self.__model,
            messages=messages,
            temperature=self.__temperature,
            max_tokens=self.__max_tokens
        )
        self.__messages.append(response.choices[0]["message"])
        return self.last_response()
    
    def last_response(self) -> str:
        return self.__messages[-1]["content"]
    
    def clear_messages(self) -> None:
        self.__messages.clear()
    
    
    # Settings
    
    def pop_setting(self, index: int = -1) -> str:
        return self.__settings.pop(index)
    
    def get_settings(self) -> None:
        return [s["content"] for s in self.__settings]        
    
    def add_setting(self, setting: str) -> None:
        self.__settings.append({"role": "system", "content": setting})
        
    def clear_settings(self) -> None:
        self.__settings.clear()
    
    
    # Getters and Setters
        
    def get_temperature(self) -> float:
        return self.__temperature
    
    def set_temperature(self, temperature: float) -> None:
        if temperature > 2 or temperature < 0:
            raise ValueError(f"temperature = {temperature}. temperature must be between 0 and 2")
        self.__temperature = temperature
        
    def get_max_tokens(self) -> int:
        return self.__max_tokens
    
    def set_max_tokens(self, max_tokens: int) -> None:
        if max_tokens < 0:
            raise ValueError(f"max_tokens = {max_tokens}. max_tokens must be >= 0")
        self.__max_tokens = max_tokens
    
    
    # Auxilliary
    
    def reset(self) -> None:
        self.clear_settings()
        self.clear_messages()
        
    def __str__(self) -> str:
        messages = [
            f"{self.__user if message['role'] == 'user' else self.__assistant}:\n{message['content']}"
            for message in self.__messages
        ]
        return "\n\n".join(messages)
    
if __name__ == "__main__":
    chat = Conversation("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")
    chat.say("hello")
    chat.say("when is christmas?")
    chat.say("write me a limerick")
    print(chat)