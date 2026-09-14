import random
import json
import os
from typing import Dict, Set, Tuple
from endstone.plugin import Plugin
from endstone.command import Command, CommandContext
from endstone.event import player_event
from endstone.player import Player


class RTPPlugin(Plugin):
    """Random Teleport Plugin for Endstone Bedrock Server"""
    
    api_version = "0.1"
    
    def __init__(self):
        super().__init__()
        self.used_locations: Set[Tuple[int, int, int]] = set()
        self.config = {}
        self.config_file = None
        
    def on_load(self) -> None:
        """Called when the plugin is loaded"""
        self.logger.info("RTP Plugin loading...")
        self.load_config()
        self.register_commands()
        
    def on_enable(self) -> None:
        """Called when the plugin is enabled"""
        self.logger.info("✓ RTP Plugin enabled successfully!")
        self.logger.info(f"Short range: {self.config['short_range']} blocks")
        self.logger.info(f"Long range: {self.config['long_range']} blocks")
        
    def on_disable(self) -> None:
        """Called when the plugin is disabled"""
        self.logger.info("RTP Plugin disabled")
        self.save_config()
        
    def load_config(self) -> None:
        """Load configuration from file"""
        plugin_dir = self.get_data_folder()
        self.config_file = os.path.join(plugin_dir, "config.json")
        
        default_config = {
            "short_range": 100,
            "long_range": 1000,
            "y_min": 0,
            "y_max": 256,
            "safe_ground_search": True,
            "max_attempts": 50,
            "cooldown": 5
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            except:
                self.config = default_config
        else:
            self.config = default_config
            os.makedirs(plugin_dir, exist_ok=True)
            self.save_config()
            
    def save_config(self) -> None:
        """Save configuration to file"""
        if self.config_file:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
                
    def get_data_folder(self) -> str:
        """Get the data folder for the plugin"""
        data_folder = os.path.join(os.getcwd(), "plugins", "endstone-rtp-plugin")
        return data_folder
        
    def register_commands(self) -> None:
        """Register RTP commands"""
        pass  # Commands are handled by Endstone automatically
        
    def generate_safe_location(self, player: Player, range_distance: int) -> Tuple[float, float, float] | None:
        """Generate a random safe teleport location
        
        Args:
            player: The player to teleport
            range_distance: Distance range for teleportation
            
        Returns:
            Tuple of (x, y, z) coordinates or None if no safe location found
        """
        player_pos = player.location
        player_x = int(player_pos.x)
        player_z = int(player_pos.z)
        
        for attempt in range(self.config['max_attempts']):
            # Generate random coordinates
            x = player_x + random.randint(-range_distance, range_distance)
            z = player_z + random.randint(-range_distance, range_distance)
            
            # Check if location already used
            if (x, z) in self.used_locations:
                continue
                
            # Find safe Y coordinate
            if self.config['safe_ground_search']:
                # Try to find ground level
                y = self.find_ground_level(player.world, x, z)
                if y is None:
                    continue
            else:
                y = random.randint(
                    self.config['y_min'],
                    self.config['y_max']
                )
            
            # Mark location as used
            self.used_locations.add((x, z))
            
            # Limit stored locations to prevent memory issues
            if len(self.used_locations) > 1000:
                self.used_locations.clear()
            
            return (float(x + 0.5), float(y), float(z + 0.5))
            
        return None
        
    def find_ground_level(self, world, x: int, z: int) -> int | None:
        """Find safe ground level at given coordinates
        
        Args:
            world: The world to search in
            x: X coordinate
            z: Z coordinate
            
        Returns:
            Safe Y coordinate or None
        """
        try:
            # Search from top to bottom
            for y in range(self.config['y_max'], self.config['y_min'], -1):
                # Get block at position
                block = world.get_block_at(x, y, z)
                
                # Check if block is solid
                if block and block.is_solid():
                    # Return Y position above the block
                    return y + 1
                    
        except:
            pass
            
        return None
