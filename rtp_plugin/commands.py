from endstone.command import Command, CommandUsage
from endstone.player import Player
from rtp_plugin.plugin import RTPPlugin
import time


class RTACommand(Command):
    """Random Teleport Any Distance command"""
    
    def __init__(self, plugin: RTPPlugin):
        super().__init__("rta", "Random teleport any distance")
        self.plugin = plugin
        self.player_cooldowns = {}
        
    def on_execute(self, context: CommandContext) -> bool:
        """Execute the RTA command"""
        sender = context.sender
        
        if not isinstance(sender, Player):
            sender.send_message("§cThis command can only be used by players!")
            return False
            
        # Check cooldown
        if not self.check_cooldown(sender):
            sender.send_message(
                f"§cPlease wait before using RTP again!"
            )
            return False
            
        # Generate random location with long range
        location = self.plugin.generate_safe_location(
            sender,
            self.plugin.config['long_range']
        )
        
        if location is None:
            sender.send_message(
                "§cCould not find a safe location! Try again."
            )
            return False
            
        # Teleport player
        sender.teleport(location[0], location[1], location[2])
        sender.send_message(
            f"§a✓ Teleported to random location!"
            f"\n§7X: §b{int(location[0])} §7Y: §b{int(location[1])} §7Z: §b{int(location[2])}"
        )
        
        return True
        
    def check_cooldown(self, player: Player) -> bool:
        """Check if player is on cooldown"""
        current_time = time.time()
        cooldown = self.plugin.config.get('cooldown', 5)
        
        if player.name in self.player_cooldowns:
            if current_time - self.player_cooldowns[player.name] < cooldown:
                return False
                
        self.player_cooldowns[player.name] = current_time
        return True


class RTSCommand(Command):
    """Random Teleport Short distance command"""
    
    def __init__(self, plugin: RTPPlugin):
        super().__init__("rts", "Random teleport short distance")
        self.plugin = plugin
        self.player_cooldowns = {}
        
    def on_execute(self, context: CommandContext) -> bool:
        """Execute the RTS command"""
        sender = context.sender
        
        if not isinstance(sender, Player):
            sender.send_message("§cThis command can only be used by players!")
            return False
            
        # Check cooldown
        if not self.check_cooldown(sender):
            sender.send_message(
                f"§cPlease wait before using RTP again!"
            )
            return False
            
        # Generate random location with short range
        location = self.plugin.generate_safe_location(
            sender,
            self.plugin.config['short_range']
        )
        
        if location is None:
            sender.send_message(
                "§cCould not find a safe location! Try again."
            )
            return False
            
        # Teleport player
        sender.teleport(location[0], location[1], location[2])
        sender.send_message(
            f"§a✓ Teleported nearby!"
            f"\n§7X: §b{int(location[0])} §7Y: §b{int(location[1])} §7Z: §b{int(location[2])}"
        )
        
        return True
        
    def check_cooldown(self, player: Player) -> bool:
        """Check if player is on cooldown"""
        current_time = time.time()
        cooldown = self.plugin.config.get('cooldown', 5)
        
        if player.name in self.player_cooldowns:
            if current_time - self.player_cooldowns[player.name] < cooldown:
                return False
                
        self.player_cooldowns[player.name] = current_time
        return True
