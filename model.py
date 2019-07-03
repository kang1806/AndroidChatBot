from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer



bot = ChatBot(
    'Test',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.db'
)


trainer1 = ListTrainer(bot)
trainer2 = ChatterBotCorpusTrainer(bot)

trainer2.train(
    "chatterbot.corpus.english"
)

trainer1.train([
    "just testing",
    "it work, wow"
])
