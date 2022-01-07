from answer import Answer


class FunctionAnswer(Answer):
    def __init__(self, function_answer, confirm=True, **kwargs):
        super().__init__(**kwargs)
        self.function_answer = function_answer
        self.confirm = confirm

    async def send_answer(self, message, client):
        self.function_answer(message)
        await message.react("👌")
