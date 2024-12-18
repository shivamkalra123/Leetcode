from typing import Optional, List
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Queue for level order traversal
        
        level = 0  # To track the current level (odd or even)
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the level if it's an odd level (1-based index)
            if level % 2 == 1:
                current_level.reverse()
            
            result.append(current_level)
            level += 1  # Increment level counter
        
        return result
