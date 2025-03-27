# fenics/attack/attack_types/delay.py

import random
import time
import logging
from typing import Optional

from fenics.attack.attack_types.base import Attack


class DelayAttack(Attack):
    """Delay attack that simulates network delay by sleeping."""
    
    def __init__(self, node_id: int, logger: Optional[logging.Logger] = None):
        """
        Initialize the delay attack.
        
        Args:
            node_id: ID of the attacker node
            logger: Logger instance
        """
        super().__init__(node_id, logger)
    
    def execute(self) -> float:
        """
        Execute the delay attack by sleeping for a random amount of time.
        
        Returns:
            Total time spent including the delay
        """
        start_time = time.time()
        
        # Using the exact same delay range as the original code
        delay_duration = random.uniform(500, 700)
        self.logger.info(f"[node_{self.node_id}] Delaying sending updates by {delay_duration:.2f} seconds.")
        
        # Simulate network delay
        time.sleep(delay_duration)
        
        # Calculate total time spent
        end_time = time.time()
        sending_time = end_time - start_time
        
        return sending_time

# import random
# import time
# import logging
# from typing import Optional

# from dfl_simulator.attack.attack_types.base import Attack


# class DelayAttack(Attack):
#     """Delay attack that simulates network delay by sleeping."""
    
#     def __init__(self, node_id: int, min_delay: float = 0.5, max_delay: float = 2.0, logger: Optional[logging.Logger] = None):
#         """
#         Initialize the delay attack.
        
#         Args:
#             node_id: ID of the attacker node
#             min_delay: Minimum delay in seconds
#             max_delay: Maximum delay in seconds
#             logger: Logger instance
#         """
#         super().__init__(node_id, logger)
#         self.min_delay = min_delay
#         self.max_delay = max_delay
    
#     def execute(self) -> float:
#         """
#         Execute the delay attack by sleeping for a random amount of time.
        
#         Returns:
#             Actual delay duration in seconds
#         """
#         delay_duration = random.uniform(self.min_delay, self.max_delay)
#         self.logger.info(f"[node_{self.node_id}] Executing delay attack with duration {delay_duration:.2f} seconds")
        
#         # Simulate network delay
#         time.sleep(delay_duration)
        
#         self.logger.info(f"[node_{self.node_id}] Delay attack completed")
#         return delay_duration