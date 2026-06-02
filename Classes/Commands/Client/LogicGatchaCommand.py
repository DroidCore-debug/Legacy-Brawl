import json
import random

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicGatchaCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(fields["BoxID"])
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["BoxID"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        
        box_id = fields.get("BoxID", 0)
        
        # Default rewards
        coins_reward = 100
        gems_reward = 10
        
        if box_id == 10:  # Mega Box
            coins_reward = 1000
            gems_reward = 50
        elif box_id == 14:  # Big Box
            coins_reward = 300
            gems_reward = 20
            
        player_data["Coins"] = player_data.get("Coins", 0) + coins_reward
        player_data["Gems"] = player_data.get("Gems", 0) + gems_reward
        
        # Deduct box cost if necessary, but usually game client handles purchase deduction.
        # Save updated data
        db_instance.updatePlayerData(player_data, calling_instance)
        
        # Send OutOfSync to reload and refresh client state cleanly
        Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0})

    def getCommandType(self):
        return 500
