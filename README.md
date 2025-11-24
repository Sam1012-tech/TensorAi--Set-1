# AI CODEFIX 2025 - Easy Challenge
## Navigate Namma Bengaluru (Bangalore Wumpus World)

---

## Problem Statement

You are required to implement an **A\* pathfinding algorithm** for a Bangalore-themed variant of the classic Wumpus World. The agent must navigate a 5×10 grid filled with real-world Bangalore obstacles to reach the goal safely.

---

## World Description

### Grid Layout
- **Size:** 5 rows × 10 columns
- **Agent Start:** Bottom-left diagonal cell (0, 4)
- **Goal:** Randomly placed (varies per team based on seed)

### Environmental Elements

| Element | Percept | Effect |
|---------|---------|--------|
| **Traffic Light** | Adjacent cells detect "light" indicator | Agent must wait (nested loop delay) |
| **Cow** | Adjacent cells detect "moo" sound | Agent resets to start position |
| **Pit** | Adjacent cells detect "breeze" | **Game Over** if entered |
| **Goal** | No percept | **Win** if reached |

---

## What's Already Implemented ✅

The starter code (`wumpus_world.py`) provides:

- ✅ Pygame visualization of 5×10 grid
- ✅ Random world generation (using your team's unique seed)
- ✅ Percept detection system (breeze, moo, light)
- ✅ Traffic light delay mechanism (nested loop)
- ✅ Cow collision → reset to start
- ✅ Pit detection → Game Over
- ✅ Manual movement controls (arrow keys)
- ✅ Game state management

---

## What You Must Implement 🔨

### Task: Complete the `find_path_astar()` function

**Location:** `wumpus_world.py`, line ~170

**Requirements:**

1. **Implement A\* pathfinding** from agent's current position to goal
2. **Movement rules:**
   - Only **orthogonal movement** (up, down, left, right)
   - **NO diagonal movement allowed**
3. **Handle obstacles:**
   - **Pits:** Must avoid completely (entering = Game Over)
   - **Traffic Lights:** Can pass through but cost more (suggest cost = 5)
   - **Cows:** Strategy choice:
     - Option A: Avoid cows completely
     - Option B: Handle collision and replan from start
4. **Return value:**
   - List of (x, y) tuples representing path
   - Example: `[(0, 4), (1, 4), (2, 4), ...]`
   - Return `None` if no path exists

---

## Algorithm Hints

### A\* Formula
```
f(n) = g(n) + h(n)
```
- **g(n)** = actual cost from start to node n
- **h(n)** = heuristic estimate from n to goal (use Manhattan distance)
- **f(n)** = total estimated cost

### Cost Function
```python
def get_cell_cost(x, y):
    cell_type = self.grid[y][x]['type']
    if cell_type == 'pit':
        return float('inf')  # Avoid pits
    elif cell_type == 'traffic_light':
        return 5  # Higher cost due to wait
    elif cell_type == 'cow':
        return 10  # Higher cost (or avoid completely)
    else:
        return 1  # Normal cell
```

### Manhattan Distance Heuristic
```python
def heuristic(pos, goal):
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
```

### Key Considerations

⚠️ **No Diagonal Movement**
- When generating neighbors, only use: `[(0,-1), (0,1), (-1,0), (1,0)]`
- Do NOT use diagonal directions like `(1,1)` or `(-1,-1)`

⚠️ **Cow Collision Handling**
- If your path crosses a cow, the agent resets to start
- You need to either:
  - Avoid cows entirely in your pathfinding
  - OR detect collision and replan from start position

⚠️ **Path Not Found**
- If no valid path exists, set `self.message = "Path Not Found"`
- Return `None`

---

## How to Run

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python wumpus_world.py
```

### Controls
- **Arrow Keys:** Manual movement (for testing)
- **SPACE:** Execute A\* pathfinding (once implemented)
- **R:** Reset world with same seed
- **ESC:** Quit

---

## Testing Your Solution

### Test Cases
1. **Basic Path:** Can agent reach goal on empty grid?
2. **Avoid Pits:** Does A\* route around pits correctly?
3. **Traffic Lights:** Does path account for traffic light costs?
4. **No Path:** Does it return "Path Not Found" when goal is unreachable?
5. **Cow Handling:** What happens if only path includes a cow?

### Expected Output
When you press **SPACE**, you should see:
```
=== Executing A* Pathfinding ===
Path found: [(0, 4), (1, 4), (2, 4), (2, 3), (3, 3), ...]
```
Agent should then automatically navigate to the goal.

---

## Submission Checklist

- [ ] `find_path_astar()` function fully implemented
- [ ] A\* algorithm correctly uses Manhattan distance heuristic
- [ ] No diagonal movement in path
- [ ] Pits are avoided (never entered)
- [ ] Traffic lights handled (higher cost or proper logic)
- [ ] Cow collision strategy decided and implemented
- [ ] "Path Not Found" message displayed when no path exists
- [ ] Agent successfully reaches goal when path exists
- [ ] Code is clean and well-commented

---

## Debugging Tips

### Print Debugging
Add these to understand your A\* logic:
```python
print(f"Current node: {current}")
print(f"Goal: {goal}")
print(f"f_score[current]: {f_score[current]}")
print(f"Neighbors: {neighbors}")
```

### Visualize Open Set
```python
print(f"Open set size: {len(open_set)}")
print(f"Visited nodes: {len(visited)}")
```

### Check Path Validity
```python
for step in path:
    cell_type = self.grid[step[1]][step[0]]['type']
    print(f"{step} -> {cell_type}")
```

---

## Scoring Criteria

| Criteria | Points |
|----------|--------|
| A\* correctly implemented | 40% |
| Reaches goal successfully | 30% |
| Handles all obstacles correctly | 20% |
| Code quality & comments | 10% |

---

## FAQs

**Q: Can I use libraries like `heapq` for priority queue?**
A: Yes! Python's `heapq` is perfect for A\*.

**Q: What if multiple paths have same cost?**
A: Any valid optimal path is acceptable.

**Q: Should I avoid cows or handle reset?**
A: Your choice! Both strategies are valid if implemented correctly.

**Q: Can I modify other functions besides `find_path_astar()`?**
A: Yes, but document your changes clearly.

**Q: How do I know my team's unique configuration?**
A: Check `team_config.json` - each team has a different seed.

---

## Resources

- [A\* Pathfinding Tutorial](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [Python heapq Documentation](https://docs.python.org/3/library/heapq.html)
- [Manhattan Distance](https://en.wikipedia.org/wiki/Taxicab_geometry)

---

**Good luck, and may your paths be optimal!** 🚀

---

**Event:** AI CODEFIX 2025
**Organized by:** Dept. of AI&ML & AI&DS
**In collaboration with:** AI Planet, Agrowvitz, Tensor AI Club
